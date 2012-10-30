import networkx as nx
import time

def poly(t):
    n = 1
    while True:
        if t == 3: yield n*(n+1)/2
        elif t == 4: yield n**2
        elif t == 5: yield n*(3*n-1)/2
        elif t == 6: yield n*(2*n-1)
        elif t == 7: yield n*(5*n-3)/2
        elif t == 8: yield n*(3*n-2)
        else: yield 0
        n += 1

G = nx.DiGraph()
l = []
s = time.time()

for i in range(6):
    tmp = 0
    g = poly(i+3)
    l.append( [] )
    while tmp < 1000:
        tmp = g.next()

    while tmp < 10000:
        l[i].append( tmp )
        if not G.has_node(tmp):
            G.add_node(tmp,t=[i])
        else:
            d = G.node[tmp]['t']
            d.append(i)
            G.add_node(tmp,t=d)            
        tmp = g.next()

for n in G.nodes(1):
    for m in G.nodes(1):
        if n[0]%100 == m[0]/100:
            if n[1]['t'] != m[1]['t'] or len(n[1]['t'])>1:
                G.add_edge(n[0],m[0])
        
size = 0

while size != len(G.nodes()):
    size = len(G.nodes())
    for n in G.nodes():
        if not G.in_degree(n) or not G.out_degree(n):
            G.remove_node(n)

print size, len(G.edges())
print time.time()-s

for i in range( len(l) ):
    for v in list(l[i]):
        if not G.has_node(v):
            l[i].remove(v)

res = []

for v in l[-1]:
    for n in G.nodes():
        if G.node[n]['t'] != [5]:
            if nx.shortest_path_length(G,v,n) == 3:
                if nx.shortest_path_length(G,n,v) == 3:
                    res.append( [v,n] )

def flow(n):
    Gs = nx.Graph()
    for v in n:
        Gs.add_edge('a',v,capacity=1)
        sets = G.node[v]['t']
        for s in sets:
            Gs.add_edge(v,s,capacity=1)
    for i in range(6):
        Gs.add_edge('b',i,capacity=1)
    return sum(nx.ford_fulkerson_flow(Gs,'a','b')['a'].values())
    

for r in res:
    p1 = nx.shortest_path(G, r[0], r[1])
    p2 = nx.shortest_path(G, r[1], r[0])
    ans = set(p1+p2)
    if len( ans ) == 6:
        if flow(ans) == 6:
            print ans
            print sum(ans)
        
