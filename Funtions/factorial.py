def factorial(num):
    if num < 0:
        return "Invalid Input"
    elif num == 0:
        return 1
    ans = 1
    for i in range(1, num+1):
        ans *= i

    return ans


result = factorial(6)
print(result)