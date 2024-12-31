a = 4
b = 2

try:
    print('Resource Open')
    print(a/b)
    k = int(input('Enter a number : '))
    print(k)
except ZeroDivisionError:
    print('Hey, You cannot divide a number by Zero')
except ValueError:
    print('Invalid Input')
except Exception as e:
    print(e)
finally:
    print('Resource Close')


print('Bye')
