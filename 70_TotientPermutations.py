def is_perm(n,m):
    n=str(n)
    m=str(m)
    return all(n.count(char) == m.count(char) for char in n) 

def tot(n):
    res = n
    for i in range(2,int(n**0.5+1)):
        if not n%i: res -= res/i
        while not n%i: n /= i
    if n > 1: 
        res -= res/n
    return res

m = float('inf')
for i in xrange(2,int(1E7)):
    t = tot(i)
    if float(i)/t < m and is_perm(i,t):
        m = float(i)/t
        res = i

print res

