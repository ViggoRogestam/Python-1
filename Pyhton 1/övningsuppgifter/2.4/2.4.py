"""
Ovningsuppgift 2.4. Skapa ett program som fr˚agar om anv¨andarens ˚alder.
Programmet ska svara anv¨andaren inom hur m˚anga ˚ar anv¨andaren uppn˚ar myn-
dig ˚alder (18 ˚ar).
Hur gammal ¨a r du ?
> 13
Du ¨a r myndig inom 5 ˚a r !
"""

input = input("Hur gammal är du?: ")
ålder = int(input)
årTillMyndig = 18 - ålder
print("Du är myndig inom", årTillMyndig, "år!")