# Formatera om lista till json
import json

random_stuff = [1337, 13.37, "Ååh Yää!"]

with open('text.json', 'w') as f:
    random_stuff = json.dumps(random_stuff)
    f.write(random_stuff)

print(random_stuff)

