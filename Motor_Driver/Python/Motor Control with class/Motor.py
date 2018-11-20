class Motor:
    def _init_(self, R_Ena, L_Ena, In1, In2, In3, In4) :
        self.R_Ena = R_Ena
        self.L_Ena = L_Ena
        self.In1 = In1
        self.In2 = In2
        self.In3 = In3
        self.In4 = In4
        # whats next ?
   
    def setup_pins(setup):
        GPIO.setup(setup.R_Ena, GPIO.OUT)
        GPIO.setup(setup.L_Ena, GPIO.OUT)
        GPIO.setup(setup.In1, GPIO.OUT)
        GPIO.setup(setup.In2, GPIO.OUT)
        GPIO.setup(setup.In3, GPIO.OUT)
        GPIO.setup(setup.In4, GPIO.OUT)
    
   
        
