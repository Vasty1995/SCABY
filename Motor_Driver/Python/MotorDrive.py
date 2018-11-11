import RPi.GPIO as GPIO # GPIO pin library
import time
import curses 

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

try:
    while True:
                  char = screen.getch()
                      if char == ord('q'):
                                 break
                      elif char == curses.KEY_UP:
                                 print "UP"
                      elif char == curses.KEY_DOWN 

GPIO.setwarnings(False) #do not show any warnings
GPIO.setmode(GPIO.BCM)

# Right Motor      
motorRENPin  = 2  # GPIO2
motorRIN2Pin = 3  # GPIO3
motorRIN1Pin = 4  # GPIO4

# Left Motor 
motorLENPin  = 17 # GPIO17
motorLIN2Pin = 27 # GPIO27 
motorLIN1Pin = 22 # GPIO22


# Right Motor 
GPIO.setup(motorRENPin, GPIO.OUT)  # GPIO2 : Right Motor Enable pin 
GPIO.setup(motorRIN2Pin, GPIO.OUT) # GPIO3
GPIO.setup(motorRIN1Pin, GPIO.OUT) # GPIO4

#Left Motor 
GPIO.setup(motorLENPin,  GPIO.OUT) # GPIO17 : Left Motor Enable pin 
GPIO.setup(motorLIN2Pin, GPIO.OUT) # GPIO27
GPIO.setup(motorLIN1Pin, GPIO.OUT) # GPIO22

# Start both motors from an off state.
GPIO.output(motorRENPin, GPIO.LOW) # GPIO2 = 0
GPIO.output(motorLENPin, GPIO.LOW) # GPIO17 = 0

###################################################
# PWM
# To start pwm => p = GPIO.PWM(Pin# , frequency)
p = GPIO.PWM(2,207)  # Pin 2 @ f = 207Hz
p = GPIO.PWM(17,207) # Pin 17 @f = 207Hz
p.start(0) # p.start(dc), dc = duty cycle 
           # (0.0 <= dc <= 100.0)
# To chane frequency: p.ChangeFrequncy(freq) where freq is the new frequncy in Hz
# To stop PWM: p.stop()

try:
    while 1:
# Loop Statments in Python
# for x in range(6):
#   print(x) 
# prints: 0 1 2 3 4 5
# To sepecify an incrment 
# for x in range(0,6,2)
       # for i in range(100): # Increments i up to 100 starting form 0 
        #        p.ChangeDutyCycle(i) # Duty cycle changes by every 0.02 seconds up untill it reaches 99
         #       time.sleep(0.02)
                
        # Right Motor move forward 
        # IN1 = 1 && IN2 = 0   
        GPIO.output(motorRIN1Pin, GPIO.HIGH) # GPIO4 = 1: 
        GPIO.output(motorRIN2Pin, GPIO.LOW)  # GPIO3 = 0
       # time.sleep(0.02)
    
        # Left Motor move forward 
        # IN3 = 1 && IN4 = 0
        GPIO.output(motorLIN1Pin, GPIO.HIGH) # GPIO22
        GPIO.output(motorLIN2Pin, GPIO.LOW)  # GPIO27
        #time.sleep(0.02)
        
except KeyboardInterrupt:
    pass
p.stop()
GPIO.cleanup()
