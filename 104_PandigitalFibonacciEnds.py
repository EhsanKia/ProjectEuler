import math

k = 2
f0, f1 = 1, 1
while True:
    k += 1
    f0, f1 = f1, f0 + f1

    end = set(str(f1 % 10**9))
    if len(end) < 9 or '0' in end:
        continue
    start = set(str(f1 / 10**(int(math.log10(f1)) - 8)))
    if len(start) < 9 or '0' in start:
        continue
    print k
    break
