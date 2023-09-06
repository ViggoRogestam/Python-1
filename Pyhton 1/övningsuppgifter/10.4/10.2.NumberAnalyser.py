with open('numbers.csv', 'r') as my_file:
    numbers = my_file.read()

ett = 0
två = 0
tre = 0
fyra = 0
fem = 0
sex = 0
sju = 0
åtta = 0
nio = 0
for index in numbers:

    if index == 0:
        continue
    elif index == "1":
        ett += 1
    elif index == "2":
        två += 1
    elif index == "3":
        tre += 1
    elif index == "4":
        fyra += 1
    elif index == "5":
        fem += 1
    elif index == "6":
        sex += 1
    elif index == "7":
        sju += 1
    elif index == "8":
        åtta += 1
    elif index == "9":
        nio += 1
ui_width = 30
print("-"* ui_width)
print(".: NUMBERANALYSER :.".center(ui_width))
print("-"* ui_width)
print(f"| 1 | {ett}")
print(f"| 2 | {två}")
print(f"| 3 | {tre}")
print(f"| 4 | {fyra}")
print(f"| 5 | {fem}")
print(f"| 6 | {sex}")
print(f"| 7 | {sju}")
print(f"| 8 | {åtta}")
print(f"| 9 | {nio}")