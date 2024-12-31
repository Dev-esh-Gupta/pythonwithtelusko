class Computer:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram
        print("In Init")

    def config(self):
        print("Computer have CPU : ", self.cpu)
        print("Computer have RAM : ", self.ram)


obj = Computer("i5", "16GB")
obj1 = Computer("ryzen 5", "32GB")


obj.config()
obj1.config()
