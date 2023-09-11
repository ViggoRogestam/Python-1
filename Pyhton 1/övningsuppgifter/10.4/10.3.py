import os
import csv

ui_width = 30

# Variables
found_person = []
imported_database = []

# Import database
with open('database.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    people_data = list(csv_reader)

while True:
    os.system('cls' if os.name == 'nt' else 'clear')  # rensar terminalen
    # Layout
    print('-' * ui_width)
    print('.: PEOPLES DATABASE :.'.center(ui_width))
    print('-' * ui_width)
    print('get_id | Get person by ID')
    print('scan_f | List people by FORENAME')
    print('scan_s | List people by SURNAME')
    print('exit | Exit program')
    print('-' * ui_width)

    indata = input(">")
    if indata == "get_id":
        id_nummer = input('Enter ID Number >')
        for person in people_data:
            if person["ID"] == id_nummer:
                print('-' * ui_width)
                print(f"Matches found:")
                for key, value in person.items():
                    print(f"{key}: {value}")
                print('-' * ui_width)
                input('Press any key to continue...')

    elif indata == "scan_f":
        name = input('Enter Forename >')
        for person in people_data:
            if person['FORENAME'].lower() == name.lower():
                print('-' * ui_width)
                print(f"Matches found:")
                for key, value in person.items():
                    print(f'{key}: {value}')
        print('-' * ui_width)
        input('Press any key to continue...')

    elif indata == "scan_s":
        lsst_name = input('Enter Surname >')
        for person in people_data:
            if person['SURNAME'].lower() == lsst_name.lower():
                print('-' * ui_width)
                print(f"Matches found:")
                for key, value in person.items():
                    print(f'{key}: {value}')
        print('-' * ui_width)
        input('Press any key to continue...')
    elif indata.lower() == "exit":
        break
