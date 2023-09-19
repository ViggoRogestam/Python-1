import random
"""Din uppgift är att konstruera en funktion get_even(lista) som returnerar samtliga 
   jämna heltal från listan. Listan i lista ska inte ändras av funktionen."""
numbers = []

for x in range(10):
    numbers.append(random.randint(0, 9))


def get_even(list):
    even_list = []
    for number in list:
        if number % 2 == 0:
            even_list.append(number)

    return even_list


even = get_even(numbers)
print('even:', even)
print('numbers:', numbers)
