# python script for select values from mysql table and save it to excel file
import mysql.connector
from xlwt import Workbook
from mysql.connector import Error

try:
    MySQLconnect = mysql.connector.connect(host='127.0.0.1', user='root', password='', database='e-attendance_system')

    if MySQLconnect.is_connected():
        print("\nConnected Successfully To mysql database")

        MySQLcursor = MySQLconnect.cursor()

        MySQLcursor.execute("SELECT * FROM admin;")

        columnName = MySQLcursor.column_names

        tableValues = MySQLcursor.fetchall()

        print("\nData retrived successfully from mysql database")

        workBook = Workbook()

        workSheet = workBook.add_sheet("Sheet No 1")

        for i in range(len(columnName)):
            workSheet.write(0, i, columnName[i])

        for r, row in enumerate(tableValues):
            for c, col in enumerate(row):
                workSheet.write(r + 1, c, col)

        workBook.save("D:\\books\\me\\Python\\python_scripts\\Excel-MySQL.xls")

        print("\nData Written Successfully to excel file")

except Error as e:
    print("\nERROR", e)

finally:
    if(MySQLconnect.is_connected()):
        MySQLcursor.close()
        MySQLconnect.close()
        print("\nMysql connection closed")