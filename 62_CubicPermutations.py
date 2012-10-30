import networkx as nx
import time

def is_perm(n,m):
    n=str(n)
    m=str(m)
    return all(n.count(char) == m.count(char) for char in n) 

n=1
m=12
l = []

while len(str(n**3)) < m:
    n+=1

while len(str(n**3)) < m+1:
    l.append(n)
    n+=1

G = nx.Graph()
G.add_nodes_from(l)

for i in range(len(l)):
    if i%50 == 0: print time.time()
    for j in range(i+1,len(l)):
        if is_perm( l[i]**3, l[j]**3 ):
            G.add_edge( l[i], l[j] )
            break
            
nodes = nx.connected_component_subgraphs(G)[0].nodes()
print min(nodes)**3
