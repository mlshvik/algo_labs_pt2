import unittest
import sys

sys.path.append("D:\\унік\\лаби\\k_element.py")
from src.k_element import find_kth_element

class TestFindKthElement(unittest.TestCase):

    def test_find_kth_element(self):
        self.assertEqual(find_kth_element([15, 7, 22, 9, 36, 2, 42, 18], 5), (18, 7))

    def test_find_kth_element_with_smaller_array(self):
        self.assertEqual(find_kth_element([15, 7, 22], 1), (22, 2))

    def test_find_kth_element_with_repeated_elements(self):
        self.assertEqual(find_kth_element([15, 15, 15, 15, 15], 2), (15, 0))



if __name__ == '__main__':
    unittest.main()