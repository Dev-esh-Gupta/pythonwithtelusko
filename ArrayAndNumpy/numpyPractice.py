from numpy import *


arr = array([2, 3, 4, 8.0])
print(arr)
print(arr.dtype)

arr = linspace(0, 15, 20) #start, stop(include), and part (by default it is 50 part)

print(arr)

arr = arange(1, 25, 2) #start, stop (exclude), gap

print(arr)

arr = logspace(1, 40, 5)

print(arr)

arr = zeros(5) # by default it is float
print(arr)

arr = ones(5, int) # by default it is float
print(arr)

