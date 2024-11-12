#!/usr/bin/python3
"""
Module to read a text file (UTF8) and print its content to stdout.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (str): Defaults to an empty string.
    """
    # Using the 'with' statement to ensure proper file handling
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content, end="")
