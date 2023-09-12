import json
attendants = ['Åsa', 'Kalle', 'Olivia', 'Johan']

with open('data.json', 'w') as my_file:
    my_file.write(json.dumps(attendants))

with open('data.json') as f:
    data = json.loads(f.read())

print(data[0])