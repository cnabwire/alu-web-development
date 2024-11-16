#!/usr/bin/python3
"""7-add_item.py
   A script that adds all arguments to a Python list,
   and then saves them to a file.
"""


import sys
from os import path

# Importing the save_to_json_file and load_from_json_file functions
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

if __name__ == "__main__":
    file_path = "add_item.json"

    # Load the existing list from the file if it exists
    if path.exists(file_path):
        try:
            list_obj = load_from_json_file(file_path)
        except ValueError:
            list_obj = []
    else:
        list_obj = []

    # Add command-line arguments to the list
    list_obj.extend(sys.argv[1:])

    # Save the updated list to the file
    save_to_json_file(list_obj, file_path)
