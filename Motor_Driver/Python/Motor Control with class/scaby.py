from Motor import Drive
import RP.GPIO as GPIO
import time
#GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BCM)

#############################################3
# Initialize Rspi pins to be used

R_Motor_Ena = 0     # Right Motor Enable
L_Motor_Ena = 26    # Left Motor Enable
R_In1 = 5           # Right Motor pin 1
R_In2 = 6           # Right Motor pin 2
L_In1 = 13          # Left Motor pin 1
L_In2 = 19          # Left Motor pin 2


Right_Motor = Drive(R_In1, R_In2, R_Motor_Ena)
Left_Motor = Drive(L_In1, L_In2, L_Motor_Ena)

Right_Motor.forward()
Left_Motor.forward()

