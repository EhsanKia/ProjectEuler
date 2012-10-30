import time

def f(n,l=0):
    if n==0:
        return 1

    i = 2**l
    if i > n:
        return 0

    if n >= 2*i:
        return f(n-2*i,l+1) + f(n-i,l+1) + f(n,l+1)

    return f(n-i,l+1) + f(n,l+1)

memo = {}
memo[0] = 0
memo[1] = 1
def f2(n):
    if not memo.has_key(n):
        if n%2==0:
            memo[n] = f2(n/2)
        else:
            memo[n] = f2( (n-1)/2 ) + f2( (n+1)/2 )
    return memo[n]

print f2(10**25 +1)
