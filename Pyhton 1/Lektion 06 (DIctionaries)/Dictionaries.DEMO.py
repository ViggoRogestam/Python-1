# Dictionaries DEMO


# Skapa Dict:en
person = {
    "name": "Mahmud",
    "age": 50
}

# Hämta ett element
print(f'Hej {person}["name"]', end='. ')
print(f'Du är {person["age"]} år gammal.')
"""
# Referera till en nyckel dynamiskt
key = input('Ange attribut (nyckel) >')

# Försök skriva ut värdet under anginva nyckeln
try:
    print(person[key])
except KeyError as key_error:
    print(f'Fel! Attributet {key_error} existerar inte!')
"""
# Ändra värdet
person['age'] = 51
print(f'\n{person}')

# Lägg till ny data (key-value-pair) / (element)
person['address'] = 'Hemfridsvägen 17'
print(f'\n{person}')

# Ta bort element
del person['age']
print(f'\n{person}')

# Kopiera dict
person_copy = person.copy()
print(person_copy)

# Ta bort objekt
"""
del person_copy
print(person_copy) # Visar ibland felmeddelande
"""

# Iteration av dict
for key in person:
    print(f'Key: {key}')
    print(f'Value: {person[key]}')

# Nästlande dict
person['adress'] = {
    "gaturadress": "Hemfridsvägen 17",
    "ort": "Sollentuna",
    "postnummer": 19267
}

# SKriv ut adressen enligt svensk standard
print("\nADRESS:")
print(person['adress']['gaturadress'])
print(person['adress']['postnummer'], (person['adress']['ort']).upper())
