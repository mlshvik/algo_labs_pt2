class BinaryTree:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class MirrorTree:
    def invert_binary_tree(self, tree: BinaryTree) -> BinaryTree:
        if tree is None:
            return None

        self.invert(tree)

        return tree

    def invert(self, node):
        if not node:
            return

        self.invert(node.left)
        self.invert(node.right)

        node.left, node.right = node.right, node.left

        return node


