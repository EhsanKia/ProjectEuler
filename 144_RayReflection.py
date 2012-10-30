from numpy import array
from numpy.linalg import norm
from decimal import *
import numpy as np
import time

getcontext().prec = 50

def get_t1( p, v):
    insqrt = -(p[0]**2 * v[1]**2) + 2*p[0]*p[1]*v[0]*v[1]
    insqrt += -(p[1]**2 * v[0]**2) + 100 * v[0]**2 + 25 * v[1]**2
    result = -2 * Decimal.sqrt( insqrt ) - 4 * p[0] * v[0] - p[1] * v[1]
    result /= 4 * v[0]**2 + v[1]**2
    return result

def get_t2( p, v):
    insqrt = -(p[0]**2 * v[1]**2) + 2*p[0]*p[1]*v[0]*v[1]
    insqrt += -(p[1]**2 * v[0]**2) + 100 * v[0]**2 + 25 * v[1]**2  
    result = 2 * Decimal.sqrt( insqrt ) - 4 * p[0] * v[0] - p[1] * v[1]
    result /= 4 * v[0]**2 + v[1]**2
    return result
    

s = array([ Decimal('0')  , Decimal('10.1') ])
d = array([ Decimal('1.4'), Decimal('-9.6') ])
v = d-s

count = 0
st = time.time()

for i in range(10000):
    d1 = s+v*get_t1( s, v)
    d2 = s+v*get_t2( s, v)
    
    if norm(d1-s) > norm(d2-s):
        s = d1
    else:
        s = d2

    n = array( [ 8*s[0], 2*s[1] ] )
    n /= norm(n)
    v = v - 2*np.dot(n,v)*n
    v /= norm(v)

    count += 1
    
    if s[0] < 0.01 and s[0] > -0.01 and s[1] > 0:
        print s, count

    if count%100==0:
        print time.time()-st
        st=time.time()
    
