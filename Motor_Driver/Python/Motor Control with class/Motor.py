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
        
       
