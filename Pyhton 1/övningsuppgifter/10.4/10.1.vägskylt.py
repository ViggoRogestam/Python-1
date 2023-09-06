# Öppna en fil med with (a+ = appaend och läs)
import os
while True:
    os.system('cls' if os.name == 'nt' else 'clear')  # rensar terminalen
    with open('../9.4/sign.txt', "r") as my_file:
        text = my_file.read()
    print("|---------------------------------------------------------------------------------|")
    print("|  #  ----------------------------------------------------------          #       |")
    print(f"| xxx |              Welcome to  {text}                       |    #    ###      |")
    print("| xxx ----------------------------------------------------------   ###   ###      |")
    print("|  |                     |                   |                      |     |    #  |")
    print("|---------------------------------------------------------------------------------|")
    print("|  C | Change sign message")
    print("|  E | Exit program")
    print("|-------------------------")
    indata = input(">").lower()
    if indata == "c":
        with open('../9.4/sign.txt', "w+") as my_file:
            indata = input("Vad ska skylten säga? >")
            my_file.write(indata)
            my_file.seek(0)  # Gå till filens första position
            text = my_file.read()
    elif indata == "e":
        break
    else:
        print("Error: Not vaild input")
        input("\nPress any key to continue")
        continue
