from collections import Counter
f = open( r"C:\Users\Ehsan\Desktop\poker.txt",'r')

cOrder = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']

def getT(h):
    return ''.join(h)[1::2]
def getV(h):
    v = ''.join(h)[::2]
    return sorted( map(lambda x: cOrder.index(x), list( v )) )

def rf(h):
    if getT(h).count( getT(h)[0] ) != 5:
        return -1
    if getV(h) != range(8,13):
        return -1
    return 1

def sf(h):
    if getT(h).count( getT(h)[0] ) != 5:
        return -1
    v = getV(h)
    if v != range(min(v),min(v)+5):
        return -1
    return max( v )

def fk(h):
    v = Counter( getV(h) )
    if v.most_common()[0][1] == 4:
        return v.most_common()[0][0]
    return -1

def fh(h):
    v = Counter( getV(h) )
    if v.most_common()[0][1] == 3 and v.most_common()[1][1] == 2:
        return v.most_common()[0][0]
    return -1

def fl(h):
    if getT(h).count( getT(h)[0] ) != 5:
        return -1
    return max( getV(h) )

def st(h):
    v = getV(h)
    if v != range(min(v),min(v)+5):
        return -1
    return max( v )

def tk(h):
    v = Counter( getV(h) )
    if v.most_common()[0][1] == 3:
        return v.most_common()[0][0]
    return -1

def tp(h):
    v = Counter( getV(h) )
    if v.most_common()[0][1] == 2 and v.most_common()[1][1] == 2:
        return max( v.most_common()[0][0], v.most_common()[1][0] )
    return -1

def op(h):
    v = Counter( getV(h) )
    if v.most_common()[0][1] == 2:
        return v.most_common()[0][0]
    return -1

def poker(h1,h2):
    if rf(h1) != rf(h2):
        return rf(h1)>rf(h2)
    if sf(h1) != sf(h2):
        return sf(h1)>sf(h2)
    if fk(h1) != fk(h2):
        return fk(h1)>fk(h2)
    if fh(h1) != fh(h2):
        return fh(h1)>fh(h2)
    if fl(h1) != fl(h2):
        return fl(h1)>fl(h2)
    if st(h1) != st(h2):
        return st(h1)>st(h2)
    if tk(h1) != tk(h2):
        return tk(h1)>tk(h2)
    if tp(h1) != tp(h2):
        return tp(h1)>tp(h2)
    if op(h1) != op(h2):
        return op(h1)>op(h2)
    return max(getV(h1))>max(getV(h2))

win=0
for line in f.readlines():
    cards = line.strip('\n').split(' ')
    h1 = cards[:5]
    h2 = cards[5:]
    if poker(h1,h2):
        win+=1

print win
