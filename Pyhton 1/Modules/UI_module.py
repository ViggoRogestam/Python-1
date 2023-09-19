# Variables
ui_width = 50


# prints out a line of dashes or stars depending on if dots is True or False
def line(dots=False):
    # if dots is True, print a line of stars
    if dots:
        print("*" * ui_width)
    # if dots is False, print a line of dashes
    else:
        print("-" * ui_width)


# prints out a header with the text centered in the middle of the line
def header(text):
    # formats the text to be centered
    formated_text = text.center(ui_width)
    # adds a border to the text
    bordered_text = f"|{formated_text}|"
    print(bordered_text)


# prints out a text with a border on the left side
def echo(text):
    print(f'| {text}')


# gets input from the user and returns it
def prompt(choice):
    return input(f'| {choice} > ')


def clear():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
