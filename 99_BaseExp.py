import math

f = open( r"C:/Users/Ehsan/Desktop/base_exp.txt",'r')

i = 1
m = 0

for l in f.readlines():
    n = l.strip('\n').split(',')
    res = math.log( float(n[0]) )* float(n[1])
    if res > m:
        m = res
        mi = i
    i+=1
