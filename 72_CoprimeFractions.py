maxD = 1000000

def tot(n):
    res = n
    for i in range(2,int(n**0.5+1)):
        if not n%i: res -= res/i
        while not n%i: n /= i
    if n > 1: 
        res -= res/n
    return res

print sum(map(tot,range(2,maxD+1)))