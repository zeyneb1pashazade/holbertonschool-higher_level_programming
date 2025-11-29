#!/usr/bin/python3
"""
2-append_write.py

A function that appends a string at the end of a text file (UTF8) and returns
the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file, creating the file if it
    does not exist.

    The file is opened in 'a' (append) mode with UTF-8 encoding.

    Args:
        filename (str): The name of the file to append to. Defaults to "".
        text (str): The string content to append to the file. Defaults to "".

    Returns:
        int: The number of characters successfully added to the file.
    """
    # Open file in 'a' (append) mode with UTF-8 encoding.
    # 'a' mode ensures that new content is added to the end of the file.
    # If the file does not exist, it will be created.
    with open(filename, mode='a', encoding='utf-8') as f:
        # Write the text and capture the number of characters written.
        nb_characters_added = f.write(text)

    # Return the character count.
    return nb_characters_added
