from libs.ent import primes
from operator import mul

def tot(n):
    res = n
    for i in range(2,int(n**0.5+1)):
        if not n%i: res -= res/i
        while not n%i: n /= i
    if n > 1: 
        res -= res/n
    return res

p = primes(100)
 
goal = 15499.0/94744
i = 1
d = 1
inc = reduce(mul,p[:d])
m = float("inf")

while True:
    test = tot(i+inc+1)/float(i+inc)
    if test < m:
        m = test
        i += inc
        if test < goal:
            break
    else:
        d += 1
        inc = reduce(mul,p[:d])

print i+1