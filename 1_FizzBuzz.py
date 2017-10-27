total = 0

for x in range (1, 1000):
    if x % 3 == 0:
        total += x
    if x % 5 == 0:
        total += x
    if x % 3 == 0 and x % 5 == 0:
        total -= x
    
print(total)
