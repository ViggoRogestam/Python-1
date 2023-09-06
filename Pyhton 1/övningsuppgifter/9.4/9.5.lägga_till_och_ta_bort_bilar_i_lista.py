# List
cars = ["Volvo", "Toyota", "Kia"]
# Layout
ui_width = 30

while True:
    import os

    os.system('cls' if os.name == 'nt' else 'clear')
    print("*" * ui_width)
    print(".: STACKMASTER 1.0 :.".center(ui_width))
    print("-" * ui_width)
    for element in cars:
        print(f"-{element}")
    print("-" * ui_width)
    print("MENU".center(ui_width))
    print("-" * ui_width)
    print("PUSH | Push element to stack")
    print("PULL | Pull element from stack")
    print("EXIT | Exit program")
    print("-" * ui_width)
    print(ui_width * "-")
    indata = input("Välj alternativ (PUSH, PULL, EXIT)>".lower())
    if indata == "push":
        push = input("Vilket bilmärke vill du lägga till? >").capitalize()
        cars.append(push)
    elif indata == "pull":
        if len(cars) == 0:
           print("error: finns inga bilar att ta bort.")
           input("Tryck valfri knapp för att forstätta...")
        else:
            pull = input(f"Vill du ta bort {cars[-1]}? y/n>".lower())
            if pull == "y":
                removed_car = cars.pop()
                print(f"{removed_car} togs bort")
            else:
                continue
    elif indata == "exit":
        break
print("Tryck på valfri tagnet för att avsluta....")
input()
