import os
import json

# Öppna JSON filen och lagra den i variabeln 'notes'
with open('notes.json') as f:
    notes = json.load(f)

# Variables
i = 0
ui_widht = 30

while True:
    # Rensar Terminalen
    if os.name == 'posix':  # För Unix/Linux/macOS
        os.system('clear')
    elif os.name == 'nt':  # För Windows
        os.system('cls')

    # Layout
    print('.: ALWAYSNOTE :.'.center(ui_widht))
    print('-- gold edition --'.center(ui_widht))
    print('*' * ui_widht)

    # Skriv ut anteckningar
    for note in notes:
        print('-', note)

    # Layout
    print('-' * ui_widht)
    print('view | view note')
    print('add | add note')
    print('rm | remove note')
    print('exit | exit program')
    print('-' * ui_widht)

    # user input
    choice = input('menu > ').lower()

    # Visa anteckningar
    if choice == 'view':
        choice_note = input('Title: >')
        try:
            print('-' * ui_widht)
            print(f'{notes[choice_note]}')
            print('-' * ui_widht)
            input('Press any key to continue...')
        except KeyError:
            print(f'Fel. Anteckningen finns inte')
            input('Press any key to continue...')

    # Lägg till anteckning
    elif choice == 'add':
        try:
            # Get user input
            print('-' * ui_widht)
            choice_title = input('Title >')
            choice_desc = input('Desc >')

            # Try to add the note to the dict
            notes[choice_title] = choice_desc

            # Layout
            print('-' * ui_widht)
            print('INFO: Note added')
            print('-' * ui_widht)
            input('Press any key to continue...')
        except:
            print('Unexpected error')

    # Ta bort anteckning
    elif choice == 'rm':
        try:
            choice_remove = input('Title >')
            del notes[choice_remove]

            # Layout
            print('-' * ui_widht)
            print('INFO: Note deleted')
            print('-' * ui_widht)
            input('Press any key to continue...')
        except:
            print('Note does not exist')

    elif choice == 'exit':
        # Spara anteckningarna till JSON filen
        with open('notes.json', 'w') as f:
            json.dump(notes, f)
        break
print('Programmet avlsutas.')
