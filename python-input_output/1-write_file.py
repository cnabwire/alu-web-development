#!/usr/bin/python3
"""3-write_file.py
"""


def write_file(filename="", text=""):
    """ writes a string to a text file """

    with open(filename, 'w', encoding="utf-8") as f_obj:
        return f_obj.write(text)
