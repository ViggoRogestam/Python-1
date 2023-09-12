import random
# Skapa en lista med 10 slumpmässiga heltal
my_list = [random.randint(1, 100) for i in range(1, 11)]
# Skapa en ny lista med listkomprehension som endast innehåller de udda talen från den första listan
new_list = [tal for tal in my_list if tal % 2 != 0 ]
print(new_list)