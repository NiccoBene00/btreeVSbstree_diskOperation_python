# class BSTree:
#     nodes_read = 0
#     nodes_written = 0
#
#     def __init__(self, val=None):
#         # Initialize a tree node with a value
#         self.value = val
#         if self.value:
#             # If a value is provided,
#             #create left and right children as empty trees
#             self.left = BSTree()
#             self.right = BSTree()
#         else:
#             # If no value is provided, set left and
#             #right children to None
#             self.left = None
#             self.right = None
#
#         BSTree.nodes_written += 1
#
#     def isempty(self):
#         # Check if the tree node is empty
#         return self.value == None
#
#     def isleaf(self):
#         # Check if the tree node is a leaf node (both left and right
#         # children are None)
#         if self.left.left == None and self.right.right == None:
#             return True
#         else:
#             return False
#
#     def insert(self, data):
#
#         BSTree.nodes_read += 1  # Read current node to check if it's empty
#
#         if self.isempty():
#             # If the current node is empty,
#             #insert the data as its value
#             self.value = data
#             # Create empty left and right children
#             self.left = BSTree()
#             self.right = BSTree()
#
#             BSTree.nodes_written += 1 # current node written
#
#         elif self.value == data:
#             # If the data already exists in the tree, return
#             return
#         elif data < self.value:
#             # If the data is less than the current node's value,
#             #insert it into the left subtree
#
#             BSTree.nodes_read += 1 # Reading left child node
#
#             self.left.insert(data)
#             return
#         elif data > self.value:
#             # If the data is greater than the current node's value,
#             #insert it into the right subtree
#
#             BSTree.nodes_read += 1  # Reading right child node
#
#             self.right.insert(data)
#             return
#
#     def search(self, v):
#
#         BSTree.nodes_read += 1  # Read current node to check its value
#
#
#         if self.isempty():
#             # If the tree is empty, the value is not found
#             #print("{} is not found".format(v))
#             return False
#         if self.value == v:
#             # If the value is found at the current node,
#             #print a message and return True
#             #print("{} is found".format(v))
#             return True
#         if v < self.value:
#             # If the value is less than the current node's value,
#             #search in the left subtree
#             return self.left.search(v)
#         else:
#             # If the value is greater than the current node's value,
#             #search in the right subtree
#             return self.right.search(v)
#
#     def inorder(self):
#         if self.isempty():
#             # If the tree is empty, return an empty list
#             return []
#         else:
#             # Return the inorder traversal of the tree (left subtree,
#             # root, right subtree)
#             return self.left.inorder() + [self.value] + self.right.inorder()
#
#     def maxval(self):
#
#         BSTree.nodes_read += 1  # Reading current node
#
#
#         # Find the maximum value in the Tree
#         if self.right.right == None:
#             return (self.value)
#         else:
#             return (self.right.maxval())
#
#     def delete(self, v):
#
#         BSTree.nodes_read += 1  # Reading current node to check its value
#
#         # Delete a value from the Tree
#         if self.isempty():
#             return
#         if v < self.value:
#             self.left.delete(v)
#             return
#         if v > self.value:
#             self.right.delete(v)
#             return
#         if v == self.value:
#             if self.isleaf():
#                 self.value = None
#                 self.left = None
#                 self.right = None
#                 return
#
#             elif self.left.isempty():
#                 self.value = self.right.value
#                 self.left = self.right.left
#                 self.right = self.right.right
#
#                 BSTree.nodes_written += 1  # Writing updated node value and children
#
#                 return
#             else:
#                 self.value = self.left.maxval()
#                 self.left.delete(self.left.maxval())
#
#                 BSTree.nodes_written += 1  # Writing updated node value
#
#                 return
#
#     @classmethod
#     def get_nodes_read(cls):
#         """Return total number of read nodes."""
#         return cls.nodes_read
#
#     @classmethod
#     def get_nodes_written(cls):
#         """Return total number of written nodes."""
#         return cls.nodes_written

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.nodes_read = 0
        self.nodes_written = 0

    def insert(self, key):
        self.nodes_read = 0
        self.nodes_written = 0

        if self.root is None:
            self.root = Node(key)
            self.nodes_written += 1
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        self.nodes_read += 1

        if key < node.key:
            if node.left is None:
                node.left = Node(key)
                self.nodes_written += 1
            else:
                self._insert_recursive(node.left, key)
        elif key > node.key:
            if node.right is None:
                node.right = Node(key)
                self.nodes_written += 1
            else:
                self._insert_recursive(node.right, key)

    def search(self, key):
        self.nodes_read = 0
        found = self._search_recursive(self.root, key)
        return found

    def _search_recursive(self, node, key):
        if node is None:
            return False

        self.nodes_read += 1

        if key == node.key:
            return True
        elif key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)

    def delete(self, key):
        self.nodes_read = 0
        self.nodes_written = 0
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, node, key):
        if node is None:
            return None

        self.nodes_read += 1  # read current node

        if key < node.key:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursive(node.right, key)
        else:
            # bingo
            if node.left is None:
                self.nodes_written += 1
                return node.right
            elif node.right is None:
                self.nodes_written += 1
                return node.left

            # node with two child: find inorder successor
            min_larger_node = self._find_min(node.right)
            node.key = min_larger_node.key
            self.nodes_written += 1  # update key
            node.right = self._delete_recursive(node.right, min_larger_node.key)

        if node is not None:
            self.nodes_written += 1  # write update node
        return node

    def _find_min(self, node):
        # find min in subtree (successor)
        while node.left is not None:
            self.nodes_read += 1  # read each visited node
            node = node.left
        self.nodes_read += 1  # read final node
        return node

    def print_tree(self):
        """Print the tree in a format with numbers and parentheses."""

        def _print_tree(node):
            if node is None:
                return ""
            left_part = _print_tree(node.left)
            right_part = _print_tree(node.right)
            result = f"({node.key}"
            if left_part or right_part:  # If there are children
                result += f"({left_part}{right_part})"
            return result

        # Start the recursive printing from the root
        return _print_tree(self.root)