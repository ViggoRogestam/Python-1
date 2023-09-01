""""
input_password = input("Enter Password: ")
password = "Hej123"
if(password == input_password):
    print("Correct Password")
else:
    print("Incorrect Password!")
 
    

team = "engineering"
if team == "content":
    print("This person comes from the content team.")
elif team == "engineering":
    print("This person comes from the engineering team.")
else:
    print("This person doesn't come from the content or engineering teams.")
    """
    
order = input("What would you like to order: pizza or hamburger? ")
if order == "hamburger":
    print("Thank you.")
    cheese = input("Do you want cheese?")
    if cheese == "yes":
        print("You got it.")
    else:
        print("No cheese it is.")
elif order == "pizza":
    print("Pizza coming up.")
    toppings = input("Do you want pepperoni on that yes/no?")
    if toppings == "yes":
        print("We will add pepperoni.")
    else:
        print("Your pizza will not have pepperoni.") 