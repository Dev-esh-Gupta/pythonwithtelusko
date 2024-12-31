class Car:
    # Class variable (static variable)
    wheels = 4

    def __init__(self):
        # These variables are called instance variable
        self.mil = 25
        self.com = "TATA"


c1 = Car()
c2 = Car()

c1.mil = 30  # instance namespace
Car.wheels = 8  # class namespace

print(c1.mil, c1.com, c1.wheels)
print(c2.mil, c2.com, c2.wheels)
