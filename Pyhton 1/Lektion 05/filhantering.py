"""f = open("textfil.txt", "x")"""
import os

if os.path.exists('textfil.txt'):
    # Läser en befintlig fil och gör den skrivbar (w = write)
    my_file = open('textfil.txt', 'w')
else:
    # Skapa en ny fil (x = create)
    my_file = open('textfil.txt', 'x')


# Skriv till en fil
my_file.write("Rad 1.\n")
my_file.write("Rad 2.\n")
my_file.write("Rad 3.\n")


# Öppna och läs från en fil (r = read)
my_file = open('textfil.txt', 'r')
text = my_file.read()
print(text)
# Stänger filen (för att frigöra resurser)
my_file.close()


# Öppna en fil med with
with open('textfil.txt', "a+") as my_file:
    my_file.write("rad 4.\n")
    my_file.seek(0)
    text = my_file.read()
print(text)

# Ta bort en fil
if os.path.exists("textfil.txt"):
    os.remove("textfil.txt")
    print("File is removed")
else:
    print("The file does not exist")