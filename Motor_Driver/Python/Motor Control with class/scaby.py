# scaby.py 
#
from Motor import Drive
import RPi.GPIO as GPIO
import time

#############################################3
# Initialize Rspi pins to be used

RM_En = 0     # Right Motor Enable
LM_En = 26    # Left Motor Enable
R_In1 = 5           # Right Motor pin 1
R_In2 = 6           # Right Motor pin 2
L_In1 = 13          # Left Motor pin 1
L_In2 = 19          # Left Motor pin 2


Right_Motor = Drive(R_In1, R_In2, RM_En)
Left_Motor = Drive(L_In1, L_In2, LM_En)

Stop_RM =  Drive(R_In1, R_In2, RM_En)
Stop_LM = Drive(L_In1, L_In2, LM_En)

Right_Motor.forward()
#time.sleep(2)
Left_Motor.forward()
#time.sleep(2)

Stop_RM.break_M()
Stop_LM.break_M()

############################################################
# End
#
