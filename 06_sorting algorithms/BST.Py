# Implementing binary search tree

# Creating the node class
# Create a node.
# Store the value in the node.
# Give the node a left pointer.
# Give the node a right pointer.
# # Initially, both pointers point to nothing because the node has no children.
class ProductNode:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.left = None
        self.right = None


# The BST Class
class BST:
    def __init__(self):
        self.root = None

    def insert(self, name, value):
        self.root = self._insert(self.root, name, value)

    def _insert(self, node, name, value):
        # base case
        if node is None:
            return ProductNode(name, value)

        # recursive case
        if value < node.value:
            node.left = self._insert(node.left, name, value)
        elif value > node.value:
            node.right = self._insert(node.right, name, value)
        else:
            return node
        return node

    # search
    def search(self, value):
        return self._search(self.root, value)

    def _search(self, node, value):
        if node is None:
            return None

        if value == node.value:
            return node

        if value < node.value:
            return self._search(node.left, value)

        else:
            return self._search(node.right, value)
