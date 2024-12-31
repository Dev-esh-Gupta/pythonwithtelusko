def greet():
    print("Hello")

def add_sub(x, y):
    c = x + y
    d = x - y
    return c, d

greet()

result1 = add_sub(5, 4)
print(result1[0], result1[1])