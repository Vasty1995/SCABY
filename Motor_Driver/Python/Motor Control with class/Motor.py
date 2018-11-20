class Drive:
    pin1 = 0
    pin2 = 0
    pinEN = 0

    def __init__(self, pin1, pin2, pinEN):
        self.pin1 = pin1
        self.pin2 = pin2
        self.pinEN = pinEN
        """
    
        GPIO.setup(self.pin1, GPIO.OUTPUT)
        GPIO.setup(self.pin2, GPIO.OUTPUT)
        GPIO.setup(self.pinEN, GPIO.OUTPUT)
        
        GPIO.output(self.pinEN, 0)
        """
    def forward(self):
        return self.pin1
        print self.pin2
        print self.pinEN


"""    return GPIO.output(self.pin1, 1)
        return GPIO.output(self.pin2, 0)
        return GPIO.output(self.pinEna, 1)


##############################################

DC Motors can turn in two directions.
The turn directions are controlled by the power being applied to the motor.

An H Bridge is used to control => direction of the motor. 
                               => speed 
                               => break 
  1. L298 H Bridge  
     H Bridge: a circuit which allows a voltage to be applied across a load (motor) in either direction 
             : has 4 switches arranged in an "H" fashion 

    L298 H Bridge Hardware Logic:
       Left                                         Right
     _____________________________________________
    |  L_pin1 = 1  |                              |  
    |              |   Out1   ________   Out2     | 3 = R_pin3
    +              |_________|  Motor |___________|  
    _              |         |________|           | 
    |  L_pin2 = 2  |                              | 4 = R_pin4
    |______________|______________________________|

        L_pin1 = IN1 && EN 
        L_pin2 = ~IN1 && EN

        R_pin3 = IN2 && EN
        R_pin3 = ~IN2 && EN

        Out1 & Out2 can only be either postive(closed) or negative(open)    

 ###########
 Forward Drive (spin Motor Clockwise) 
 
     Make EN = 1 , IN1 = 0,  IN2 = 1
    _________________________________________
   |                                        |
   |     1   Out1(-)   ________  Out2 (+)   | 3     
   +        __________|  Motor |____________|      
   _       |          |________|                           
   |     2 |                                  4           
   |_______|________________________________
        
        Out1                             |  Out2 
     ----------------------------------------------------------------------------
        L_pin1 = IN1 && EN =  0 & 1 = 0  |   R_pin3 = IN2 && EN  = 1 & 1 = 1 (+)
    (-) L_pin2 = ~IN1 && EN = 1 & 1 = 1  |   R_pin4 = ~IN2 && EN = 0 & 1 = 0  
        
###########
 Reverse Drive (spin Motor CounterClockwise) 
 
     Make EN = 1 , IN1 = 1,  IN2 = 0
    _________________________________________
   |       |                                 
   |     1 | Out1(+)   ________  Out2 (-)      3     
   +       |__________|  Motor |_____________      
   _                  |________|             |              
   |     2                                   | 4           
   |_________________________________________|
        
        Out1                             |  Out2 
     ----------------------------------------------------------------------------
        L_pin1 = IN1 && EN =  1 & 1 = 1  |   R_pin3 = IN2 && EN  = 0 & 1 = 0 
        L_pin2 = ~IN1 && EN = 0 & 1 = 0  |   R_pin4 = ~IN2 && EN = 1 & 1 = 1  
        

 ###########
 First Break Motor 
 
    Make EN = 1 , IN1 = 0,  IN2 = 0
    _________________________________________
   |                        Right             
   |     1    Out1 (-)  ________   Out2 (-)   
   +        ___________|  Motor |____________      
   _       |           |________|            |               
   |     2 |                                 |           
   |_______|_________________________________|
   
    
        
        Out1                             |   Out2 
     ----------------------------------------------------------------------------
        L_pin1 = IN1 && EN =  0 & 1 = 0  |   R_pin3 = IN2 && EN  = 0 & 1 = 0
    (-) L_pin2 = ~IN1 && EN = 1 & 1 = 1  |   R_pin4 = ~IN2 && EN = 1 & 1 = 1  (-)
        
 ###########
 Second Break Motor 
 
    Make EN = 1 , IN1 = 1,  IN2 = 1
    _________________________________________
   |       |                 Right           |  
   |     1 |  Out1 (+)  ________   Out2 (+)  | 
   +       | __________|  Motor |____________|      
   _                   |________|            |               
   |     2                                   |           
   |_________________________________________|
   
        
        Out1                             |   Out2
     ----------------------------------------------------------------------------
        L_pin1 = IN1 && EN =  1 & 1 = 1  |   R_pin3 = IN2 && EN  = 1 & 1 = 1
        L_pin2 = ~IN1 && EN = 0 & 1 = 0  |   R_pin4 = ~IN2 && EN = 0 & 1 = 0 
             
        
        
       
"""

