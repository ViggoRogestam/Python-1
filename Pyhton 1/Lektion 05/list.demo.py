deltagare = ["Lina", "Gunilla", "Erik", "Carl"]
i = 0
while i < len(deltagare):
    print("Välkommer " + deltagare[i])
    deltagare.remove(deltagare[i])
    i += 1

deltagare = ["Lina", "Gunilla", "Erik", "Carl"]
for namn in deltagare:
    print(f"Väkommen {namn}")
    del deltagare[namn]