RATIO = 2 + 3**0.5

b = 1
total = 0

while True:
    a = int(b * RATIO) + 2
    perimeter = 3 * a + 1
    if perimeter > 10**9:
        break
    print a, a + 1
    total += perimeter

    b = int(a * RATIO) - 1
    perimeter = 3 * b - 1
    if perimeter > 10**9:
        break
    print b, b - 1
    total += perimeter

print total

# def digit_sum(n):
#     value = n if n < 10 else n % 10 + digit_sum(n // 10)
#     return value if value < 10 else digit_sum(value)


# def is_square(n):
#     if n % 10 not in {0, 1, 4, 5, 6, 9}:
#         return False
#     # if digit_sum(n) not in {1, 4, 7, 9}:
#     #     return False

#     x, y = n, (n + 1) // 2
#     while y < x:
#         x, y = y, (y + n // y) // 2
#     return x ** 2 == n


# total = 0
# for i in range(2, 10**9 / 3):
#     a, b = i, i + 1
#     a2, b2 = a**2, b**2

#     area1 = b2 * (4 * a2 - b2)
#     # Check triangle (a, a, b)
#     if area1 % 16 == 0 and is_square(area1):
#         total += 2 * a + b
#         print 1, a, b

#     # Check triangle (b, b, a)
#     area2 = a2 * (4 * b2 - a2)
#     if area2 % 16 == 0 and is_square(area2):
#         total += 2 * b + a
#         print 2, b, a

# print total
