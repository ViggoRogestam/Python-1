# Mata in ett tal, skriver ut dubbla värdet av talet.
indata = input("Mata in ett heltal >")
try:
    indata =int(indata)
    results = indata * 2 # Math
    print("RESULTAT:", results)
except:
    print(indata, "kan inte översättas till ett heltal")