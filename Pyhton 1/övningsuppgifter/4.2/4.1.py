
biggest_number = float('-inf')
smallest_number = float('inf')
sum = 0
number_of_numbers = 0

while True:
    user_input = input("Mata in tal")
    user_input = int(user_input)
    if user_input < 0:
        break
    
    number_of_numbers += 1
    sum += user_input
    if user_input < smallest_number:
        smallest_number = user_input
    if user_input > biggest_number:
        biggest_number = user_input
        
if number_of_numbers > 0:
    avrage = sum / number_of_numbers
else: avrage = 0

print("Största tal:", biggest_number)
print("Minsta tal:", smallest_number)
print("Medelvärde:", avrage)
print("Summa:", sum)
