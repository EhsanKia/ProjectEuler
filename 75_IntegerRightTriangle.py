from collections import deque

LIMIT = 1500000
d = deque([(2,1),(3,1)])
triples = []

# Generates all unique triplets
while d:
    m, n = d.popleft()

    if (m-n)%2==0:
        continue

    s = 2 * m * (m+n)

    if (s <= LIMIT):
        triples.append(s)
        b1 = (2*m-n,m)
        b2 = (2*m+n,m)
        b3 = (m+2*n,n)
        d.extend([b1,b2,b3])

results = [0] * (LIMIT+1)

# Checks all multiples of the triples less than the limit
for t in triples:
    for i in range(t, LIMIT+1, t):
        results[i] += 1

# Sums only length that have one way
print results.count(1)