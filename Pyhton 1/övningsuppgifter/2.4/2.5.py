"""
Ovningsuppgift 2.5. Konstruera ett program i vilken en anv¨andare matar in
fem heltal. Avg¨or med den matematiska standardfunktionen max det h¨ogsta
inmatade talet och presentera detta f¨or anv¨andaren.
Ange tal :
a = 1
b = 9
c = 2
d = 6
e = 5
Det h ¨o gsta inmatade heltalet ¨a r 9.
"""
a = int(input("Mata in ett tal: "))
b = int(input("Mata in ett tal: "))
c = int(input("Mata in ett tal: "))
d = int(input("Mata in ett tal: "))
e = int(input("Mata in ett tal: "))
maximum = max(a, b, c, d, e)
print(maximum)