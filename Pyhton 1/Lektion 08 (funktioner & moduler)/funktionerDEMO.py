# Anropa modulerna i filen utils.py
import utils

numbers = [6, 5, 2, 3, 4, 6, 7, 8, 9, 10]


def minimum(list):
    if list:
        return min(list)
    else:
        return None


def greet(firstname, lastname=''):
    print(f"Hello {firstname} {lastname}")


# använd greet-modulen från utils.py
utils.greet("Viggo")
