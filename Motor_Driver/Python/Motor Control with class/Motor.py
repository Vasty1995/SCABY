class Drive:
    def _init_(self, pin1, pin2, pinEna):
        self.pin1 = pin1
        self.pin2 = pin2
        self.pinEna = pinEna


"""
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
   |     1 | Out1(+)   ________  Out2 (-)     3     
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
             
        
        
       
""""

    def forward(self):
        GPIO.output(self.pin1, 1)
        GPIO.output(self.pin2, 0)
        GPIO.output(self.pinEna, 1)





class Drive:
    def _init_(self, pin1, pin2, pinEna):
        self.pin1 = pin1
        self.pin2 = pin2
        self.pinEna = pinEna
            
    def forward(self):
        GPIO.output(self.pin1, 1)
        GPIO.output(self.pin2, 0)
        GPIO.output(self.pinEna, 1)
        
  #  def Reverse(self): 
        
       
