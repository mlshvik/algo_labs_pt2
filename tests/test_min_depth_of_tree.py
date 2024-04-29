import unittest
from src.min_depth_of_tree_ import min_depth

class TestMinDepth(unittest.TestCase):
    def test_min_depth_empty_graph(self):
        graph = []
        root = None
        self.assertEqual(min_depth(root, graph), 1)

    def test_min_depth_single_node(self):
        graph = [(1, None)]
        root = 1
        self.assertEqual(min_depth(root, graph), 2)

    def test_min_depth_balanced_tree(self):
        graph = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7)]
        root = 1
        self.assertEqual(min_depth(root, graph), 3)

    def test_min_depth_unbalanced_tree(self):
        graph = [(1, 2), (1, 3), (2, 4), (2, 5), (4, 6)]
        root = 1
        self.assertEqual(min_depth(root, graph), 2)

    def test_min_depth_disconnected_graph(self):
        graph = [(1, 2), (1, 3), (4, 5), (4, 6)]
        root = 1
        self.assertEqual(min_depth(root, graph), 2)

if __name__ == '__main__':
    unittest.main()
