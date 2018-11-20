from Motor import Drive  
import RPi.GPIO as GPIO
import time 

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

R_Motor_Ena = 0
L_Motor_Ena = 26
R_In1 = 5
R_In2 = 6
L_In3 = 13
L_In4 = 19

Right_Motor = Drive(R_In1, R_In2, R_Motor_Ena)
Left_Motor = Drive(L_In3, L_In4, L_Motor_Ena)

Right_Motor.Forward
Left_Motor.Forward
time.sleep(5)



