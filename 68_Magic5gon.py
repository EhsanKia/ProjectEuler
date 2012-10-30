from itertools import permutations as perm


for p in perm( range(1,11) ):    
    if min(p[0],p[1],p[2],p[3],p[4])!=p[0]: continue
    v1 = p[0] + p[5] + p[6]
    v2 = p[1] + p[6] + p[7]
    if v1 == v2:
        v3 = p[2] + p[7] + p[8]
        if v1 == v3:
            v4 = p[3] + p[8] + p[9]
            if v1 == v4:
                v5 = p[4] + p[9] + p[5]
                if v1 == v5:
                    maxP = p

p = map(str, maxP)
print p[0]+p[5]+p[6]+p[1]+p[6]+p[7]+p[2]+p[7]+p[8]+p[3]+p[8]+p[9]+p[4]+p[9]+p[5]

