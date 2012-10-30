import time

def isRep( l, n=1 ):
    if n*10 > len(l):
        return 0

    for i in range(n,n*10):
        if l[i%n] != l[i]:
            break
        elif i==(n*10)-1:
            return n
    return 0 + isRep(l,n+1)

l = []
s = time.time()

for n in range(2,10001):
    if n%500==0:
        print time.time()-s
        s = time.time()
        
    if int(n**0.5) != n**0.5:
        m = [ 0 ]
        d = [ 1 ]
        a = [ int(n**0.5) ]
        i=0

        while True:
            m.append( d[i]*a[i] - m[i] )
            d.append( (n - m[i+1]**2)/d[i] )
            a.append( int( (a[0]+m[i+1])/d[i+1] ) )
            i+=1
            if i > 300 and i%10 ==0 and isRep( a[1:] ) > 0:
                l.append( isRep( a[1:] ) )
                break

print "Average: ", sum(l)/len(l)
print "# of Odd: ", sum( map( lambda x: x%2, l ) )
raw_input("Press any key to exit")
