import random
# En klass som beskriver en rektangel

class Rectangle:
    def __init__(self, length, width):
        # Private Attributes
        self.__length = length
        self.__width = width

    # Gettters & Setters
    def get_length(self):
        return self.__length

    def set_length(self, length):
        if length > 0:
            self.__length = length
        else:
            print('Felaktig längd')

    def get_width(self):
        return self.__width

    def set_width(self, width):
        if width > 0:
            self.__width = width
        else:
            print('Felaktig bredd')

    # Methods
    def area(self):
        return self.get_length() * self.get_width()

    def circumference(self):
        return 2 * (self.get_length() + self.get_width())


"""# Skapa objekt av klassen rectangle
r1 = Rectangle(5, 10)
r2 = Rectangle(10, 20)
r3 = Rectangle(2, 15)

# print
print(f'r2 Area: {r2.area()}\nr2 Circumference: {r2.circumference()}')
print(f'r3 Area: {r3.area()}\nr3 Circumference: {r3.circumference()}')

# lista av objekt
r_lista = [
    Rectangle(1, 2),
    Rectangle(3, 4),
    Rectangle(5, 6),
    Rectangle(7, 8),
]
for r in r_lista:
    print(r.area())"""

# skapa en tom lista
r_list = []

# skapa en iteration som loopar 1000 gånger
for i in range(1000):
    # skapa en instans av rectangle
    r_list.append(Rectangle(random.randint(1, 100), random.randint(1, 100)))

area_sum = 0
for r in r_list:
    area_sum += r.area()
print(area_sum)
