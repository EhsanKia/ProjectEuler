import math

m = 3
n = 2

def tot(m,n):
    s=0
    for i in range(m):
        for j in range(n):
            s += (m-i)*(n-j)
    return s

m = float('inf')

for i in range(100):
    for j in range(i):
        n = tot(i,j)
        if n > 2E6+m: break
        if math.fabs(2E6-n) < m:
            m = math.fabs(2E6-n)
            best = [i,j]
        
