
def count(lst):
    even = 0
    odd = 0
    for val in lst:
        if val % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


lst = [20, 11, 14, 5, 67, 12, 98, 40, 234]

even, odd = count(lst)

print(even, odd)

print("Even : {} and Odd : {}".format(even, odd))
