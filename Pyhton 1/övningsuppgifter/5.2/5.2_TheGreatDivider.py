# The Great Divider

# Layout
ui_width = 30
print(ui_width * "*")
print("THE GREAT DIVIDER".center(ui_width))
print(ui_width * "-")
print("Beräknar c för uttrycket: ".center(ui_width))
print()
print("a / b = c".center(ui_width))
print()
print(ui_width * "-")

# variabler och matte
a = 0
b = 0
try:
    a = float(input("Enter value for a >"))
    b = float(input("Enter value for b >"))

    c = a / b  
    if a == 0: # Om b är noll kommer ZeroDivisionError att utlösa här
        raise ZeroDivisionError("ERROR: division with zero")

except ValueError:
    print("ERROR: invalid number.")
except ZeroDivisionError:
    print("ERROR: division with zero")

else:
    print(a, "/", b, "=", c)

finally:
    print("Programmet avslutas.")
