class TrieNode:
    def __init__(self):
        self.childNodes = {}
        self.isWordEnd = False

class Trie: 
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr_node = self.root
        for ch in word:
            node = curr_node.childNodes.get(ch, TrieNode())
            curr_node.childNodes[ch] = node
            curr_node = node

        curr_node.isWordEnd = True

    def search(self, word: str) -> bool:
        curr_node = self.root
        for ch in word:
            node = curr_node.childNodes.get(ch)
            if not node:
                return False
            curr_node = node

        return curr_node.isWordEnd


    def starts_with(self, prefix: str) -> bool:
        currNode = self.root
        for ch in prefix:
            node = currNode.childNodes.get(ch) 
            if not node:
                return False
            currNode = node

        return True