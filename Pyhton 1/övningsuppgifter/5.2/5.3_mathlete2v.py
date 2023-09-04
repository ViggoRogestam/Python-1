#Mathlete

# Layout
ui_width = 30
print(ui_width * "*")
print("MATHLETE".center(ui_width))
print(ui_width * "-")
print()


# variables
sum = 0
avrage = 0
kardinalitet = 0
while True:
    indata = input(">")
    indata_lower = indata.lower()
    try:
        indata = int(indata)
        sum += indata
        kardinalitet += 1
        avrage = sum / kardinalitet
    except ValueError:
        print("FEL: ogilgit nummer")
    if indata_lower == "exit":
        break
print(ui_width * "-")
print("Kardinalitet: ", kardinalitet)
print("Summa: ", sum)
print("Medelvärde: ", avrage)        