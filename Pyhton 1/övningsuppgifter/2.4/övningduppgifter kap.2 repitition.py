
# 2.1
citat = input("datatyper har inbyggda metoder")
print(citat.upper())

#2.2
input = int(input("Mata in ett flyttal: "))
print(round(input))


#2.3
print("Hallå!")
first_name = input("Vad är ditt förnamn?: ")
last_name = input("Vad är ditt efternamn?: ")
print("Trevligt att träffas", first_name, last_name)


# 2.4
age = int(input("Hur gammal är du?: "))
age 
print("Du är myndig inom", (18- age), "år")


#2.5
print("Ange tal:")
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
maximum = max(a,b,c,d,e)
print("a =", a)
print("b =", b)
print("c =", c)
print("d =", d)
print("e =", e)
print()
print("Det högsta inmatade heltalet är", maximum)


#2.6

#Layout
import math
print("""
.: KORVKOLLEN 1.0.1 :.
- -- - -- - -- - -- - -- -   
Hur många elever vill ha ...""")

#Sausages Amount
sausage_2 = int(input("2 vanliga korvar: "))
sausage_3 = int(input("3 vanliga korvar: "))
vegan_sausage_2 = int(input("2 vegnaska korvar: "))
vegan_sausage_3 = int(input("3 veganska korvar: "))

#Layout
print("""
- -- - -- - -- - -- - -- - -- - -- -
-           INKÖPSLISTA            -
- -- - -- - -- - -- - -- - -- - -- -""")

#Math
sausage_pack = math.ceil((sausage_2 * 2 + sausage_3 * 3) /8)
vegan_sausage_pack = math.ceil((vegan_sausage_2 * 2 + vegan_sausage_3 * 3) /4)
drinks = sausage_2 + sausage_3 + vegan_sausage_2 + vegan_sausage_3

#Prices
sausage_pack_price = 20.95
vegan_sausage_pack_price = 34.95
drink_price = 13.95

total_sausage_price = sausage_pack * sausage_pack_price
total_vegan_sausage_price = vegan_sausage_pack * vegan_sausage_pack_price
total_drinks_price = drinks * drink_price


#Results
print("| Vanlig korv:", sausage_pack,"förpackingar")
print("| Vegansk korv:", vegan_sausage_pack,"förpackingar")
print("| Dryck:", drinks,"drickor")
print("""
- -- - -- - -- - -- - -- - -- - -- -""")
print ("|", total_sausage_price + total_vegan_sausage_price + total_drinks_price,"SEK")
print("""
- -- - -- - -- - -- - -- - -- - -- -""")
