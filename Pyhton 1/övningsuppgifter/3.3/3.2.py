
"""
Alder S¨omnbehov (per natt)
1 ˚ar 14 timmar
2 ˚ar 13 timmar
3 ˚ar 12 timmar
4 ˚ar 11,5 timmar
5-6 ˚ar 11 timmar
7 ˚ar 10,5 timmar
8-10 ˚ar 10 timmar
11 ˚ar 9,5 timmar
12 - 15 ˚ar 9 timmar
16 ˚ar 8,5 timmar
17+ ˚ar 8 timmar
"""


age = int(input("Enter age >"))
name = input("Enter name >")

sleep_table = {
 1: 15,
 2: 13,
 3: 12,
 4: 11.5,
 5: 11,
 6: 11,
 7: 10.5,
 8: 10,
 9: 10,
 10: 10,
 11: 9.5,
 12: 9,
 13: 9,
 14: 9,
 16: 8.5,
 17: 8,}
    
if int(age) in sleep_table:
    required_sleep = sleep_table[age]
    print("Hej", name,".", "Enligt vårdguidens rekomendationer behöver individer i din ålder", "("+str(age)+")", "sova minst", required_sleep, "timmar per natt")   
elif age > 17:
    print("Hej", str(name) + "." + " Enligt vårdguidens rekomendationer behöver individer i din ålder", "(" + str(age) + ")", "sova minst 8 timmar per natt")
else:
    print("Åldern du har matat in är ej giltig.")    
        
    
    
    
    
    
