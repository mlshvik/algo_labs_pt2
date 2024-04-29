import unittest
from vai_vu_lab6 import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_count_cross_tribe_pairs(self):
        pairs = [
            [1, 2],
            [2, 4],
            [3, 5]
        ]
        self.assertEqual(self.solution.number_of_pairs(3, pairs), 4)

    def test_count_cross_tribe_pairs2(self):
        pairs = [
            [1, 2],
            [2, 4],
            [1, 3],
            [3, 5],
            [8, 10]
        ]
        self.assertEqual(self.solution.number_of_pairs(5, pairs), 4)

    def test_count_cross_tribe_pairs3(self):
        pairs = [
            [1, 2],
            [3, 4],
            [5, 6],
            [7, 8],
            [2, 3]
        ]
        self.assertEqual(self.solution.number_of_pairs(5, pairs), 9)

if __name__ == '__main__':
    unittest.main()