nums = [2, 3, 5, 7, 1, 2, 5]

it = iter(nums)

print(it.__next__())
print(it.__next__())
print(it.__next__())
print(next(it), end="\n\n\n")


# My own iterator
class TopTen:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1

            return val
        else:
            raise StopIteration


values = TopTen()
print(values.__next__())
print(values.__next__())

for i in values:
    print(i)
