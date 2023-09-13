notes = {
    'Meddelande från skolan': 'Friluftsdag på tisdag ',
    'Kom ihåg!': 'Ta bilen till verkstad',
    'Inför tentamen': 'Gör alla instuderingsuppgifter'
}
# Skriv ut key och value för varje objekt i dict:en
for note in notes:
    print('-----')
    print(f'Titel: {note}')
    print(f'Text: {notes[note]}')
