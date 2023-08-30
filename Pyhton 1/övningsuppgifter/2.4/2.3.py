"""
vningsuppgift 2.3. Konstruera ett program d¨ar anv¨andaren i dialog med
datorn ger sitt f¨or- och efternamn. Datorn ska avsluta k¨orningen med att h¨alsa
p˚a anv¨andaren enligt exemplet nedan:
dator > Hall ˚a !
dator > Vad ¨a r ditt f ¨o rnamn ?
du > Johan
dator > Vad ¨a r ditt efternamn ?
du > Svensson
dator > Trevligt att tr ¨a ffas Johan Svensson !
"""

print("Hello")
firstName = input("Vad är ditt namn?: ")
lastName = input("Vad är dit efternamn?: ")
print("Trevligt att träffas ", firstName , lastName)