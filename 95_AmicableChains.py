import collections

LIMIT = 1000000


def divisors(n):
    yield 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            yield i
            yield n // i


amicable_map = collections.defaultdict(int)
for i in range(1, LIMIT):
    amicable_map[i] = sum(divisors(i))

max_len = 0
all_seen = set([1])
for i in range(1, LIMIT):
    if i in all_seen:
        continue

    j = i
    seq = []
    seen = set()
    while True:
        seq.append(j)
        seen.add(j)
        j = amicable_map[j]
        if j in seen:
            seq = seq[seq.index(j):]
            break

    if j in all_seen:
        continue
    if max(seq) > LIMIT:
        continue

    all_seen.update(seq)
    if len(seq) > max_len:
        max_len = len(seq)
        print max_len, min(seq)
