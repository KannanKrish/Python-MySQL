import mysql.connector

dbcon = mysql.connector.Connect(
    host="localhost", user="test", passwd="test"
)

cursor = dbcon.cursor()

cursor.execute("create database test")

cursor.execute("show databases")

for database in cursor:
    print(database)
