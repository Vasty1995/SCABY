import crcmod
import serial
import struct
import collections
import time
from threading import Thread
import math
from time import sleep
import sys
import RPi.GPIO as GPIO 
import sys

class MarvelmindHedge (Thread):
    def __init__ (self, adr=5, tty="/dev/ttyACM0", baud=9600, maxvaluescount=3, debug=False, recieveUltrasoundPositionCallback=None, recieveImuRawDataCallback=None, recieveImuDataCallback=None, recieveUltrasoundRawDataCallback=None):
        self.tty = tty  # serial
        self.baud = baud  # baudrate
        self.debug = debug  # debug flag
        self._bufferSerialDeque = collections.deque(maxlen=255)  # serial buffer

        self.valuesUltrasoundPosition = collections.deque([[0]*6]*maxvaluescount, maxlen=maxvaluescount) # ultrasound position buffer
        self.recieveUltrasoundPositionCallback = recieveUltrasoundPositionCallback
        
        self.valuesImuRawData = collections.deque([[0]*10]*maxvaluescount, maxlen=maxvaluescount) # raw imu data buffer
        self.recieveImuRawDataCallback = recieveImuRawDataCallback

        self.valuesImuData = collections.deque([[0]*14]*maxvaluescount, maxlen=maxvaluescount) # processed imu data buffer
        self.recieveImuDataCallback = recieveImuDataCallback

        self.valuesUltrasoundRawData = collections.deque([[0]*5]*maxvaluescount, maxlen=maxvaluescount)
        self.recieveUltrasoundRawDataCallback = recieveUltrasoundRawDataCallback


        self.pause = False
        self.terminationRequired = False
        self.xvalue_int = 0
        self.yvalue_int = 0
        self.adr = adr
        self.serialPort = None
        Thread.__init__(self)

    def Return_X_position(self):
        if (isinstance(self.position()[1], int)):
            self.xvalue_int = float(self.position()[1])
            return self.xvalue_int;
        else:
            self.xvalue_int = float(self.position()[1])
            return self.xvalue_int;
            
    def Return_Y_position(self):
        if (isinstance(self.position()[1], int)):
            self.yvalue_int = float(self.position()[2])
            return self.yvalue_int;
        else:
            self.yvalue_int = float(self.position()[2])
            return self.yvalue_int;
        
    def position(self):
        return list(self.valuesUltrasoundPosition)[-1];
    
    def stop(self):
        self.terminationRequired = True
        print ("stopping")

    def run(self):      
        while (not self.terminationRequired):
            if (not self.pause):
                try:
                    if (self.serialPort is None):
                        self.serialPort = serial.Serial(self.tty, self.baud, timeout=3)
                    readChar = self.serialPort.read(1)
                    while (readChar is not None) and (readChar is not '') and (not self.terminationRequired):
                        self._bufferSerialDeque.append(readChar)
                        readChar = self.serialPort.read(1)
                        bufferList = list(self._bufferSerialDeque)
                        
                        strbuf = (b''.join(bufferList))

                        pktHdrOffset = strbuf.find(b'\xff\x47')
                        if (pktHdrOffset >= 0 and len(bufferList) > pktHdrOffset + 4 and pktHdrOffset<220):
