import numpy as np

def sign(number):
    try:return number/abs(number)
    except ZeroDivisionError:return 0

file = open(r"C:\Users\Ehsan\Desktop\triangles.txt", 'r')

data = file.readlines()

count = 0

for line in data:
    t = line.strip('\n').split(',')
    t = map(int, t)
    
    p0 = [ 0   , 0   , 0 ]
    p1 = [ t[0], t[1], 0 ]
    p2 = [ t[2], t[3], 0 ]
    p3 = [ t[4], t[5], 0 ]

    l0 = np.subtract( p0, p1 )
    l1 = np.subtract( p2, p1 )
    l2 = np.subtract( p3, p1 )

    if sign(np.cross(l1,l0)[2]) == sign(np.cross(l1,l2)[2]):
        l0 = np.subtract( p0, p2 )
        l1 = np.subtract( p1, p2 )
        l2 = np.subtract( p3, p2 )

        if sign(np.cross(l1,l0)[2]) == sign(np.cross(l1,l2)[2]):
            l0 = np.subtract( p0, p3 )
            l1 = np.subtract( p1, p3 )
            l2 = np.subtract( p2, p3 )

            if sign(np.cross(l1,l0)[2]) == sign(np.cross(l1,l2)[2]):
                count+=1
print count
