from array import *

vals = array('i', [3, 4, 6, -5, 7])

print(vals.buffer_info())

vals.append(2)

print(vals)

vals.remove(-5)

print(vals)

print(vals[2])

for i in range(5):
    print(vals[i])

newArray = array(vals.typecode, (a*a for a in vals))

print(newArray)


