# API: https://4bbh01oqwj.execute-api.eu-north-1.amazonaws.com/numcheck?integer=100
import requests
import json

# connect to the api
url = "https://4bbh01oqwj.execute-api.eu-north-1.amazonaws.com/numcheck"

# User input
while True:
    try:
        user_int = int(input('Enter a positive integer >'))
        if user_int < 0:
            print('FEL: Ange ett positivt heltal.')
        else:
            break
    except ValueError:
        print('FEL: Användarinmatningen är inte ett heltal')
        continue

# Create query string parameter from the user_int
param = {"integer": user_int}

# Make GET request wiht the query string parameter
response = requests.get(url, params=param)

# Convert response from json to a pyhton dict
data = json.loads(response.text)

if data['even'] == True:
    print(f'{user_int} är ett jämt nummer.', end=' ')
else:
    print(f'{user_int} är inte ett jämt nummer.', end=' ')
if data['prime'] == True:
    print(f'Nummret är ett primtal.')
else: print(f'Nummret är inte ett primtal.')

if data.get('factors'):
    # Konvertera alla faktorer till strängar
    factor_strings = [str(factor) for factor in data['factors']]

    # Skapa en sträng med alla faktorer separerade med ", "
    factor_string = ", ".join(factor_strings)

    # Ersätt det sista kommat med ", och"
    factor_string = factor_string[::-1].replace(",", "hco ", 1)[::-1]

    # Skriv ut den färdiga strängen
    print(f"Numrets faktorer är {factor_string}.")


