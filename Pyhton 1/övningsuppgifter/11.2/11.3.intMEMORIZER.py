import json
import os

# Variabler

try:
    with open('heltal.json', 'r') as f:
        heltal_lista = json.load(f)
except FileNotFoundError:
    heltal_lista = []

while True:
    # Rensar Terminalen
    if os.name == 'posix':  # För Unix/Linux/macOS
        os.system('clear')
    elif os.name == 'nt':  # För Windows
        os.system('cls')

    # Sortera listan
    heltal_lista.sort()

    # Layout
    ui_width = 18
    print('.: intMEMORIZER :.')
    print('*'*ui_width)

    # Printa ut memorerade heltal
    for heltal in heltal_lista:
        print(f'{heltal}')
    print('-'*ui_width)
    print(f'SUMMA: ', sum(heltal_lista))
    print('-' * ui_width)

    try:
        indata = int(input('Ange heltal: '))
        if indata == 0:
            break
        elif indata not in heltal_lista:
            heltal_lista.append(indata)
        else:
            continue

    except ValueError:
        print(f'FEL. inmatningen är inte ett heltal')
        input('Tryck valfri tagnet för att forstätta...')
        continue

with open('heltal.json', 'w') as f:
    json.dump(heltal_lista, f)

