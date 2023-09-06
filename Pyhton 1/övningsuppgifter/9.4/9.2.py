registrerade =["Anna", "Eva", "Erik", "Lars", "Karl"]
avanmälningar =["Anna", "Erik", "Karl"]

# Skapa kopia av lista
registrerade_copy = registrerade.copy()

for namn in avanmälningar:
    if namn in registrerade_copy:
        registrerade_copy.remove(namn)

print(registrerade_copy)