class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):  # overloaded inbuilt add
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)
        return s3

    def __gt__(self, other):  # gt -> Greater than
        score1 = self.m1 + self.m2
        score2 = other.m1 + other.m2
        return score1 > score2

    def __str__(self):  # overloaded inbuilt str
        return (f'{self.m1}, {self.m2}')


s1 = Student(23, 34)
s2 = Student(11, 17)

s3 = s1 + s2

print(s3.m1, s3.m2)
if s1 > s2:
    print('S1 wins')
else:
    print('S2 wins')

a = 6
print(a)
print(s1)