#                           print(bufferList)
                            isMmMessageDetected = False
                            isCmMessageDetected = False
                            isRawImuMessageDetected = False
                            isImuMessageDetected = False
                            isDistancesMessageDetected = False
                            pktHdrOffsetCm = strbuf.find(b'\xff\x47\x01\x00')
                            pktHdrOffsetMm = strbuf.find(b'\xff\x47\x11\x00')
                            pktHdrOffsetRawImu = strbuf.find(b'\xff\x47\x03\x00')
                            pktHdrOffsetDistances = strbuf.find(b'\xff\x47\x04\x00')
                            pktHdrOffsetImu = strbuf.find(b'\xff\x47\x05\x00')

                            if (pktHdrOffsetMm!=-1):
                                isMmMessageDetected = True
                                if (self.debug): print ('Message with US-position(mm) was detected')
                            elif (pktHdrOffsetCm!=-1):
                                isCmMessageDetected = True
                                if (self.debug): print ('Message with US-position(cm) was detected')
                            elif (pktHdrOffsetRawImu!=-1):
                                isRawImuMessageDetected = True
                                if (self.debug): print ('Message with raw IMU data was detected')
                            elif (pktHdrOffsetDistances!=-1):
                                isDistancesMessageDetected = True
                                if (self.debug): print ('Message with distances was detected')
                            elif (pktHdrOffsetImu!=-1):
                                isImuMessageDetected = True
                                if (self.debug): print ('Message with processed IMU data was detected')
                            msgLen = ord(bufferList[pktHdrOffset + 4])
                            if (self.debug): print ('Message length: ', msgLen)

                            try:
                                if (len(bufferList) > pktHdrOffset + 4 + msgLen + 2):
                                    usnCRC16 = 0
                                    if (isCmMessageDetected):
                                        usnTimestamp, usnX, usnY, usnZ, usnAdr, usnAngle, usnCRC16 = struct.unpack_from ('<LhhhxBhxxH', strbuf, pktHdrOffset + 5)
                                        usnX = usnX/100.0
                                        usnY = usnY/100.0
                                        usnZ = usnZ/100.0
                                        usnAngle = 0b0000111111111111&usnAngle
                                    elif (isMmMessageDetected):
                                        usnTimestamp, usnX, usnY, usnZ, usnAdr, usnAngle, usnCRC16 = struct.unpack_from ('<LlllxBhxxH', strbuf, pktHdrOffset + 5)
                                        usnX = usnX/1000.0
                                        usnY = usnY/1000.0
                                        usnZ = usnZ/1000.0
                                        usnAngle = 0b0000111111111111&usnAngle
                                    elif (isRawImuMessageDetected):
                                        ax, ay, az, gx, gy, gz, mx, my, mz, timestamp, usnCRC16 = struct.unpack_from ('<hhhhhhhhhxxxxxxLxxxxH', strbuf, pktHdrOffset + 5)
                                    elif (isImuMessageDetected):
                                        x, y, z, qw, qx, qy, qz, vx, vy, vz, ax, ay, az, timestamp, usnCRC16 = struct.unpack_from ('<lllhhhhhhhhhhxxLxxxxH', strbuf, pktHdrOffset + 5)

                                    crc16 = crcmod.predefined.Crc('modbus')
                                    crc16.update(strbuf[ pktHdrOffset : pktHdrOffset + msgLen + 5 ])
                                    CRC_calc = int(crc16.hexdigest(), 16)

                                    if CRC_calc == usnCRC16:
                                        if (isMmMessageDetected or isCmMessageDetected):
                                            value = [usnAdr, usnX, usnY, usnZ, usnAngle, usnTimestamp]
                                            if (self.adr == usnAdr or self.adr is None):
                                                self.valuesUltrasoundPosition.append(value)
                                                if (self.recieveUltrasoundPositionCallback is not None):
                                                    self.recieveUltrasoundPositionCallback()
                                        elif (isRawImuMessageDetected):
                                            value = [ax, ay, az, gx, gy, gz, mx, my, mz, timestamp]
                                            self.valuesImuRawData.append(value)
                                            if (self.recieveImuRawDataCallback is not None):
                                                self.recieveImuRawDataCallback()
                                        # elif (isDistancesMessageDetected):
                                        #     value = 
                                        #     self.valuesUltrasoundRawData.append(value)
                                        #     if (self.recieveUltrasoundRawDataCallback is not None):
                                        #         self.recieveUltrasoundRawDataCallback()
                                        elif (isImuMessageDetected):
                                            value = [x/1000.0, y/1000.0, z/1000.0, qw/10000.0, qx/10000.0, qy/10000.0, qz/10000.0, vx/1000.0, vy/1000.0, vz/1000.0, ax/1000.0,ay/1000.0,az/1000.0, timestamp]
                                            self.valuesImuData.append(value)
                                            if (self.recieveImuDataCallback is not None):
                                                self.recieveImuDataCallback()
                                    else:
                                        if self.debug:
                                            print ('\n*** CRC ERROR')

                                    if pktHdrOffset == -1:
                                        if self.debug:
                                            print ('\n*** ERROR: Marvelmind USNAV beacon packet header not found (check modem board or radio link)')
                                        continue
                                    elif pktHdrOffset >= 0:
                                        if self.debug:
                                            print ('\n>> Found USNAV beacon packet header at offset %d' % pktHdrOffset)
                                    for x in range(0, pktHdrOffset + msgLen + 7):
                                        self._bufferSerialDeque.popleft()
                            except struct.error:
                                print ('smth wrong')
                except OSError:
                    if self.debug:
                        print ('\n*** ERROR: OS error (possibly serial port is not available)')
                    time.sleep(1)
                except serial.SerialException:
                    if self.debug:
                        print ('\n*** ERROR: serial port error (possibly beacon is reset, powered down or in sleep mode). Restarting reading process...')
                    self.serialPort = None
                    time.sleep(1)
            else: 
                time.sleep(1)
    
        if (self.serialPort is not None):
            self.serialPort.close()
####################################################################################
            
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

####################################
# Initialize Rspi pins to be used  #
####################################
RM_En = 20  # Right Motor Enable
LM_En = 21  # Left Motor Enable
R_In1 = 25  # Right Motor pin 1
R_In2 = 8   # Right Motor pin 2
L_In1 = 1   # Left Motor pin 1
L_In2 = 7   # Left Motor pin 2

