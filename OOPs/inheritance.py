class A:
    def feature1(self):
        print('Feature 1 working')

    def feature2(self):
        print('Feature 2 working')

class B(A): # Single Level inheritance
    def feature3(self):
        print('Feature 3 working')

    def feature4(self):
        print('Feature 4 working')

class D:
    def feature6(self):
        print('Feature 6 working')

class C(B, D): # Multiple inheritance and Multilevel (A->B->C)
    def feature5(self):
        print('Feature 5 working')


a1 = A()
b1 = B()
b1.feature1()
c1 = C()
c1.feature5()
c1.feature6()

