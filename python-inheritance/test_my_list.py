import unittest
from 1-my_list import MyList  # Import MyList from your script

class TestMyList(unittest.TestCase):
    """Test the MyList class."""

    def test_print_sorted(self):
        """Test that print_sorted() prints the list in ascending order."""
        my_list = MyList([3, 1, 4, 2, 5])
        with self.assertLogs() as captured:
            my_list.print_sorted()
        self.assertIn("[1, 2, 3, 4, 5]", captured.output[0])

    def test_empty_list(self):
        """Test print_sorted on an empty list."""
        my_list = MyList()
        with self.assertLogs() as captured:
            my_list.print_sorted()
        self.assertIn("[]", captured.output[0])

    def test_already_sorted(self):
        """Test print_sorted on a list that's already sorted."""
        my_list = MyList([1, 2, 3, 4, 5])
        with self.assertLogs() as captured:
            my_list.print_sorted()
        self.assertIn("[1, 2, 3, 4, 5]", captured.output[0])

if __name__ == '__main__':
    unittest.main()
