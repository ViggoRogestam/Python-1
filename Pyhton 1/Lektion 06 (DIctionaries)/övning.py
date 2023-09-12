# Övning på tolkning av dict
person = {
    "firstname": "Johan",
    "lastname": "Svensson",
    "age": 25,
    "pets": [
        {"name": "Morris", "age": 3, "type": "hund"},
        {"name": "Lisa", "age": 4, "type": "katt"}
    ]
}

# Skapa variabler
name = person['firstname'] + ' ' + person["lastname"]
age = person["age"]
pets = person["pets"] # Hela listan
num_pets = len(pets)

# Skriv ut
print('...ÖVNING...')
print(f'{name} är {age} år gammal och har {num_pets} husdjur:')
for pet in pets:
    print(f'* En {pet["age"]} år gammal {pet["type"]} som heter {pet["name"]}')


# Skriv ut namnet på första husdjuret
print(f'\n{person["pets"][0]["name"]}')
