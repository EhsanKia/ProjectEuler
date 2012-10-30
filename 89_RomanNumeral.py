import re

val = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1,
       'CM':900, 'CD':400, 'XC':90, 'XL':40, 'IX':9, 'IV':4}

f = open(r"C:\Users\Ehsan\Desktop\roman.txt",'r')

rData = []

for line in f.readlines():
    rData.append( line.strip('\n') )

sumB = 0
sumA = 0

def readRom(n):
    if len(n)==0:
        return 0
    elif len(n)==1:
        return val[ n[0] ]
    elif val[ n[0] ] < val[ n[1] ]:
        return val[ n[1] ] - val[ n[0] ] + readRom( n[2:] )
    else:
        return val[ n[0] ] + readRom( n[1:] )

def createRom(n):
    s = ""
    for k in ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']:
        while n >= val[k]:
            n -= val[k]
            s += k
    return s

for n in rData:
    sumB += len(n)
    sumA += len( createRom( readRom(n) ) )
    #print n, createRom( readRom(n) )

print sumB, sumA, sumB-sumA
