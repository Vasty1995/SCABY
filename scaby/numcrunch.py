from marvelmind import MarvelmindHedge  # Marvelmind class, claculates Left and Right Beacon values
import sys
import math
import time
from time import sleep
import numpy

hedge = MarvelmindHedge()

class crunch():
    def __init__(self):
        self.lenLR = 0  # Holds the total length for the values being sent out from marvelmind 

        self.degree = [] # List to store angle values
        
        self.LB = []    # List to store both x & y
        self.LBx = []   # List to store x values only
        self.LBy = []   # List to store y values only
        self.lblen = 0  # Holds the list length from Left Beacon
        
        self.RB = []    # List to store both x & y
        self.RBx = []   # List to store x values only
        self.RBy = []   # List to store y values only
        self.rblen = 0  # Holds the list length from  Right Beacon
        
        self.wp = []     # Empty list to store waypoints
        self.wpx = []    # List to store waypoint x     
        self.wpy = []    # List to store waypoint y
        self.x = 0
        self.y = 0.25

        self.Im = []     # Empty List to store Imaginary point 
        self.Imx = []    # List to store Imaginary point x
        self.Imy = []    # List to store Imaginary point y

        self.Imd = []    # Imaginary Point Distance 
        self.Lbd = []    # Left Beacon Distance
        self.Rbd = []    # Right Beacon Distance

        self.zlb = []    # Left Beacon Ratio = Lbd / Imd
        self.zrb = []    # Right Beacon Ratio = Rbd / Imd
        self.zlr = []    # Array to hold = [ zlb, zrb ]
        
        self.dist= []    # Array to hold = [ Imd, Lbd, Rbd ]

    ####################################################################
    # Angle                                                            #
    ####################################################################
    def Angle(self):
        print("================")
        print(" Angle ")
        print("================")
        
        # Create a MarvelmindHedge thread
        hedge = MarvelmindHedge(tty = "/dev/ttyACM0", adr=2, debug=False) 
        hedge.start() # start thread
        sleep(1)

        self.degree = hedge.return_angle()
        
    ####################################################################
    # Left Beacon                                                      #
    ####################################################################
    def LBC(self):
        print("================")
        print(" Left Beacon ")
        print("================")
        
        # Create a MarvelmindHedge thread
        hedge = MarvelmindHedge(tty = "/dev/ttyACM0", adr=2, debug=False) 
        hedge.start() # start thread
        sleep(1)

        hedge.distances()
        #self.LBx = hedge.return_x()
        #self.LBy = hedge.return_y()
        
        #self.LBang = hedge.Angle()  # Angle Value of Left Beacon

        #self.LBx.hedge.print_position()  # Value of Left Beacon X
        #self.LBy.extend(hedge.Return_Y_position())  # Value of Left Beacon Y
	
	#self.LBx.extend(hedge.())
	#self.LBy.extend(hedge.print_distances())
        
        # Check to see every x has its pair y
        # The length or the amount of x & y values being sent out should be the same
        #if len(self.LBx) == len(self.LBy):
        #    self.lenLR = len(self.LBx)
        
       # for i in range(self.lenLR):
        #    print("(LBx",i,", LBy",i,")","= (",self.LBx[i],", ",self.LBy[i],")")
        
        #self.LB = [self.LBx, self.LBy, self.lenLR] # Create an array for Left Beacon values
       #return self.LBang
    
    #################################################################
    # Right Beacon                                                  #
    #################################################################
    def RBC(self):
        print("\n================")
        print(" Right Beacon ")
        print("================")
        
        # Create a MarvelmindHedge thread
        hedge = MarvelmindHedge(tty = "/dev/ttyACM0", adr=2, debug=False) 
        hedge.start() # start thread
        sleep(1)

        self.RBang = hedge.Angle()  # Angle Value of Right Beacon

      # self.RBx.extend(hedge.Return_X_position())  # Value of Left Beacon X
       # self.RBy.extend(hedge.Return_Y_position())  # Value of Left Beacon Y
        
        # Check to see every x has its pair y
        # The length or the amount of x & y values being sent out should be the same
        #if len(self.RBx) == len(self.RBy):
         #   self.lenLR = len(self.RBx)
        
       # for i in range(self.lenLR):
        #    print("(RBx",i,", RBy",i,")","= (",self.RBx[i],", ",self.RBy[i],")")
        
        #self.RB = [self.RBx, self.RBy, self.lenLR] # Create an array for Left Beacon values
        #return self.RBang
  
    #################################################################
    # WayPoint                                                      #
    #################################################################
    def Wayp(self):
        print("\n================")
        print("Way Points")
        print("================")
        
        for k in range(self.lenLR):
            self.wpx.insert(k,self.x)
            self.wpy.insert(k,self.y)
            self.y += 0.25
            print("(wpx",k,", wpy",k,")","= (",self.wpx[k],", ",self.wpy[k],")")
    
        self.wp = [self.wpx,self.wpy]
        return self.wp

    ###########################################################
    # Imaginary Point                                         #
    #   Imx = LBx + (RBx - LBx)/2                             #
    #   Imy = LBy + (RBy - LB)/2                              #
    ###########################################################
    
    def IMP(self):
        print("\n================")
        print(" Imaginary Point ")
        print("================")
        
        for l in range(self.lenLR):
            self.Imx.insert(l,self.LB[0][l] + ((self.RB[0][l]-self.LB[0][l])/2))
            self.Imy.insert(l,self.LB[1][l] + ((self.RB[1][l]-self.LB[1][l])/2))
            print("(Imx",l,", Imy",l,")","= (",self.Imx[l],", ",self.Imy[l],")")
        
        self.Im = [self.Imx, self.Imy]
        return self.Im

    ###########################################################
    # Distance                                                #
    ###########################################################
    
    def Dist(self):
        
    # This fucntion calculates the distance between Waypoint to
    # Imaginary point, Left Beacon, and Right Beacon
       
        
        for m in range(self.lenLR):
            print("\n================")
            print(" Distance  ")
            print("================")
            
            self.Imd.insert(m, round(math.sqrt( ( ( self.wp[0][m] - self.Im[0][m])**2 ) + ( ( self.wp[1][m] - self.Im[1][m] )**2 ) ), 4 ) ) 
            self.Lbd.insert(m, round(math.sqrt( ( ( self.wp[0][m] - self.LB[0][m] )**2 ) + ( (  self.wp[1][m] -  self.LB[1][m] )**2 ) ), 4 ) )
            self.Rbd.insert(m, round(math.sqrt( ( ( self.wp[0][m] - self.RB[0][m] )**2 ) + ( ( self.wp[1][m] -  self.RB[1][m] )**2) ), 4 ) )
            print("Imd ", m , " = " , self.Imd[m])
            print("Lbd ", m , " = " , self.Lbd[m])
            print("RBd ", m , " = " , self.Rbd[m])

            ###########################################################
            # Z ratio                                                 #
            ###########################################################
            print("\n================")
            print(" Z values ")
            print("================")
   
            self.zlb.insert(m, round((self.Lbd[m] /  self.Imd[m] ), 4))
            self.zrb.insert(m, round((self.Rbd[m] /  self.Imd[m] ), 4))
            print("Zlb ", m ," = " , self.zlb[m])
            print("Zrb ", m , " = " , self.zrb[m])
            
        self.zlr = [self.zlb, self.zrb]
        return self.zlr

    
   
    
        


