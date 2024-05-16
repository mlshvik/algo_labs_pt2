import unittest
from src.flower_shopss_ import *

class TestFlowerDelivery(unittest.TestCase):

    def setUp(self):
        self.test_data = {
            "test1.csv": [
                "F1 F2",
                "S1 S2",
                "F1 X1 10", "X1 X2 10", "X2 S1 10",
                "F2 X3 20", "X3 S2 20"
            ],
            "test2.csv": [
                "F1",
                "S1 S2",
                "F1 S1 15", "F1 S2 25"
            ],
            "test3.csv": [
                "F1 F2",
                "S1",
                "F1 S1 5", "F2 X1 10", "X1 S1 0"
            ],
            "test4.csv": [
                "F1 F2",
                "S1 S2",
                "F1 S1 30", "F1 S2 10", "F2 S1 5", "F2 S2 15"
            ],
            "test5.csv": [
                "F1 F2 F3",
                "S1",
                "F1 F2 10", "F2 F3 20", "F3 S1 30"
            ]
        }

        for filename, lines in self.test_data.items():
            with open(filename, 'w', newline='') as file:
                writer = csv.writer(file)
                for line in lines:
                    writer.writerow([line])

    def tearDown(self):
        for filename in self.test_data.keys():
            os.remove(filename)

    def test_maximum_flower_delivery(self):
        expected_results = {
            "test1.csv": 30,
            "test2.csv": 40,
            "test3.csv": 5,
            "test4.csv": 60,
            "test5.csv": 30
        }

        for filename, expected in expected_results.items():
            result = maximum_flower_delivery(filename)
            self.assertEqual(result, expected, f"Failed test with file {filename}")

if __name__ == "__main__":
    unittest.main()