todos = [
    'Städa',
    'Handla',
    'Plugga',
    'Ge blod']
print(todos)
indata = input('Ta bort todo (värde): ').capitalize()
todos.remove(indata)
print(todos)
