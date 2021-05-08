print(list(filter(lambda x: x % 2 == 0,range(50))))

a = [1,2,3]
b = a
b[0] = 4
print(b,a)

d = [1,2,3]
c = d[:]
c[0] = 4
print(c,d)

a = 'This is a interview'
print(min([(len(x),x) for x in a.split()])[1])

import numpy as np
a = np.array([1,10,21,3])
for x in range(len(a)):
    min = x
    for y in range(x+1,len(a)):
        if a[min] > a[y]:
            min = y
    a[min],a[x] = a[x] ,a[min]
print(a)


