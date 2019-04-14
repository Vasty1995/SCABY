import numpy as np
from array import *
# How to ready t.txt in python
# 

#4, -0.058, 0.559, 0.000
#6, 1.117, 0.000, 0.000
#5, 1.279, 0.489, 0.000
#3, 0.000, 0.000, 0.000

file = open("t.txt","r")

tempA = file.read(23)
tempB = file.read(23)
tempC = file.read(23)
tempD = file.read(23)

#temp = np.array([tempA, tempB, tempC, tempD])


#print(tempA[0])
#print(tempB[1])
#print(tempC)
#print(tempD)

#print(tempA[0])
#print(tempB[1])

#print(tempC[1])
#print(tempD[1])


# tempA
if tempA[0] == '4':
	beacon4 = tempA[0]
	print('beacon=',beacon4)
	B4X = []
	B4X = [tempA[3],tempA[4],tempA[5],tempA[6],tempA[7],tempA[8]]
	str4X = ''.join(B4X)
	print(str4X)
	
	B4Y = []
	B4Y = [tempA[10],tempA[11],tempA[12],tempA[13],tempA[14],tempA[15]]
	str4Y = ''.join(B4Y)
	print(str4Y)
	
elif tempA[0] == '5':
	beacon5 = tempB[0]
	print(beacon5)

elif tempA[0] == '6' :
	beacon6 = tempA[0]
	print(beacon6)
elif tempA[0] == '3' :
	beacon3 = tempA[0]
	print(beacon3)
#tempB	
if tempB[1] == '4' :
	beacon4 = tempB[1]
	print(beacon4)
	
elif tempB[1] == '5' :
	beacon5 = tempB[1]
	print(beacon5)
elif tempB[1] == '6' :
	beacon6 = tempB[1]
	print(beacon6)
elif tempB[1] == '3' :
	beacon3 = tempB[1]
	print(beacon3)

# tempC
if tempC[1] == '4' :
	beacon4 = tempC[1]
	print(beacon4)
elif tempC[1] == '5' :
	beacon5 = tempC[1]
	print(beacon5)
elif tempC[1] == '6' :
	beacon6 = tempC[1]
	print(beacon6)
elif tempC[1] == '3' :
	beacon3 = tempC[1]
	print(beacon3)
	
#tempD	
if tempD[1] == '4' :
	beacon4 = tempD[1]
	print(beacon4)
elif tempD[1] == '5' :
	beacon5 = tempD[1]
	print(beacon5)
elif tempD[1] == '6' :
	beacon6 = tempD[1]
	print(beacon6)
elif tempD[1] == '3' :
	beacon3 = tempD[1]
	print(beacon3)

