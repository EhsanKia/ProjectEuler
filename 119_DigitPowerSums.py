import math


def digit_sum(n):
    return n if n < 10 else n % 10 + digit_sum(n // 10)


# def trailing_zeros(n):
#     s = str(n)
#     return len(s) - len(s.rstrip('0'))


# i = 0
# ds = 1
# n = 10
# while i < 30:
#     if ds != 1:
#         power = int(round(math.log(n, ds)))
#         if pow(ds, power) == n:
#             i += 1
#             print i, n, ds, int(power)
#     ds += 1
#     n += 1
#     if n % 10 == 0:
#         zeros = trailing_zeros(n) if n % 100 == 0 else 1
#         ds -= 9 * zeros

results = []
for ds in range(1, 200):
    for p in range(15):
        n = pow(ds, p)
        if n < 10:
            continue
        if digit_sum(n) != ds:
            continue
        results.append((n, ds, p))

for i, (n, _, _) in enumerate(sorted(results), start=1):
    print i, n
