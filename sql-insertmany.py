import mysql.connector

dbcon = mysql.connector.Connect(
    host="localhost", user="test", passwd="test", database="student"
)

cursor = dbcon.cursor()

sql = "insert into student (Name, Age) VALUES (%s, %s)"
vals = [
    ("Arjun", "18"),
    ("Ram", "16"),
    ("Sanju", "15")
]

cursor.executemany(sql, vals)

dbcon.commit()

print("New records added successfully")
