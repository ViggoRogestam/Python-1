import _mysql_connector

# Skapa en databasanslutning mot databasen
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    port="8889",
    user="root",
    password="root",
    database="employees_db"
)
mycursor = mydb.cursor()

# Create table:
# mycursor.execute("""CREATE TABLE employee_table (
#               id INT AUTO_INCREMENT PRIMARY KEY,
#               first_name TEXT(64),
#               last_name TEXT(64),
#               salary INTEGER(255))""")
# Insert into table:
sql = "INSERT INTO employee_table (first_name, last_name, salary) VALUES (%s, %s, %s)"
val = ("John", "Nilsson", 50000)
mycursor.execute(sql, val)
mydb.commit()

# Select from table:
"""

mycursor.execute("SELECT * FROM employees_table")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
"""
# Select with a filter:
"""
sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
"""

# Update table:
"""
sql = "UPDATE employees_table SET pay = %s WHERE pay = %s"
val = ("50000", "60000")

mycursor.execute(sql, val)

mydb.commit()
"""
# Delete from table:
"""
sql = "DELETE FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )

mycursor.execute(sql, adr)

mydb.commit()
"""

"""class Employee:
    def __init__(self, first, last, email):
        self.first = first
        self.last = last
        self.email = email

    def insert_employee(self):
        with open:
"""
