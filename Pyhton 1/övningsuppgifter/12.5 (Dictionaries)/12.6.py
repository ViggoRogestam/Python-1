import os
import json

# Öppna JSON filen och lagra den i variabeln 'notes'
try:
    with open('notes.json') as f:
        notes = json.load(f)
except FileNotFoundError:
    notes = {}

# Variables
ui_width = 30

while True:
    # Rensa Terminalen
    if os.name == 'posix':  # För Unix/Linux/macOS
        os.system('clear')
    else:  # För övriga operativsystem
        os.system('cls')

    # Layoutx
    print('.: ALWAYSNOTE :.'.center(ui_width))
    print('-- gold edition --'.center(ui_width))
    print('*' * ui_width)

    # Skriv ut anteckningar (innehåll från notes)
    for note in notes:
        print('-', note)

    # Layout
    print('-' * ui_width)
    print('view | view note')
    print('add | add note')
    print('rm | remove note')
    print('exit | exit program')
    print('-' * ui_width)

    # user input
    choice = input('menu > ').lower()

    # Implimentera view
    if choice == 'view':
        choice_note = input('Title: >')
        try:
            print('-' * ui_width)
            print(f'{notes[choice_note]}')
            print('-' * ui_width)
            input('Press any key to continue...')
        except KeyError:
            print(f'Fel. Anteckningen finns inte')
            input('Press any key to continue...')

    # Implimitera add
    elif choice == 'add':
        try:
            # Get user input
            print('-' * ui_width)
            choice_title = input('Title >')
            choice_descr = input('Descr >')

            # Try to add the note to the dict
            notes[choice_title] = choice_descr

            # Layout
            print('-' * ui_width)
            print('INFO: Note added')
            print('-' * ui_width)
            input('Press any key to continue...')
        except:
            print('Unexpected error')

    # implimintera rm (remove)
    elif choice == 'rm':
        try:
            choice_remove = input('Title >')
            del notes[choice_remove]

            # Layout
            print('-' * ui_width)
            print('INFO: Note deleted')
            print('-' * ui_width)
            input('Press any key to continue...')
        except:
            print('Note does not exist')
    # Implimintera exit
    elif choice == 'exit':
        # Spara anteckningarna till JSON filen
        with open('notes.json', 'w') as f:
            json.dump(notes, f)
            print("\n\033[3m" + "Saving to notes.json..." + "\033[0m")
            print('\n\033[1m' + 'Programmet stängdes.' + '\033[0m')
        break



