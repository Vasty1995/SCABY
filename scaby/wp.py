"""
import numpy as np
import matplotlib.pyplot as plt
"""
		A [ ax[1], ay[1] ] = ( 2, 0) 	A =	(20, 0) 
		A [ ax[1], ay[1] ] = ( 2, 0) 		(18, 0)
		A [ ax[1], ay[1] ] = ( 2, 0) 		(20, 0) 
		A [ ax[1], ay[1] ] = ( 2, 0) A [ ax[1], ay[1] ] = ( 2, 0) 		(18, 0)
		A [ ax[1], ay[1] ] = ( 2, 0) 
		A [ ax[1], ay[1] ] = ( 2, 0) 		(20, 0) 
		A [ ax[1], ay[1] ] = ( 2, 0) 
		A [ ax[1], ay[1] ] = ( 8, 0) 	
		A [ ax[1], ay[1] ] = ( 6, 0) 
		A [ ax[2], ay[2] ] = ( 4, 0)
		A [ ax[1], ay[1] ] = ( 2, 0) 
	Start =	A [ ax[0], ay[0] ] = (20, 0)

"""




ax = np.array([0,0,0,0,0,0,0,0,0,0])
ay = np.arange([0,22,2])
A = np.array([ax, ay])

#start = [0, 0]
#finsih = [20,20]

while(not finished)
check if at starting poistion
mobile beacon Left
mobile beacon right 



Start: in Ideal setup where everything is right 
    
    0  | 0
  wp [ x | y ]
  Lb [ x | y ]
  Rb [ x | y ]

wp = [ 0 , 0 ]
Lb = [ 0 , 0 ]
Rb = [ 0 , 0 ]

if( wp[x] == (Lb[x] & Rb[x] )
    Scaby is @ starting positon 
    print("Start mow that ass")

else 
  Figure out where start is 
  

"""

"""
Sample route for a 1 by 4 feet map.
Let us assume a single bar " | " is 1ft
  | = 4 ft   => 1.00 Done 
  | = 3 ft   => 0.75 Done
  | = 2 ft   => 0.50 Done 
  | = 1 ft   => 0.25 Done
  | = 0 ft   => 0.00 Start 


0 | 4  ft => End of Route  
0 | 2  ft => Half Way 
0 | 0  ft => Start 

wp = [0 ,  0,  0,  2,  0,  4]
wp = [x0, y0, x1, y1, x2, y2]


wp[0] = 0  = x0
wp[1] = 0  = y0
wp[2] = 0  = x1
wp[3] = 2  = y1
wp[4] = 0  = x2
wp[5] = 4  = y2
"""
wp = [0 ,  0,  0,  2,  0,  4]
for i in range(len(wp):
  print(wp[i])
 
"""
Mobile Beacons = >  [ LB   |  RB  ]
                    [ x, y | x, y ]

LB = [0 ,  0,  0,  2,  0,  4]
RB = [x0, y0, x1, y1, x2, y2]
"""
