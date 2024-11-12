#!/usr/bin/python3


class MyList(list):
    """A class that inherits from list and adds a print_sorted method."""
    
    def print_sorted(self):
        """Prints the list in ascending sorted order, assuming all elements are integers."""
        if all(isinstance(i, int) for i in self):
            print(sorted(self))
        else:
            print("All elements must be integers.")
