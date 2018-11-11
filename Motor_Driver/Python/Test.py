import RPi.GPIO as GPIO # GPIO pin library
import time
import curses 


GPIO.setwarnings(False) #do not show any warnings
GPIO.setmode(GPIO.BCM)

GPIO.setup(2,GPIO.OUT) # Right motor enable pin 
GPIO.setup(3,GPIO.OUT) # Right motor in pin 1
GPIO.setup(4,GPIO.OUT) # Right motor in pin 2
GPIO.setup(17,GPIO.OUT)# Left motor enable pin 
GPIO.setup(27,GPIO.OUT)# Left motor in pin 1
GPIO.setup(22,GPIO.OUT)# Left motor in pin 2


# Reset left and right motors 
GPIO.output(2,GPIO.LOW)
GPIO.output(17,GPIO.LOW)

GPIO.output(3,GPIO.HIGH)
GPIO.output(4,GPIO.LOW)
GPIO.output(27,GPIO.HIGH)
GPIO.output(22,GPIO.LOW)

