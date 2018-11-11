import RPi.GPIO as GPIO # GPIO pin library
import time

GPIO.setwarnings(False) #do not show any warnings
GPIO.setmode(GPIO.BCM)

# Right Motor      
motorRENPin  = 2  # GPIO23
motorRIN2Pin = 3  # GPIO3
motorRIN1Pin = 4  # GPIO4

# Left Motor 
motorLENPin  = 17 # GPIO17
motorLIN2Pin = 27 # GPIO 27 
motorLIN1Pin = 22 # GPIO22


# Right Motor 
GPIO.setup(motorRENPin, GPIO.OUT) # Ena GPIO2
GPIO.setup(motorRIN2Pin, GPIO.OUT) # GPIO 3
GPIO.setup(motorRIN1Pin, GPIO.OUT) # GPIO 4

# Intialize turn motor off at first 
GPIO.output(motorRENPin, GPIO.LOW) # GPIO2 = 0

#Left Motor 
GPIO.setup(motorLENPin,  GPIO.OUT) 
GPIO.setup(motorLIN2Pin, GPIO.OUT)
GPIO.setup(motorLIN1Pin, GPIO.OUT)

# Intialize turn motor off at first 
GPIO.output(motorLENPin, GPIO.LOW)

###################################################
# PWM
p = GPIO.PWM(2,207) #10 blue
p = GPIO.PWM(17,207) #5 brown
p.start(0)


#p.ChangeDutyCycle(90)
try:
    while 1:
        for i in range(100):
                p.ChangeDutyCycle(i)
                time.sleep(0.02)
                
        # Right Motor 
        GPIO.output(motorRIN1Pin, GPIO.HIGH) # GPIO 4, 8
        GPIO.output(motorRIN2Pin, GPIO.LOW) # GPIO 3, 9
        time.sleep(0.02)
    
        #Left Motor 
        GPIO.output(motorLIN1Pin, GPIO.HIGH) # GPIO 4, 6
        GPIO.output(motorLIN2Pin, GPIO.LOW)  # GPIO 3, 7
        time.sleep(0.02)
        
except KeyboardInterrupt:
    pass
p.stop()
GPIO.cleanup()