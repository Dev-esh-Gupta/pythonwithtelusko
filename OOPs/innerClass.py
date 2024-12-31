class Student:
    def __init__(self, name, rollNo):
        self.name = name
        self.rollNo = rollNo
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.rollNo)
        self.lap.show()

    # Below-mentioned Laptop class is inner class
    class Laptop:
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8

        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = Student('Devesh', 1)
s2 = Student('Seema', 2)
s1.show()
print(s1.lap.brand)

lap1 = s1.lap
lap2 = s2.lap
print(lap1.cpu)

# Directly creating object of Laptop Inner class
lap3 = Student.Laptop()
lap3.show()
