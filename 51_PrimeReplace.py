def isprime(n):
    for x in range(2, int(n**0.5) + 1):
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


def pf(n, v):
    c = 0
    for i in range(1, 10):
        m = int(str(n).replace(str(v), str(i)))
        if not isprime(m):
            c += 1
        if c > 1:
            return False
    return True


pg = gen_primes()
while True:
    p = pg.next()

    for i in range(3):
        if str(p).count(str(i)):
            if pf(p, i):
                print p
