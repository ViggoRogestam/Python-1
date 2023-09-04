import random
import os




# Layout
ui_width = 30
print(ui_width * "*")
print(".: HIGHER OR LOWER GAME :.".center(ui_width))
print(ui_width * "-")
print("""Welcome to the higher or lower game. 
I will randomise a number between 
0 and 99. Can you guess it?""")
print(ui_width * "-")

# Math
random_int = random.randint(1, 99)

counter = 0
while True:
    try:
        indata = input("Enter your guess >")
        counter += 1
        indata = int(indata)
        if indata > random_int:
            print("LOWER ! ")

        elif indata < random_int:
            print("HIGHER ! ")

        elif indata == random_int:
            print(indata, "is correct!")
            print("It took you", counter, "guesses")
            print("Good job!")

            user_value = input("Do you want to continue? y/n >").lower()
            if user_value != "y":
                break
    except:
        print(indata, "är inte ett tal")