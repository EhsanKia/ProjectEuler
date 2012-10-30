import math
from fractions import Fraction as F

def isSquare(n):
    n = n**0.5
    return int(n)==n

def contF(n):
    m = [ 0 ]
    d = [ 1 ]
    a = [ int(n**0.5) ]
    i=0

    while True:
        yield a[-1]
        m.append( d[i]*a[i] - m[i] )
        d.append( (n - m[i+1]**2)/d[i] )
        a.append( int( (a[0]+m[i+1])/d[i+1] ) )
        i+=1

def makeF(l):
    if len(l)==1:
        return l[0]
    return l[0] + F( 1, makeF( l[1:] ) )
        

maxX=0

for D in range(2,1001):
    if isSquare(D): continue
    g = contF(D)
    l = []
    while True:
        l.append( g.next() )
        f = makeF(l)
        x = f.numerator
        y = f.denominator
        if x**2 - D*y**2 == 1:
            break
        x+=1
    if x > maxX:
        maxX = x
        maxD = D
