notes = {
    'Meddelande från skolan': 'Friluftsdag på tisdag ',
    'Kom ihåg!': 'Ta bilen till verkstad',
    'Inför tentamen': 'Gör alla instuderingsuppgifter'
}
# Anteckning som ska tas bort
title = input('Ta bort artikel: ')

# Ta bort anteckning från dict
try:
    del notes[title]
except KeyError:
    print('Fel. Anteckningen finns inte')
# Skriv ut dict:en
for key in notes:
    print('-----')
    print(f'Titel: {key}')
    print(f'Text: {notes[key]}')
