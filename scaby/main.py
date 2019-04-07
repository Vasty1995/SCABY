########################################################################################################
# Class Declarations                                                                                   #              
########################################################################################################
#import motor     # Includes all the manuever fucntions  
#from numcrunch import crunch            # Calculates distance(Imd,Lbd,Rbd, zlb and zrb)
from marvelmind import MarvelmindHedge  # Marvelmind class, claculates Left and Right Beacon values

import time
from time import sleep
import sys
import RPi.GPIO as GPIO
import math

####################################################################
# Pi GPIO Initalize                                                #              
####################################################################    
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

####################################################################
# Import Distance Calculations  and Motor Control functions        #              
####################################################################

# call numcrunch.py file 
#robo = motor() # call motor.py file 

####################################################################
# SCABY Route Pattern Option: 1                                    #              
####################################################################
def SDbot():
    print("===================================================")
    print("                   SCABY")
    print("===================================================")
    print("\nThank you for choosing SCABY!")
    print("For a Horzontal mow Please enter 1 ")
    mrout = input("For a Vertical mow Please enter 2\n")

    return mrout
 

def HorzMow(Ho):
    if(Ho == 1):
        print("You have chosen Horzontal mow")
    else:
        return
####################################################################
# SCABY Route Pattern Option: 2                                    #              
####################################################################   
# Start Vertical mow
def VertMow(Vert):
    if(Vert == 2):
        print("You have chosen Vertical mow")
    else:
        return 

####################################################################
# Motor Control: from Motor.py                                     #              
####################################################################
def Steer():
     #while True:
      #  try:  
            #motor.up()
            #time.sleep(4) 
            #motor.stop()

            #motor.down()
            #time.sleep(4) 
            #motor.stop()

            motor.left()
            time.sleep(4) 
            motor.stop()

            #motor.right()
            
       # except KeyboardInterrupt:
        #    sys.exit()
        
####################################################################
# Test Function: from Marvelmind.py                                #              
####################################################################
def test():
    LeftB = MarvelmindHedge(tty = "/dev/ttyACM0", adr = 1, debug = False) # Beacon 2
    #RightB = MarvelmindHedge(tty = "/dev/ttyACM1", adr = 2, debug = False) # Beacon 1

    LeftB.start()
    #RightB.start()
    while True:
        try:
            sleep(1)
            #LeftB.print_position()
            LeftB.run()
           #RightB.run()
        
        #if(marv.return_angle() ==  )
         #   print("Left Beacon ########################")
          #  LeftB.b5()
            #LeftB.b6()
            #LeftB.b4()
            #LeftB.b3()

            #print("Right Beacon ########################")
            
            #RightB.b5()
            #RightB.b6()
           # RightB.b4()
            #RightB.b3()
            #marv.print_distances()

        except KeyboardInterrupt:
            LeftB.stop()
            RightB.stop()
            sys.exit()
            
####################################################################
# Call fucntions to execute                                        #              
####################################################################    
test()

#choice = SDbot()  
#HorzMow(choice)
#VertMow(choice)
#Steer()


GPIO.cleanup() # Cleans up used ports
