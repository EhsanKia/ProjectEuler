from fractions import gcd, Fraction as F
from collections import deque
import time

q = [ (2,1) ]

s = set()
l=10000
c=0

s = time.time()
while len(q) > 0:
    v = q.pop()
    c+=1
    m1 = (2*v[0]-v[1],v[0])
    m2 = (2*v[0]+v[1],v[0])
    m3 = (v[0]+2*v[1],v[1])

    if m1[0]<=l: q.append( m1 )
    if m2[0]<=l: q.append( m2 )
    if m3[0]<=l: q.append( m3 )

print c
print time.time()-s

