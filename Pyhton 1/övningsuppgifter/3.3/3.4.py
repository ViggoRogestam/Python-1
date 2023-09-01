country = str(input("Enter a country >"))
country = country.capitalize()
norden = ["Sverige", "Finland", "Norge", "Danmark", "Island"]
storbritanien = ["England", "Nordirland", "Skottland", "Wales"]
if country in norden:
    print("Landet ligger i Norden.")
elif country in storbritanien:
    print("Landet ligger i Storbritanien")
else:
    print("Error: landet tillhör varken Norden eller Storbritanien.")   