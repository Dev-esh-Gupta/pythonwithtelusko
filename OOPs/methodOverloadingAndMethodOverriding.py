class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    # Method overloading is achieved by following way
    def sums(self, a=None, b=None, c=None):
        s = 0
        if a != None and b != None and c != None:
            s = a + b + c
        elif a != None and b != None:
            s = a + b
        elif a != None:
            s = a

        return s


s1 = Student(23, 45)

print(s1.sums(2, 3))
print(s1.sums(2, 3, 5))

print(s1.sums(2))
print(s1.sums())


class A:
    def show(self):
        print('in A Show')


class B(A):
    # def show(self):
    #     print('in B show')
    pass


a1 = A()
a1.show()

b1 = B()
# If B have show method it will print that show
# otherwise parent show method
b1.show()
