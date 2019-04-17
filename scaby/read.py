import numpy as np
from array import *
#4, -0.058, 0.559, 0.000
#6, 1.117, 0.000, 0.000
#5, 1.279, 0.489, 0.000
#3, 0.000, 0.000, 0.000

file = open("t.txt","r")

tempA = file.read(23)
tempB = file.read(23)
tempC = file.read(23)
tempD = file.read(23)

########################################################################
# tempA																   #
########################################################################
print(tempA)
if tempA[0] == '4':
	beacon4 = tempA[0]
	print("Beacon = ",beacon4)
	B4X = []
	B4X = [tempA[3],tempA[4],tempA[5],tempA[6],tempA[7],tempA[8]]
	str4X = ''.join(B4X)
	print("B4 X = ", str4X)
	
	B4Y = []
	B4Y = [tempA[10],tempA[11],tempA[12],tempA[13],tempA[14],tempA[15]]
	str4Y = ''.join(B4Y)
	print("B4 Y = ", str4Y)
	
elif tempA[0] == '5':
	beacon5 = tempA[0]
	print("Beacon = ",beacon5)
	B5X = []
	B5X = [tempA[3],tempA[4],tempA[5],tempA[6],tempA[7],tempA[8]]
	str5X = ''.join(B5X)
	print("B5 X = ", str5X)
	
	B5Y = []
	B5Y = [tempA[10],tempA[11],tempA[12],tempA[13],tempA[14],tempA[15]]
	str5Y = ''.join(B5Y)
	print("B5 Y = ", str5Y)

elif tempA[0] == '6' :
	beacon6 = tempA[0]
	print("Beacon = ",beacon6)
	B6X = []
	B6X = [tempA[3],tempA[4],tempA[5],tempA[6],tempA[7],tempA[8]]
	str6X = ''.join(B6X)
	print("B6 X = ", str6X)
	
	B6Y = []
	B6Y = [tempA[10],tempA[11],tempA[12],tempA[13],tempA[14],tempA[15]]
	str6Y = ''.join(B6Y)
	print("B6 Y = ", str6Y)
	
elif tempA[0] == '3' :
	beacon3 = tempA[0]
	print("Beacon = ",beacon3)
	B3X = []
	B3X = [tempA[3],tempA[4],tempA[5],tempA[6],tempA[7],tempA[8]]
	str3X = ''.join(B3X)
	print("B3 X = ", str3X)
	
	B3Y = []
	B3Y = [tempA[10],tempA[11],tempA[12],tempA[13],tempA[14],tempA[15]]
	str3Y = ''.join(B3Y)
	print("B3 Y = ", str3Y)

########################################################################
# tempB															   #
########################################################################
if tempB[1] == '4':
	beacon4 = tempB[1]
	print("Beacon = ",beacon4)
	B4X = []
	B4X = [tempB[4],tempB[5],tempB[6],tempB[7],tempB[8],tempB[9]]
	str4X = ''.join(B4X)
	print("B4 X = ", str4X)
	
	B4Y = []
	B4Y = [tempB[10],tempB[11],tempB[12],tempB[13],tempB[14],tempB[15]]
	str4Y = ''.join(B4Y)
	print("B4 Y = ", str4Y)
elif tempB[1] == '6' :
	beacon6 = tempB[1]
	print("Beacon = ",beacon6)
	B6X = []
	B6X = [tempB[4],tempB[5],tempB[6],tempB[7],tempB[8],tempB[9]]
	str6X = ''.join(B6X)
	print("B6 X = ", str6X)
	
	B6Y = []
	B6Y = [tempB[10],tempB[11],tempB[12],tempB[13],tempB[14],tempB[15]]
	str6Y = ''.join(B6Y)
	print("B6 Y = ", str6Y)
elif tempB[1] == '5':
	beacon5 = tempB[1]
	print("Beacon = ",beacon5)
	B5X = []
	B5X = [tempB[4],tempB[5],tempB[6],tempB[7],tempB[8],tempB[9]]
	str5X = ''.join(B5X)
	print("B5 X = ", str5X)
	
	B5Y = []
	B5Y = [tempB[10],tempB[11],tempB[12],tempB[13],tempB[14],tempB[15]]
	str5Y = ''.join(B5Y)
	print("B5 Y = ", str5Y)
		
elif tempB[1] == '3' :
	beacon3 = tempB[1]
	print("Beacon = ",beacon3)
	B3X = []
	B3X = [tempB[4],tempB[5],tempB[6],tempB[7],tempB[8],tempB[9]]
	str3X = ''.join(B3X)
	print("B3 X = ", str3X)
	
	B3Y = []
	B3Y = [tempB[10],tempB[11],tempB[12],tempB[13],tempB[14],tempB[15]]
	str3Y = ''.join(B3Y)
	print("B3 Y = ", str3Y)


