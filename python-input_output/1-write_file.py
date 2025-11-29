#!/usr/bin/python3
"""
1-write_file.py

A function that writes a string to a text file (UTF8) and returns
the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file, creating it if it doesn't exist,
    or overwriting it if it does.

    The file is opened in 'w' (write) mode with UTF-8 encoding.

    Args:
        filename (str): The name of the file to write to. Defaults to "".
        text (str): The string content to write to the file. Defaults to "".

    Returns:
        int: The number of characters successfully written to the file.
    """
    # Open file in 'w' (write/overwrite) mode with UTF-8 encoding.
    with open(filename, mode='w', encoding='utf-8') as f:
        # Write the text and capture the number of characters written.
        nb_characters = f.write(text)

    # Return the character count.
    return nb_characters
