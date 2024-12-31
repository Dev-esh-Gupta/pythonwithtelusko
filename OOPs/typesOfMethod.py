# instance method (two type 1. Accessor, 2. Mutator)
# 1. Accessor (use to access the value) -> getter
# 2. Mutator (use to change value) -> setter
# class method
# static method

class Student:
    school = "Dev University"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    # Below method is called instance method
    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

    def get_m1(self):
        return self.m1

    def set_m1(self, value):
        self.m1 = value

    # Below method is class method
    @ classmethod # this is called decorator
    def getSchool(cls):
        print(cls.school)

    # Below method is static method
    @ staticmethod
    def info():
        print("This is Student class.. in this module")


s1 = Student(12,34,33)
s2 = Student(14,44,23)

print('S1 average : ', s1.avg())
print('S2 average : ', s2.avg())

Student.getSchool()
Student.info()
