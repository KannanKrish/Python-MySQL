import mysql.connector

dbcon = mysql.connector.Connect(
    host="localhost", user="test", passwd="test", database="student"
)

print(dbcon)
