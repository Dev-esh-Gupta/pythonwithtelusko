import pymysql

mydb = pymysql.connect(host='127.0.0.1', user='root', password='dev37400', database='temp1')

mycursor = mydb.cursor()

# all the data from student will store in mycursor which we can print through for loop
mycursor.execute('select * from student')
# for i in mycursor:
#     print(i)

# following statement will fetch all the data from student table
# result = mycursor.fetchall()
# print(result)

# following expression will fetch one data form student table
result1 = mycursor.fetchone()

print(result1)



# for i in result:
#     print(i)

