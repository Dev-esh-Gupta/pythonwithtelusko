class Computer:
    def config(self):
        print('i5, 16GB, 1TB')


comp1 = Computer()

comp1.config() # One way of calling
Computer.config(comp1) # Another way of calling

print(type(comp1))
