#!/usr/bin/python3
'''function that writes a string to a text file (UTF8) and returns the number of characters written'''


def write_file(filename="", text=""):
    # Open the file using the 'with' statement.
    with open(filename, mode='w', encoding='utf-8') as f:
        # Write the text content to the file.
        nb_characters = f.write(text)

    # The f.write() method returns the number of characters written.
    return nb_characters
