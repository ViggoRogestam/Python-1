# Definera en funktion som skapar en dict av en sträng som innehåller förekomsten av varje bostav i strängen och skriv sedan ut innehållet snyggt
def bokstavsfrekvens(x):
    x = str(x).upper()
    text_freq = {}
    i = 0
    for i in x:
        if i in text_freq:
            text_freq[i] += 1
        elif i not in text_freq:
            text_freq[i] = 1
    sorted_dict = {key: text_freq[key] for key in sorted(text_freq)}
    for letter in sorted_dict:
        print(letter, ':', sorted_dict[letter])

# Be använderen mata in en text        
my_str = input('Mata in text > ').replace(" ", "")

# Kör texten genom funktionen
bokstavsfrekvens(my_str)
        
