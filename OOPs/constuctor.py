class Computer:
    def __init__(self):
        self.name = "Devesh"
        self.age = 26

    def update(self):
        self.age = 30

    def compare(self, c2):
        if self.age == c2.age:
            return True
        else:
            return False


c1 = Computer()
c2 = Computer()

if c1.compare(c2):
    print("Both are same")

c2.name = "Seema"
c2.age = 24

c1.update()


print(c1.name, c1.age)
print(c2.name, c2.age)