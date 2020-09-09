import mysql.connector
conn = mysql.connector.connect(host='localhost', username='root', password='Sek_d_251298', port=3310, database='dispire')
cursor = conn.cursor()
# sql = "CREATE DATABASE DISPIRE"""CREATE TABLE student(name VARCHAR(255), age INT)""
# sql = "INSERT INTO student(name, age) VALUES (%s, %s)"
sql = "SELECT * FROM student"
cursor.execute(sql)
print(cursor.fetchall())
conn.commit()
conn.close()