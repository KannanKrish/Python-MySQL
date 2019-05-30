import mysql.connector

dbcon = mysql.connector.Connect(
    host="localhost", user="test", passwd="test", database="student"
)

cursor = dbcon.cursor()

sql = "insert into student (Name, Age) VALUES (%s, %s)"
val = ("Arjun", "18")

cursor.execute(sql, val)

dbcon.commit()

print("New record added successfully")
