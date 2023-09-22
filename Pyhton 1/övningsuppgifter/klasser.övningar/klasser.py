import datetime
import math

"""
# Skapa klassen person innehållande namn, ålder och adress
class Person:
    def __init__(self, name: str, age: int, address: str):
        self.name = name
        self.age = age
        self.address = address

    # skapa en metod som printar ut information om personen.
    def print_person(self):
        print(f'Personen är {self.age} år gammal och heter {self.name}. Hen bor på på addressen {self.address}')


p1 = Person("Viggo", 20, "Larsbersvägen")
p1.print_person()


# Klass som är en cirkel med attributet för radie
class Cirkel:
    import math

    def __init__(self, radie: float):
        self.radie = radie

    def omkrets(self):
        return self.radie * 2 * math.pi


# Klass som är bankkonto där det finns attribut för saldo och kontonummer
class Bank_account:
    def __init__(self, account_num: int, balance: float):
        self.account_num = account_num
        self.balance = balance

    def get_Balance(self):
        password = int(input('Enter Account Number >'))
        if password == self.account_num:
            return self.balance
        else:
            print('Wrong account number')

    def inc_balance(self, amount: float):
        password = int(input('Enter Account Number >'))
        if password == self.account_num:
            self.balance += amount
        else:
            print('Wrong account number')

    def withdraw_balance(self, amount: float):
        password = int(input('Enter Account Number >'))
        if password == self.account_num:
            self.balance -= amount
        else:
            print('Wrong account number')

    def print_balance(self):
        password = int(input('Enter Account Number >'))
        if password == self.account_num:
            print(f'Account Balance: {self.balance} kr')
        else:
            print('Wrong account number')


a1 = Bank_account(1234, 1000)
a1_balance = a1.get_Balance()
print(a1_balance)
a1.inc_balance(1000)
a1.print_balance()
a1.withdraw_balance(500)
a1.print_balance()
"""

"""
class Employee:
    import datetime

    def __init__(self, name: str, employment_date, payment_info: int):
       """ """
        :param name: Enter employee name
        :param employment_date: Enter date of employment (year-month-day)
        :param payment_info: monthly salery (integer)
        """"""
        self.name = name
        self.employment_date = employment_date
        self.payment_info = payment_info

    def get_employee_info(self):
        return f'Name: {self.name}\nYear of employment: {self.employment_date}\nPayment info: {self.payment_info} kr'

    def employment_period_years(self):
        # dela upp datumet till tre element i en lista ['2020', '05', '14']
        date_list = str(self.employment_date).split('-')
        # skapa en datetime-variabel där genom dens konstruktor 'datetime.date(year, month, day)'
        # där de olika elementen i listan indexeras ut på rätt plats
        employmen_date = datetime.date(int(date_list[0]), int(date_list[1]), int(date_list[2]))

        # import todays date
        todays_date = datetime.date.today()
        # calculate days employed
        days_employed = (todays_date - employmen_date).days
        # convert to years employed
        years_employed = days_employed / 365.25
        # round years employed to 1 decimal
        rounded_years_employed = round(years_employed, 1)
        # return result as string
        return str(rounded_years_employed) + ' ' + "years of employment"


e1 = Employee("Viggo", "2020-05-01", 25000)
print(e1.get_employee_info())
print(e1.employment_period_years())
"""


class Student:
    def __init__(self, name: str, grades: list):
        """
        :param name: Enter Student Name
        :param grades: Enter grades inside list [a, b, c,]
        """
        self.name = name
        self.grades = grades

    def print_grade(self):
        print(self.grades)

    def calc_avrg_grade(self):
        total_grades = 0
        for i in self.grades:
            if 'a' in i:
                total_grades += 0
            elif 'b' in i:
                total_grades += 1
            elif 'c' in i:
                total_grades += 2
            elif 'd' in i:
                total_grades += 3
            elif 'e' in i:
                total_grades += 4
            elif 'f' in i:
                total_grades += 5
        print(total_grades)
        grades = ['a', 'b', 'c', 'd', 'e', 'f']
        avrg = total_grades/len(self.grades)
        return "The avrage grade is " + grades[round(avrg)]


s1 = Student("Viggo", ["a", "b", "c", "d", "d", 'd'])
s1.print_grade()
print(s1.calc_avrg_grade())
