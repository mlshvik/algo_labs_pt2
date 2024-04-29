import unittest
from src.gorilla_and_bananas import JackiesBananas


class TestForMonkey(unittest.TestCase):
    def test_find_min_bana(self):
        self.assertEqual(JackiesBananas([3, 6, 7, 11], 8), 4)

    def test_find_min_bana1(self):
        self.assertEqual(JackiesBananas([30, 11, 23, 4, 20], 5), 30)

    def test_find_min_bana2(self):
        self.assertEqual(JackiesBananas([30, 11, 23, 4, 20], 6), 23)




