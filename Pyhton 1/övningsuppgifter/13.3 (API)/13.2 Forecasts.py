import json
import requests
import os

# Variables
ui_withd = 30
city = ''
# Connect to API
url = "https://54qhf521ze.execute-api.eu-north-1.amazonaws.com/weather/"

# Loop som programmet körs i
while True:
    # Rensa Terminalen
    if os.name == 'posix':  # För Unix/Linux/macOS
        os.system('clear')
    else:  # För övriga operativsystem
        os.system('cls')
    # Layout
    print("""
    Enter the name of the city
    for which you want forecasts :""")

    # Indata från användaren
    while True:
        try:
            city = str(input('> '))
            break
        except:
            print('Oväntat fel')
            continue

    # Make GET request wiht the query string parameter
    response = requests.get(url + city)

    # Convert response from json to a pyhton dict
    data = json.loads(response.text)
    # layout
    print("-" * ui_withd)
    print('FORECASTS'.center(ui_withd))
    print('*' * ui_withd)
    # Iterate in data and print dates and forecasts
    for forecast in data['forecasts']:
        print(f'{forecast["date"]}      {forecast["forecast"]}')

    print("-" * ui_withd)

    input('Press enter to exit...')
    break
