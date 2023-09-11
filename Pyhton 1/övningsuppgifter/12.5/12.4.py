notes = {
    'Meddelande från skolan': 'Friluftsdag på tisdag ',
    'Kom ihåg!': 'Ta bilen till verkstad',
    'Inför tentamen': 'Gör alla instuderingsuppgifter'
}
# definiera titel och text
print('Lägg till artikel:')
title = input('titel >')
text = input('text >')

# lägg till titel och text i dict:en
notes[title] = text

# Skriv ut dict:en
for key in notes:
    print('-----')
    print(f'Titel: {key}')
    print(f'Text: {notes[key]}')