########################################################################
# tempC															       #
########################################################################
if tempC[1] == '4':
	beacon4 = tempC[1]
	print("Beacon = ",beacon4)
	B4X = []
	B4X = [tempC[4],tempC[5],tempC[6],tempC[7],tempC[8],tempC[9]]
	str4X = ''.join(B4X)
	print("B4 X = ", str4X)
	
	B4Y = []
	B4Y = [tempC[10],tempC[11],tempC[12],tempC[13],tempC[14],tempC[15]]
	str4Y = ''.join(B4Y)
	print("B4 Y = ", str4Y)

elif tempC[1] == '5':
	beacon5 = tempC[1]
	print("Beacon = ",beacon5)
	B5X = []
	B5X = [tempC[4],tempC[5],tempC[6],tempC[7],tempC[8],tempC[9]]
	str5X = ''.join(B5X)
	print("B5 X = ", str5X)
	
	B5Y = []
	B5Y = [tempC[10],tempC[11],tempC[12],tempC[13],tempC[14],tempC[15]]
	str5Y = ''.join(B5Y)
	print("B5 Y = ", str5Y)

elif tempC[1] == '6' :
	beacon6 = tempC[1]
	print("Beacon = ",beacon6)
	B6X = []
	B6X = [tempC[4],tempC[5],tempC[6],tempC[7],tempC[8],tempC[9]]
	str6X = ''.join(B6X)
	print("B6 X = ", str6X)
	
	B6Y = []
	B6Y = [tempC[10],tempC[11],tempC[12],tempC[13],tempC[14],tempC[15]]
	str6Y = ''.join(B6Y)
	print("B6 Y = ", str6Y)
	
elif tempC[1] == '3' :
	beacon3 = tempC[1]
	print("Beacon = ",beacon3)
	B3X = []
	B3X =  [tempC[4],tempC[5],tempC[6],tempC[7],tempC[8],tempC[9]]
	str3X = ''.join(B3X)
	print("B3 X = ", str3X)
	
	B3Y = []
	B3Y = [tempC[10],tempC[11],tempC[12],tempC[13],tempC[14],tempC[15]]
	str3Y = ''.join(B3Y)
	print("B3 Y = ", str3Y)


########################################################################
# tempD															       #
########################################################################	
if tempD[1] == '4':
	beacon4 = tempD[1]
	print("Beacon = ",beacon4)
	B4X = []
	B4X = [tempD[4],tempD[5],tempD[6],tempD[7],tempD[8],tempD[9]]
	str4X = ''.join(B4X)
	print("B4 X = ", str4X)
	
	B4Y = []
	B4Y = [tempD[10],tempD[11],tempD[12],tempD[13],tempD[14],tempD[15]]
	str4Y = ''.join(B4Y)
	print("B4 Y = ", str4Y)
	
elif tempD[1] == '5':
	beacon5 = tempD[1]
	print("Beacon = ",beacon5)
	B5X = []
	B5X = [tempD[4],tempD[5],tempD[6],tempD[7],tempD[8],tempD[9]]
	str5X = ''.join(B5X)
	print("B5 X = ", str5X)
	
	B5Y = []
	B5Y = [tempD[10],tempD[11],tempD[12],tempD[13],tempD[14],tempD[15]]
	str5Y = ''.join(B5Y)
	print("B5 Y = ", str5Y)

elif tempD[1] == '6' :
	beacon6 = tempD[1]
	print("Beacon = ",beacon6)
	B6X = []
	B6X = [tempD[4],tempD[5],tempD[6],tempD[7],tempD[8],tempD[9]]
	str6X = ''.join(B6X)
	print("B6 X = ", str6X)
	
	B6Y = []
	B6Y = [tempD[10],tempD[11],tempD[12],tempD[13],tempD[14],tempD[15]]
	str6Y = ''.join(B6Y)
	print("B6 Y = ", str6Y)
	
elif tempD[1] == '3' :
	beacon3 = tempD[1]
	print("Beacon = ",beacon3)
	B3X = []
	B3X = [tempD[4],tempD[5],tempD[6],tempD[7],tempD[8],tempD[9]]
	str3X = ''.join(B3X)
	print("B3 X = ", str3X)
	
	B3Y = []
	B3Y = [tempD[10],tempD[11],tempD[12],tempD[13],tempD[14],tempD[15]]
	str3Y = ''.join(B3Y)
	print("B3 Y = ", str3Y)

