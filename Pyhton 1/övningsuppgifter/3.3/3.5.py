# Vilken kändis liknar du
""" Name        Gender  hair    eye
Daniel radcliff, male, "brown", "brown"
Rupert Grint,   male, "red",   "blue"
Emma Watson,   female, "brown", "brown"
Selena Gomez, female, "brown", "brown"
Johnny depp, male, "brown", "green"
Cameron Diaz, female, "blond", "blue"
Natalie Portman, female, "brown", "brown"
Orlando Bloom, male, black, "blue"
Scarlet Johansson, female, "blond", "green"

"""
gender = input("What is your gender >")
hair_color = input("What is your haircolor >")
eye_color = input("What is your eye color >")

if gender == "male":
    if hair_color == "brown":
        if eye_color == "brown":
            print("Egenskaperna matchar med: Daniel Radcliff")
        
        elif eye_color == "blue":
            print("Egenskaperna matchar med: ingen")
            
        elif eye_color == "green":
            print("Egenskaperna matchar med: Johnny depp")
            
        else: print("ingen")
    elif hair_color == "red":
        if eye_color == "blue":
            print("Egenskaperna matchar med: Rupert  Grint")
        
        else: print("Egenskaperna matchar med: ingen")    
    elif hair_color == "black":
        if eye_color == "blue":
            print("Egenskaperna matchar med: Orlando Bloom")
            
        else: print("Egenskaperna matchar med: ingen")
    else:
        print("Egenskaperna matchar med: ingen")

if gender == "female":
    if hair_color == "brown":
        if eye_color == "brown":
            print("Egenskaperna matchar med: Natalie Portman, Emma Watson, Selena Gomez")
            
    elif hair_color == "blond":
        if eye_color == "blue":
            print("Egenskaperna matchar med: Cameron Diaz")
            
        elif eye_color == "green":
            print("Egenskaperna matchar med: Scarlet Johansson")
    else: print("Egenskaperna matchar med: ingen")
        
    
    
    
    
    
    
    
    
    
    
