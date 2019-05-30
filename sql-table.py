import mysql.connector

dbcon = mysql.connector.Connect(
    host="localhost", user="test", passwd="test", database="student"
)

cursor = dbcon.cursor()

cursor.execute("create table teachers (name VARCHAR(255), age INT)")

cursor.execute("show tables")

for table in cursor:
    print(table)
