
# Övningsuppgift 2.6. 
import math

# Input
vanligaKorvar2 = int(input("Hur många vill ha 2 vanliga korvar?: "))
vanligaKorvar3 = int(input("Hur många vill ha 3 vanliga korvar?: "))
veganskaKorvar2 = int(input("Hur många vill ha 2 veganska korvar?: "))
veganskaKorvar3 = int(input("Hur många vill ha 3 vegansak korvar?: "))

# Totalt antal korv & dryck
antalDryck = vanligaKorvar2 + vanligaKorvar3 + veganskaKorvar2 + veganskaKorvar3
antalVanligaKorvar = (vanligaKorvar2 * 2) + (vanligaKorvar3 * 3)
antalVeganskaKorvar = (veganskaKorvar2 * 2) + (veganskaKorvar3 * 3)
#print(antalVanligaKorvar)
#print(antalVeganskaKorvar)

# antal korvförpackningar
vanligaKorvFörpackningar = math.ceil(antalVanligaKorvar/8)
VeganskaKorvFörpackningar = math.ceil(antalVeganskaKorvar/8)

# priser
prisVanligKorvFörpackning = 20.95
prisVeganskKorvFörpackning = 34.95
prisDryck = 13.95

# Utmatning
print("------KORVKOLLEN------------")
print("-----------------------------------")
print("Hur Många Elever Vill Ha...")
print("2 Vanliga Krovar", vanligaKorvar2)
print("3 Vanliga Korvar ", vanligaKorvar3 )
print("2 Veganska Korvar ", veganskaKorvar2)
print("3 Veganska Korvar ", veganskaKorvar3)
print("-----------------------------------")
print("- INKÖPSLISTA -")
print("Vanlig Korv:", vanligaKorvFörpackningar, "förpackningar.")
print("Vegansk Korv:", VeganskaKorvFörpackningar, "förpackningar.")
print("Dryck: ", antalDryck, "drickor")
print("-----------------------------------")
print((vanligaKorvFörpackningar*prisVanligKorvFörpackning) + (VeganskaKorvFörpackningar*prisVeganskKorvFörpackning) + (antalDryck*prisDryck))