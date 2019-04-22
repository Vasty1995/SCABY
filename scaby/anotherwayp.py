import numpy as np 

def sample_Route():
  print("   __   
          |    |
          |    |
          |    | 
          |    |
          |    |    |
          |    |    |
          |    |    |pri
          |    |    | 
          |    |  __ 
          |")

  sample_Route()

def wp1():
  ax = np.full((1,10),0)
  ax = np.reshape(ax,(10,1))
  print(ax)

  ay = np.arange(0,22,2)
  ay = np.reshape(ay,(11,1))
  print(ay)

  A = np.array([[ax], [ay]])
  print(A)

  A = np.reshape(A,(21,2))
  print(A)
#Az = np.reshape(A,(10,2))
#print(Az)

"""
bx = np.full((1,10),2)
by = np.arange(0,22,2)
B = np.array([bx, by])
print(B) 

cx = np.full((1,10),4)
cy = np.arange(0,22,2)
C = np.array([cx, cy])
print(C)

dx = np.full((1,10),6)
dy = np.arange(0,22,2)
D = np.array([dx, dy])
D = np.reshape(D, (10,2))
print(D)

ex = np.full((1,10),8)
ey = np.arange(0,22,2)
E = np.array([ex, ey])
print(E)

fx = np.full((1,10),10)
fy = np.arange(0,22,2)
F = np.array([fx, fy])
print(F) 

gx = np.full((1,10),12)
gy = np.arange(0,22,2)
G = np.array([gx, gy])
print(G)

hx = np.full((1,10),14)
hy = np.arange(0,22,2)
H = np.array([hx, hy])
print(H)

ix = np.full((1,10),16)
iy = np.arange(0,22,2)
I = np.array([ix, iy])
print(I)

jx = np.full((1,10),18)
jy = np.arange(0,22,2)
J = np.array([jx, jy])
print(J) 

kx = np.full((1,10),20)
ky = np.arange(0,22,2)
K = np.array([kx, ky])
print(K)


"""


