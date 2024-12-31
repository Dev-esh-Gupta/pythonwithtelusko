class A:
    def __init__(self):
        print('In A init')


class B(A):  # Single Level inheritance
    def __init__(self):
        print('In B init')
        super().__init__() # Calling the parent class constructor


class C:
    def __init__(self):
        print('In C init')


class D(A, C): # Work based on Method Resolution Order (MRO)
    def __init__(self):
        print('In D init')
        super().__init__()  # this call init of Class A


a1 = A()
b1 = B()
d1 = D()
