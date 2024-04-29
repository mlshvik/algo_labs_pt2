import unittest
from src.trie_node import Trie

class TestTrie(unittest.TestCase):

    def setUp(self):
        self.trie = Trie()

    def test_insert_and_search(self):
        self.trie.insert("apple")
        self.assertTrue(self.trie.search("apple"))
        self.assertFalse(self.trie.search("app"))
        self.assertFalse(self.trie.search("ap"))
        self.assertFalse(self.trie.search("banana"))

    def test_starts_with(self):
        self.trie.insert("apple")
        self.trie.insert("app")
        self.trie.insert("banana")

        self.assertTrue(self.trie.starts_with("a"))
        self.assertTrue(self.trie.starts_with("ap"))
        self.assertTrue(self.trie.starts_with("app"))
        self.assertTrue(self.trie.starts_with("appl"))
        self.assertTrue(self.trie.starts_with("apple"))
        self.assertTrue(self.trie.starts_with("b"))
        self.assertTrue(self.trie.starts_with("ba"))
        self.assertTrue(self.trie.starts_with("ban"))
        self.assertTrue(self.trie.starts_with("bana"))
        self.assertTrue(self.trie.starts_with("banan"))
        self.assertTrue(self.trie.starts_with("banana"))

    def tearDown(self):
        self.trie = None

if __name__ == '__main__':
    unittest.main()
