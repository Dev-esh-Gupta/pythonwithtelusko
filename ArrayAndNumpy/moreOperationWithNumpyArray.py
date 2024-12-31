from numpy import *

arr = array([1,2,3,4,5])

arr = arr + 5

print(arr)

arr2 = array([3,4,5,6,7])

arr3 = arr + arr2

print(arr3)

print(sin(arr))
print(cos(arr))
print(log(arr))
print(sqrt(arr))
print(sum(arr))
print(min(arr))
print(max(arr))

print(concatenate([arr, arr2]))


# Shallow copy
arr3 = array([2,4,5,7,9])

arr4 = arr3

arr3[2] = 7

print(arr3)
print(arr4)

print(id(arr3))
print(id(arr4))

# Deep Copy
arr4 = arr3.copy()

arr3[1] = 15

print(arr3)
print(arr4)

print(id(arr3))
print(id(arr4))

