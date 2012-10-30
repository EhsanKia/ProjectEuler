import networkx as nx
import time

def isprime(n):
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True

def gen_primes():
    D = {}  
    q = 2  
    while True:
        if q not in D:
            yield q        
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1

G = nx.Graph()
pgen = gen_primes()
l = [ pgen.next() ]
s = time.time()

while True:
    a = pgen.next()

    if len(l)%50==0:
        mc = nx.graph_clique_number(G)
        print time.time()-s
        s = time.time()
        if mc == 5:
            break

    for b in l:
        if isprime( int( str(b)+str(a) ) ):
            if isprime( int( str(a)+str(b) ) ):
                G.add_edge(a,b)

    l.append(a)

cliques = list( nx.find_cliques(G) )
for c in cliques:
    if len(c) == 5:
        print c, sum(c)
        
print time.time()-s
