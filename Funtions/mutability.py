def update(x):
    print(id(x))  # shame address as passed variable
    x = 8  # at time of update address will be change
    print(id(x))
    print(x)


x = 10  # variables are immutable
print(id(x))
update(x)
print(x, end="\n\n")


def update_list(lst):
    print(id(lst))
    lst[1] = 15
    print(id(lst))
    print(lst)


lst = [1, 23, 45]  # lists are mutable
print(id(lst))
update_list(lst)
print(lst)
