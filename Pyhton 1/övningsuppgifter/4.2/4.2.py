multiplication_tables = float(input("Ange multiplicationstabell >"))




for x in range(1, 11):
    results = multiplication_tables * x
    print(results)
    user_input = input("Continue? y/n")
    if user_input != "y":
        break
