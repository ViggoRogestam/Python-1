# Anslagstavla
import os

# Variabler
POST_1 = ' '
POST_2 = ' '
POST_3 = ' '

while True:
    # Rensa teminalförnster
    if os.name == 'posix':  # För Unix/Linux/macOS
        os.system('clear')
    elif os.name == 'nt':  # För Windows
        os.system('cls')
    # Layout
    print('\n.: basicBILLBOARD :.')
    print('********************')
    print('P1 : ', POST_1)
    print('P2 : ', POST_2)
    print('P3 : ', POST_3)
    print('-- -- -- --- -- -- -- --- --')
    print('c | Ändra post')
    print('e | Stäng program')
    print('-- -- -- --- -- -- -- --- --')

    indata = input('Ange kommand >').lower()

    if indata == 'c':
        choice = input('Vilken post vill du ändra? >').lower()
        if choice == 'p1':
            POST_1 = input('Ange vad POST_1 ska säga >')
        elif choice == 'p2':
            POST_2 = input('Ange vad POST_2 ska säga >')

        elif choice == 'p3':
            POST_3 = input('Ange vad POST_3 ska säga >')

        else:
            print('FEl: kommand inte giltigt.')

    elif indata == 'e':
        print('Tryck på valfri tagnet för att avsluta >')
        input()
        break

    else:
        print('FEl: kommand inte giltigt.')
        input('\nTryck på valfri tagnet för att fortsätta...')
