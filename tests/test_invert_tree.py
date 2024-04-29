import unittest
from invert_tree import BinaryTree, MirrorTree

class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        self.root = BinaryTree(1)
        self.root.left = BinaryTree(2)
        self.root.right = BinaryTree(3)
        self.root.left.left = BinaryTree(4)
        self.root.left.right = BinaryTree(5)
        self.root.right.left = BinaryTree(6)
        self.root.right.right = BinaryTree(7)

    def test_inverting_tree(self):

        mirror_tree = MirrorTree()

        mirror_tree.invert_binary_tree(self.root)
        self.assertEqual(self.root.val, 1)
        self.assertEqual(self.root.left.val, 3)
        self.assertEqual(self.root.right.val, 2)
        self.assertEqual(self.root.left.left.val, 7)
        self.assertEqual(self.root.left.right.val, 6)
        self.assertEqual(self.root.right.left.val, 5)
        self.assertEqual(self.root.right.right.val, 4)

if __name__ == '__main__':
    unittest.main()
