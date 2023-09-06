indata = input("ange en text: ")
letter = input("ange bosktav du vill kontrollera i texten: ").lower()
count = 0
index = 0
while index < len(indata):
    if indata[index].lower() == letter:
        count += 1
    index += 1
print(f"Bokstaven {letter} förekommer {count} gånger i texten")
