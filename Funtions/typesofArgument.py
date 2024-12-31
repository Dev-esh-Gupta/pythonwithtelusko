def person(name, age):
    print(name)
    print(age)


person('Devesh', 26)  # Positioned argument
person(age=11, name='Gupta')  # Keyword argument


def person2(name, age=18):  # default value if argument not correspond that not passed
    print(name)
    print(age)


person2('Hary')


def sum(a, *b):  # variable length argument
    # c = a + b
    c = a
    print(a)
    print(b)
    for i in b:
        c += i
    print(c)


sum(4, 5, 11, 4, 6)


def human(name, **data): # variable length keyword argument
    print(name)
    print(data)

    for i, j  in data.items():
        print(i, j)

human('Devesh', age=26, city='Lucknow', mob=123456789)