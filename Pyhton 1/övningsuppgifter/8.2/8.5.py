todos = [
    'Städa',
    'Handla',
    'Plugga',
    'Ge blod']
found = False
print(todos)
indata = input('Ange todo: ').capitalize()
for i in todos:
    if i == indata:
        print(f'{indata} finns i listan')
        found = True
        break
if not found:
    print(f'{indata} finns inte i listan.')
    answer = input('Vill du lägga till den (y/n)? ').lower()
    if answer == "y":
        todos.append(indata)
        print('Todo tillagd!')
    else:
        print(f'{indata} inte tillagd!')
print(todos)


