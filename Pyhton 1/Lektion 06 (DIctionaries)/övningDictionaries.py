# Lista som innehåller 100 dictionaries med information om personers förnamn, efternamn och ålder
people = [
    {"forename": "Erik", "surname": "Karlsson", "age": 45},
    {"forename": "Anna", "surname": "Andersson", "age": 29},
    {"forename": "Peter", "surname": "Johansson", "age": 82},
    {"forename": "Linda", "surname": "Svensson", "age": 56},
    {"forename": "Karin", "surname": "Nilsson", "age": 34},
    {"forename": "David", "surname": "Larsson", "age": 63},
    {"forename": "Erik", "surname": "Svensson", "age": 41},
    {"forename": "Anna", "surname": "Karlsson", "age": 71},
    {"forename": "Peter", "surname": "Andersson", "age": 66},
    {"forename": "Linda", "surname": "Karlsson", "age": 49},
    {"forename": "Karin", "surname": "Johansson", "age": 37},
    {"forename": "David", "surname": "Nilsson", "age": 59},
    {"forename": "Erik", "surname": "Larsson", "age": 50},
    {"forename": "Anna", "surname": "Johansson", "age": 30},
    {"forename": "Peter", "surname": "Larsson", "age": 69},
    {"forename": "Linda", "surname": "Karlsson", "age": 45},
    {"forename": "Karin", "surname": "Svensson", "age": 82},
    {"forename": "David", "surname": "Andersson", "age": 72},
    {"forename": "Erik", "surname": "Nilsson", "age": 47},
    {"forename": "Anna", "surname": "Svensson", "age": 38},
    {"forename": "Peter", "surname": "Johansson", "age": 29},
    {"forename": "Linda", "surname": "Larsson", "age": 58},
    {"forename": "Karin", "surname": "Karlsson", "age": 65},
    {"forename": "David", "surname": "Nilsson", "age": 21},
    {"forename": "Erik", "surname": "Karlsson", "age": 27},
    {"forename": "Anna", "surname": "Andersson", "age": 43},
    {"forename": "Peter", "surname": "Svensson", "age": 30},
    {"forename": "Linda", "surname": "Larsson", "age": 75},
    {"forename": "Karin", "surname": "Johansson", "age": 62},
    {"forename": "David", "surname": "Karlsson", "age": 22},
    {"forename": "Erik", "surname": "Svensson", "age": 23},
    {"forename": "Anna", "surname": "Nilsson", "age": 69},
    {"forename": "Peter", "surname": "Johansson", "age": 35},
    {"forename": "Linda", "surname": "Karlsson", "age": 40},
    {"forename": "Karin", "surname": "Larsson", "age": 26},
    {"forename": "David", "surname": "Karlsson", "age": 64},
    {"forename": "Erik", "surname": "Andersson", "age": 44},
    {"forename": "Anna", "surname": "Svensson", "age": 48},
    {"forename": "Peter", "surname": "Larsson", "age": 57},
    {"forename": "Linda", "surname": "Johansson", "age": 55},
    {"forename": "Karin", "surname": "Nilsson", "age": 34},
    {"forename": "David", "surname": "Karlsson", "age": 53},
    {"forename": "Erik", "surname": "Svensson", "age": 61},
    {"forename": "Anna", "surname": "Andersson", "age": 42},
    {"forename": "Peter", "surname": "Johansson", "age": 36},
    {"forename": "Linda", "surname": "Larsson", "age": 70},
    {"forename": "Karin", "surname": "Karlsson", "age": 31},
    {"forename": "David", "surname": "Nilsson", "age": 19},
    {"forename": "Erik", "surname": "Karlsson", "age": 49},
    {"forename": "Anna", "surname": "Svensson", "age": 28},
    {"forename": "Peter", "surname": "Andersson", "age": 39},
    {"forename": "Linda", "surname": "Svensson", "age": 73},
    {"forename": "Karin", "surname": "Johansson", "age": 24},
    {"forename": "David", "surname": "Andersson", "age": 67},
    {"forename": "Erik", "surname": "Karlsson", "age": 77},
    {"forename": "Anna", "surname": "Nilsson", "age": 32},
    {"forename": "Peter", "surname": "Svensson", "age": 25},
    {"forename": "Linda", "surname": "Larsson", "age": 60},
    {"forename": "Karin", "surname": "Karlsson", "age": 52},
    {"forename": "David", "surname": "Nilsson", "age": 37},
    {"forename": "Erik", "surname": "Svensson", "age": 68},
    {"forename": "Anna", "surname": "Andersson", "age": 41},
    {"forename": "Peter", "surname": "Johansson", "age": 33},
    {"forename": "Linda", "surname": "Karlsson", "age": 29},
    {"forename": "Karin", "surname": "Johansson", "age": 63},
    {"forename": "David", "surname": "Karlsson", "age": 74},
    {"forename": "Erik", "surname": "Andersson", "age": 70},
    {"forename": "Anna", "surname": "Svensson", "age": 31},
    {"forename": "Peter", "surname": "Larsson", "age": 46},
    {"forename": "Linda", "surname": "Johansson", "age": 27},
    {"forename": "Karin", "surname": "Nilsson", "age": 80},
    {"forename": "David", "surname": "Karlsson", "age": 54},
    {"forename": "Erik", "surname": "Svensson", "age": 47},
    {"forename": "Anna", "surname": "Andersson", "age": 66},
    {"forename": "Peter", "surname": "Johansson", "age": 21},
    {"forename": "Linda", "surname": "Larsson", "age": 83},
    {"forename": "Karin", "surname": "Karlsson", "age": 22},
    {"forename": "David", "surname": "Nilsson", "age": 37},
    {"forename": "Erik", "surname": "Karlsson", "age": 25},
    {"forename": "Anna", "surname": "Svensson", "age": 61},
    {"forename": "Peter", "surname": "Andersson", "age": 48},
    {"forename": "Linda", "surname": "Svensson", "age": 36},
    {"forename": "Karin", "surname": "Johansson", "age": 70},
    {"forename": "David", "surname": "Andersson", "age": 58},
    {"forename": "Erik", "surname": "Karlsson", "age": 64},
    {"forename": "Anna", "surname": "Nilsson", "age": 33},
    {"forename": "Peter", "surname": "Svensson", "age": 55},
    {"forename": "Linda", "surname": "Larsson", "age": 50},
    {"forename": "Karin", "surname": "Karlsson", "age": 39},
    {"forename": "David", "surname": "Nilsson", "age": 43},
    {"forename": "Erik", "surname": "Svensson", "age": 76},
    {"forename": "Anna", "surname": "Andersson", "age": 71},
    {"forename": "Peter", "surname": "Johansson", "age": 74},
    {"forename": "Linda", "surname": "Karlsson", "age": 24},
    {"forename": "Karin", "surname": "Johansson", "age": 53},
    {"forename": "David", "surname": "Karlsson", "age": 29},
    {"forename": "Erik", "surname": "Andersson", "age": 42},
    {"forename": "Anna", "surname": "Svensson", "age": 57},
    {"forename": "Peter", "surname": "Larsson", "age": 38},
]
# Skapa program där man kan skriva in en ålder och få personer med denna ålder utskrivna
print('Vilken ålder vill du söka efter?')
search_age = int(input('> '))

print('-' * 5)
# Iterera genom listan och sök efter åldern användaren angav
for person in people:
    # Om åldern användaren angav matchar med en ålder i listan
    if person['age'] == search_age:
        print(f'- {person["forename"]} {person["surname"]} ({person["age"]}) år')