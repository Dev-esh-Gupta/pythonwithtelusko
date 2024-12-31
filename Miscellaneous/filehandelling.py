f = open('myData', 'r')

# print(f.readline(), end='')
# print(f.readline(), end='')

f1 = open('abc', 'w')

# f1.write('People')

f2 = open('file1', 'a')

f2.write('We Need somthing extra')

for data in f:
    f1.write(data)

f3 = open('biodata.jpg', 'rb')
f4 = open('myPic.jpg', 'wb')

# print(f3.read())

for data in f3:
    f4.write(data)
