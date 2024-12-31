from functools import reduce


def is_even(n):
    return n % 2 == 0


nums = [2, 4, 5, 7, 1, 12, 3, 5, 6, 9]

# Filter function will have two arguments (function, iterable)
evens = list(filter(is_even, nums))
even_lambda = list(filter(lambda n: n % 2 == 0, nums))

# Map function will have two arguments (function, iterable)
doubles = list(map(lambda n: n*2, nums))

# reduced to one value
sums = reduce(lambda a, b: a + b, doubles)

print(evens)
print('Even Lambda: ', even_lambda)
print('Doubles: ', doubles)
print('Sum of doubles: ', sums)
