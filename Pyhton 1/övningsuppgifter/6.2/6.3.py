# Är meningen en plaindrome

"""def isPalindrome(string): #Skapar en ny funktion som avgör om strängen är en palindrome
    if (string == string[::-1]):
        return "The string is a palindrome."
    else:
        return "The string is not a palindrome."""

indata = input("Mata in en mening: ")
new_string = indata.replace(" ", "").lower() # Tar bort mellanslag och stora bokstäver
if new_string == new_string[::-1]: # Jämför om strängen blir samma sträng baklänges
    print(f'{indata} är en palindrom.')
else:
    print(f'{indata} är inte en palindrom.')
