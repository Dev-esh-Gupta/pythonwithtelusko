import sys

sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())

def greet():
    print("Hello")
    greet()

# greet()