# motor.py

############################################
# Library                                  #
############################################

import time
from roboclaw import Roboclaw
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

############################################
# Linux comport name                       #
############################################
rc = Roboclaw("/dev/ttyACM3",115200)

#################################################
# M1 & M2 Tuned values from robocalw software   #                     
#################################################
PID1 = [56.54683, 1.62558, 487.67500]
PID2 = [52.02308, 1.38718, 416.15451]

QPPS1 = 3000
QPPS2 = 3000

###########################################################
# Function to Initalize Encoders and Read Encoder values  #
###########################################################
def displayspeed():
        enc1 = rc.ReadEncM1(0x80)            # Read Motor 1
        enc2 = rc.ReadEncM2(0x80)            # Read Motor 2
        speed1 = rc.ReadSpeedM1(0x80)        # Speed for Motor 1
        speed2 = rc.ReadSpeedM2(0x80)        # Speed for Motor 2
        
        PIDQ1_Vals = rc.ReadM1VelocityPID(0x80)
        PIDQ2_Vals = rc.ReadM2VelocityPID(0x80)
        
        pinFuncs = rc.ReadPinFunctions(0x80)

        print("PID Values for M1 = ", PIDQ1_Vals)
        print("PID Values for M2 = ", PIDQ2_Vals)
        print("Pin Functions are:", pinFuncs)

        #################
        # Encoders      #
        #################
        print("Encoder1:")
        if(enc1[0]==1):
                print(enc1[1])
                print(format(enc1[2],'02x'))
        else:
                print("failed")
                
	print("Encoder2:")
        if(enc2[0]==1):
                print(enc2[1])
                print(format(enc2[2],'02x'))
        else:
                print("failed")
		
        ##############
        # Speed      #  
        ##############
        print("Speed1:")
        if(speed1[0]):
                print(speed1[1])
        else:
                print("failed")
		
        print("Speed2:")
        if(speed2[0]):
                print(speed2[1])
        else:
                print("failed")
		
############################################
# Setup linux usb port communication       #
############################################
rc.Open()
address = 0x80

############################################
# Reset back to tuned PID values           #
############################################
rc.SetM1VelocityPID(address, PID1[0], PID1[1], PID1[2], QPPS1)
rc.SetM2VelocityPID(address, PID2[0], PID2[1], PID2[2], QPPS2)

#########################
# Forward               #
#########################
def up():
        print("UP")
        rc.ForwardM1(address, 100)
        rc.ForwardM2(address, 100)

#########################
# Back                  #
#########################
def down():
        rc.BackwardM1(address, 100)
        rc.BackwardM2(address, 100)

#########################
# Left                  #
#########################
def left():
        rc.ForwardM1(address, 100)
        rc.BackwardM2(address, 100)

#########################
# Right                 #
#########################
def right():
        rc.ForwardM1(address, 100)
        rc.BackwardM2(address, 100)
        
        
#########################
# stop                  #
#########################
def stop():
        rc.BackwardM1(address, 0)
        rc.BackwardM2(address, 0)
        rc.ForwardM1(address, 0)
        rc.ForwardM2(address, 0)
        rc.TurnRightMixed(address, 0)


#displayspeed()
rc.ResetEncoders(address)


