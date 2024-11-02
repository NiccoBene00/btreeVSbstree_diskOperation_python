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
