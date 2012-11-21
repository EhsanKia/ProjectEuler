from collections import Counter
from itertools   import combinations
from math        import sqrt, ceil

def is_square(n):
    return sqrt(n).is_integer()

def ncat(l):
    res = 0
    l.reverse()
    for i,n in enumerate(l):
        res += n * 10**i
    return res

def gen_squares(n):
    s = int(ceil(sqrt(10**(n-1))))
    e = int(ceil(sqrt(10**(n)))-1)
    return map(lambda x: x**2, range(s,e+1))

def matchFilter(word):
    def retFun(n):
        return len(set(word)) == len(set(str(n))) == len(set(zip(word,str(n))))
    return retFun

def mapping(word,num):
    str_num = str(num)
    d={}
    for i,c in enumerate(word):
        d[c] = int(str_num[i])
    return d

class Tree:
    def __init__(self):
        self.words = []
        self.children = {}

    def __repr__(self):
        return "Words:" + ', '.join(self.words)

def find(letters):
    frontier = [root]
    h = Counter(letters)
    for s in alphabet:
        newFrontier = []
        f = h[s]
        for node in frontier:
            for i in range(f+1):
                if node.children.has_key(i):
                    newFrontier.append(node.children[i])
        frontier = newFrontier
        
    ans = []
    for node in frontier:
        ans.extend(node.words)

    ans = filter(lambda x: len(x)==len(letters), ans)
    ans.remove(letters)
    
    return ans

alphabet =  "jqxzwkvfybhgmpudclotnraise"
root = Tree()

#Populate AnagramTree
with open(r"words.txt",'r') as f:
    data = f.readline()
    words = data.split(',')
    words = map(lambda x: x.strip('"').lower(), words)
    for word in words:
        h = Counter(word)
        curNode = root

        for s in alphabet:
            f = h[s]
            curNode = curNode.children.setdefault(f,Tree())

        curNode.words.append(word)

#Generate anagrams sets
anagrams = []
while words:
    w = words.pop()
    l = find(w)
    if l:
        for p in l:
            words.remove(p)
        l.append(w)
        anagrams.append(l)

squares = []
for a in anagrams:
    for p in combinations(a,2):
        s = filter(matchFilter(p[0]),gen_squares(len(p[0])))
        for r in s:
            m = mapping(p[0],r)
            n = ncat([m[c] for c in p[1]])
            if is_square(n) and len(p[0])==len(str(n))==len(str(r)):
                squares.append(max(r,n))

print max(squares)