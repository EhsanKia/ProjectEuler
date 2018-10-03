import collections
import itertools

peter = collections.defaultdict(int)
for roll in itertools.product(range(1, 5), repeat=9):
    peter[sum(roll)] += 1

colin = collections.defaultdict(int)
for roll in itertools.product(range(1, 7), repeat=6):
    colin[sum(roll)] += 1

peter_total = sum(peter.values())
colin_total = sum(colin.values())

peter_arr = [peter[i] / float(peter_total) for i in range(37)]
colin_arr = [colin[i] / float(colin_total) for i in range(37)]

peter_cum = [sum(peter_arr[i:]) for i in range(37)]

probability = 0
for i in range(36):
    probability += colin_arr[i] * peter_cum[i + 1]

print '%.7f' % probability
