# i = 1
#
# while i <= 4:
#     j = 1
#     while j <= 4:
#         print('#', end=" ")
#         j += 1
#
#     print()
#     i += 1


# for i in range(4, 0, -1):
#     for j in range(1, i+1):
#         print(j, end=" ")
#
#     print()

# l1 = ['A', 'B', 'C', 'D']
# l2 = ['P', 'Q', 'R']
#
# for i in range(4):
#     for j in range(i+1):
#         print(l1[j], end=" ")
#     for j in range(i, 3):
#         print(l2[j], end=" ")
#     print()

# Prime or not

num = int(input("Enter Number to check for prime : "))

if num <= 1:
    print(f"{num} is not prime!")
elif num == 2:
    print(f"{num} is a prime!")
else:
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} is not a prime!")
            break

    else:
        print(f"{num} is prime")
