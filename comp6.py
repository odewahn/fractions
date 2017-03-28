import matplotlib.pyplot as plt
import numpy as np

# new grayscale alg from Thomas Baruchel
def grayify(complexes):
    h = np.angle(complexes) / (np.pi/2.0)
    h = np.abs(np.abs(h)-1.0)
    return [ str(g) for g in h]

def cf(num, den, z, limit, n=1):
# this isn't quite right
    if den(n,z) == 0: return 1 # to eliminate div0 problems. maybe
    if n < limit : return den(n, z) + num(n+1, z)/cf(num,den,z,limit,n+1)
    if n == limit : return den(n+1,z) 
#    if n < limit: return den(n, z) + num(n+1, z)/cf(num,den,z,limit,n+1)
#    if n == limit: return num(n, z)/den(n, z)


points = 200  # number of points in each direction
scale = 2     # max value domain 
r = range(-points,points) 
domain =  [x*scale/points + 1j*y*scale/points for x in r for y in r ]
# calculates #181 from https://kettenreihen.wordpress.com/
# Probably not right, but result is a little evocative, at least
# values = [ cf(lambda n,z:z-n+1, lambda n,z:n*z,p,100) for p in domain]
# # 168 (closer)
values = [ cf(lambda n,z:1, lambda n,z:z-n+1,p,100) for p in domain]
# values = [ cf(lambda n,z:-z, lambda n,z:z**(-1/n),p,100) for p in domain]

grays = grayify(values)
plt.scatter(np.real(domain), np.imag(domain), s=1, color=grays)
plt.show()

print(cf(lambda a,b: 1, lambda a,b: 1, 0, 30)) # golden ratio
