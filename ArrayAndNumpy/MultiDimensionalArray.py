from numpy import *

arr1 = array([
    [1,2,3,4,5,9],
    [4,5,6,12,4,11]
])

print(arr1.dtype)
print(arr1.ndim)
print(arr1.shape)
print(arr1.size)
print(arr1)

# from multi dimensional to 1 D
arr2 = arr1.flatten()
print(arr2)

# from multidimensional to 2D and 3D
arr3 = arr2.reshape(3,4)
print(arr3)

arr3 = arr2.reshape(2,2,3)
print(arr3)


m = matrix(arr1)

print(m)

m = matrix('1 2 3 ; 2 3 6 ; 1 2 3')
print(m)

print(diagonal(m))
print(m.max())

m2 = matrix('1 8 0 ; 2 7 6 ; 7 11 3')

m3 = m * m2 # This is matrix multiplication

print(m3)