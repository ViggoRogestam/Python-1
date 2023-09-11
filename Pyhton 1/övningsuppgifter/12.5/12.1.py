notes = {
    'Meddelande från skolan': 'Friluftsdag på tisdag ',
    'Kom ihåg!': 'Ta bilen till verkstad',
    'Inför tentamen': 'Gör alla instuderingsuppgifter'
}
# Variables
ui_widht = 25
# Layout
print('.: ANTECKNINGAR :.')
for key in notes:
    print(f'\n{key}')
print('-'*ui_widht)

# Mata in antckning som ska skrivas ut
input_note = input('Anteckning >')
try:
    note = notes[input_note]
    print(note)


except KeyError as key_error:
    print(f'FEl, anteckningen {key_error} finns inte')