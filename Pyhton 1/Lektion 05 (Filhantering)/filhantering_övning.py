attendants = ["Lisa", "Kalle", "Olivia", "Johan"]

with open("textfil.txt", "w") as my_file:
    for attendant in attendants:
        my_file.write("Hello " + attendant + "!\n")
my_file.close()
