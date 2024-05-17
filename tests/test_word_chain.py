import unittest
from src.word_chain import (Solution, read_input, write_output)
class TestWChain(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        words = ["a", "b", "ba", "bca", "bda"]
        expected_result = 3
        result = self.solution.longestStrChain(words)
        self.assertEqual(result, expected_result)

    def test_case_2(self):
        words = ["xbc", "bca", "b", "bc"]
        expected_result = 3
        result = self.solution.longestStrChain(words)
        self.assertEqual(result, expected_result)

    def test_case_3(self):
        words = ["a", "ab", "abc"]
        expected_result = 3
        result = self.solution.longestStrChain(words)
        self.assertEqual(result, expected_result)

    def test_case_4(self):
        words = ["a", "b", "ab", "ba", "abc", "cba"]
        expected_result = 3
        result = self.solution.longestStrChain(words)
        self.assertEqual(result, expected_result)

    def test_case_5(self):
        words = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa"]
        expected_result = 7
        result = self.solution.longestStrChain(words)
        self.assertEqual(result, expected_result)

    def test_case_6(self):
        words = ["a"]
        expected_result = 1
        result = self.solution.longestStrChain(words)
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
