from math import factorial as fact
import time

v = {}

def chain(n):
    l = [n]
    while True:
        tot = 0
        for d in str(n):
            tot += fact(int(d))

        if v.has_key(tot):
            for j in range( len( l ) ):
                v[ l[j] ] = len(l)-j+v[tot]
            return len(l)+v[tot]
        if l.count(tot):
            for j in range( len( l ) ):
                v[ l[j] ] = len(l)-j
            return len(l)
        else:
            l.append(tot)
            n=tot

c=0
s = time.time()
for i in xrange(1000000):
    if v.has_key(i):
        m = v[i]
    else:
        m=chain(i)

    if m == 60:
        c+=1
print time.time()-s