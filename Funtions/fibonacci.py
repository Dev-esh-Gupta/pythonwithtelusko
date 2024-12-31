def fib(n):
    num1 = 0
    num2 = 1

    if n >= 1:
        print(num1, end=" ")
        if n >= 2:
            print(num2, end=" ")
            if n > 2:
                for i in range(n-2):
                    next_num = num1 + num2
                    print(next_num, end=" ")
                    num1 = num2
                    num2 = next_num


n = int(input("How many element you want of Fibonacci Series : "))
fib(n)
