import mysql.connector

dbcon = mysql.connector.Connect(
    host="localhost", user="test", passwd="test", database="student"
)

cursor = dbcon.cursor()

cursor.execute("select * from students")

for i in cursor:
    print(i)
