import sqlite3
connection = sqlite3.connect("info.db")
cursor = connection.cursor()
cursor.execute("drop table student")
cursor.execute("create table Student(name,age)")
print("Enter 3 Details")
for i in range(1,4) :
    name = [input("Enter Name : ")]
    age = [int(input("Enter Age : "))]
    n = len(name)
    for i in range(n) :
        cursor.execute("insert into student values (?,?)",(name[i] , age[i]))
cursor.execute("select * from student order by age desc")
print(*cursor.fetchall() , sep='\n')
