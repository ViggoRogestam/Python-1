multiplication_tables = float(input("Ange multiplicationstabell >"))

for x in range(1, 11, 3):
    results = multiplication_tables * x
    print(results)
    second_result = multiplication_tables * (x + 1)
    print(second_result)
    third_result = multiplication_tables * (x + 2)
    print(third_result)
    user_input = input("Continue? y/n >").lower()
    if user_input != "y":
        break
