car_colors = {}

while True:
    
    color = input('Car color > ')
    if color not in car_colors:
        car_colors[color] = 0 
    
    car_colors[color] += 1
    
    print('-----')
    print(f'You have seen {car_colors[color]} {color} cars!')
    print('-----')