#######################################
# Setup pins to be used as an output  #
#######################################
GPIO.setup(RM_En, GPIO.OUT) 
GPIO.setup(LM_En, GPIO.OUT)
GPIO.setup(R_In1, GPIO.OUT)
GPIO.setup(R_In2, GPIO.OUT)
GPIO.setup(L_In1, GPIO.OUT)
GPIO.setup(L_In2, GPIO.OUT)

###################################################
# Speed control                                   #
###################################################
p_RM = GPIO.PWM(RM_En, 100) # p = pwm(port,frequncy)
p_RM.start(0)               # Duty Cycle 
p_LM = GPIO.PWM(LM_En, 100)
p_LM.start(0)

###################################
# Forward Drive                   #
###################################
def forward(RM_speed, LM_speed):
    p_RM.ChangeDutyCycle(RM_speed)
    p_LM.ChangeDutyCycle(LM_speed)
    
    print("Move Forward")
    GPIO.output(R_In1, 1)
    GPIO.output(R_In2, 0)
    GPIO.output(L_In1, 1)
    GPIO.output(L_In2, 0)

#################################
# Reverse Drive                 #
#################################
def reverse(RM_speed, LM_speed):
    p_RM.ChangeDutyCycle(RM_speed)
    p_LM.ChangeDutyCycle(LM_speed)
    
    print("Move Back")
    GPIO.output(R_In1, 0)
    GPIO.output(R_In2, 1)
    GPIO.output(L_In1, 0)
    GPIO.output(L_In2, 1)

#################
# Break Drive   #
#################
def break_M():
    print("STOP")
    GPIO.output(RM_En, 0)
    GPIO.output(R_In1, 0)
    GPIO.output(R_In2, 0)
    GPIO.output(L_In1, 0)
    GPIO.output(L_In2, 0)   
    GPIO.output(LM_En, 0)

#############################
# Turn Right                #
#############################

def turn_right():
    print("Turning Right")
    p_RM.ChangeDutyCycle(50)
    p_LM.ChangeDutyCycle(100)

#############################
# Turn Left                 #
#############################

def turn_left():
    print("Turning Left")
    p_RM.ChangeDutyCycle(100)
    p_LM.ChangeDutyCycle(50)
   
################################################################################################
# Left Beacon                                                                                  #
################################################################################################
hedge = MarvelmindHedge(tty = "/dev/ttyACM0", adr=5, debug=False) # create MarvelmindHedge threa
hedge.start() # start thread
sleep(1)

LB_X = hedge.Return_X_position() # Left Beacon X
print("Left Beacon X = ", LB_X)
            
LB_Y = hedge.Return_Y_position() # Left Beacon Y
print("Left Beacon Y = ", LB_Y)

LB_len = math.sqrt( (LB_X * LB_X) + (LB_Y * LB_Y) )  
################################################################################################
# Right Beacon                                                                                 #
################################################################################################
hedge = MarvelmindHedge(tty = "/dev/ttyACM1", adr=6, debug=False) 
hedge.start() # start thread
sleep(1)

RB_X = hedge.Return_X_position()
print("Right Beacon X =", RB_X)
            
RB_Y = hedge.Return_Y_position()
print("Right Beacon Y = ", RB_Y)

RB_len = math.sqrt( (RB_X * RB_X) + (RB_Y * RB_Y) )
################################################################################################
# Imginary                                                                                 #
################################################################################################
while 1:
    Imgx = round(LB_X + ((RB_X - LB_X)/2), 3);
    Imgy = round(LB_Y + ((RB_Y - LB_Y)/2), 3);
    print("Imgx =  ",Imgx,"\nImgy = ",Imgy)

    ################
    # Waypoint 
    WPx = 0
    WPy = 0
    
    #####################
    # Imagianry Distance to way point
    Im_dis = math.sqrt( (WPx-Imgx)*(WPx - Imgx) + (WPy - Imgy )*(WPy - Imgy) )
    
    ################
    # Left and Right Beacon distance to a given way point
    RB_Z = RB_len / Im_dis
    LB_Z = LB_len / Im_dis
################################################################################################
# Length for Left and Right Beacon
#
################################################################################################
    
    
'''
##### Starting Position  ####
T1m = 4.25

if(Y_Lawn_Length < 1.7):
    forward(70, 70);
    time.sleep(2*T1m)
    turn_right();
    time.sleep(T1m/2.5)
    
    forward(70, 70);
    time.sleep(T1m)
    
    turn_right();
    time.sleep(T1m/2.5)
    
    forward(70, 70);
    time.sleep(2*T1m)
    turn_right();
    time.sleep(T1m/2)
    
    forward(70, 70);
    time.sleep(T1m)
    
    
else:
    break_M();


p_RM.stop()    # Stop speed (pwm)
p_LM.stop()    # Stop speed (pwm)
'''
hedge.stop()  # stop and close serial port
GPIO.cleanup() # Cleans up used ports 
sys.exit()

