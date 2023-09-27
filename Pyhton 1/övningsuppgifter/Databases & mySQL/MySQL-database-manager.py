import mysql.connector

# Connect to the employees_db
conn = mysql.connector.connect(
    host="localhost",
    port="8889",
    user="root",
    password="root",
    database="employees_db"
)


class Employee:
    def __init__(self, first: str, last: str, salary: int):
        """
        Enter Employee Information
        :param first: First Name
        :param last: Surname
        :param salary: Salary
        """
        self.first = first
        self.last = last
        self.salary = salary

    def insert_to_table(self):
        cursor = conn.cursor()
        sql = "INSERT INTO employee_table (first_name, last_name, salary) VALUES (%s, %s, %s)"
        val = (self.first, self.last, self.salary)
        cursor.execute(sql, val)
        conn.commit()
        cursor.close()

    def select_from_table(self):
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM employee_table")
        result = cursor.fetchall()
        cursor.close()
        return result

    def update_salary(self, new_salary: int):
        cursor = conn.cursor()
        sql = "UPDATE employee_table SET salary = %s WHERE first_name = %s AND last_name = %s"
        val = (new_salary, self.first, self.last)
        cursor.execute(sql, val)
        conn.commit()
        cursor.close()


em1 = Employee("Viggo", "Rogestam", 50000)
em1.insert_to_table()  # Inserting employee information to the database
print(em1.select_from_table())  # Fetching and printing all records from the database
em1.update_salary(60000)  # Updating salary for the employee
print(em1.select_from_table())  # Fetching and printing all records from the database again

# Don't forget to close the connection!
conn.close()
