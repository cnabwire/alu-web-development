import unittest
from 1_my_list import MyList  # Update to reflect your file naming

class TestMyList(unittest.TestCase):
    def test_print_sorted(self):
        """Test that print_sorted() prints the list in ascending order."""
        my_list = MyList([3, 1, 4, 2])
        self.assertEqual(my_list.print_sorted(), [1, 2, 3, 4])

if __name__ == '__main__':
    unittest.main()
