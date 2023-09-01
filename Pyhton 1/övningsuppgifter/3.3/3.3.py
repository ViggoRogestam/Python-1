import random
dice = random . randint (1 , 6)
if dice == 1:
    print("""
 Du slog 1!
|----------|
|          |
|     X    |
|          |
|----------|
""")
elif dice == 2:
    print("""
 Du slog 2!
|----------|
|        X |
|          |
| X        |
|----------|          
 """)
    
elif dice == 3:
    print("""
 Du slog 3!
|----------|
|        X |
|     X    |
| X        |
|----------|        
""")
    
elif dice == 4:
    print("""
  Du slog 4!
|----------|
| X      X |
|          |
| X      X |
|----------|       
""")
    
elif dice == 5:
    print("""
  Du slog 5!
|----------|
| X      X |
|     X    |
| X      X |
|----------|         
""")
    
elif dice == 6:
    print("""
  Du slog 6!
|----------|
|  X    X  |
|  X    X  |
|  X    X  |
|----------|        
""")



