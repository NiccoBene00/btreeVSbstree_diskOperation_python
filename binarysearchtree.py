class BSTree:
    nodes_read = 0
    nodes_written = 0

    def __init__(self, val=None):
        # Initialize a tree node with a value
        self.value = val
        if self.value:
            # If a value is provided,
            #create left and right children as empty trees
            self.left = BSTree()
            self.right = BSTree()
        else:
            # If no value is provided, set left and
            #right children to None
            self.left = None
            self.right = None

        BSTree.nodes_written += 1

    def isempty(self):
        # Check if the tree node is empty
        return self.value == None

    def isleaf(self):
        # Check if the tree node is a leaf node (both left and right
        # children are None)
        if self.left.left == None and self.right.right == None:
            return True
        else:
            return False

    def insert(self, data):


        BSTree.nodes_read += 1  # Read current node to check if it's empty

        if self.isempty():
            # If the current node is empty,
            #insert the data as its value
            self.value = data
            # Create empty left and right children
            self.left = BSTree()
            self.right = BSTree()

            BSTree.nodes_written += 1 # current node written

        elif self.value == data:
            # If the data already exists in the tree, return
            return
        elif data < self.value:
            # If the data is less than the current node's value,
            #insert it into the left subtree

            BSTree.nodes_read += 1 # Reading left child node

            self.left.insert(data)
            return
        elif data > self.value:
            # If the data is greater than the current node's value,
            #insert it into the right subtree

            BSTree.nodes_read += 1  # Reading right child node

            self.right.insert(data)
            return

    def search(self, v):

        BSTree.nodes_read += 1  # Read current node to check its value


        if self.isempty():
            # If the tree is empty, the value is not found
            #print("{} is not found".format(v))
            return False
        if self.value == v:
            # If the value is found at the current node,
            #print a message and return True
            #print("{} is found".format(v))
            return True
        if v < self.value:
            # If the value is less than the current node's value,
            #search in the left subtree
            return self.left.search(v)
        else:
            # If the value is greater than the current node's value,
            #search in the right subtree
            return self.right.search(v)

    def inorder(self):
        if self.isempty():
            # If the tree is empty, return an empty list
            return []
        else:
            # Return the inorder traversal of the tree (left subtree,
            # root, right subtree)
            return self.left.inorder() + [self.value] + self.right.inorder()

    def maxval(self):

        BSTree.nodes_read += 1  # Reading current node


        # Find the maximum value in the Tree
        if self.right.right == None:
            return (self.value)
        else:
            return (self.right.maxval())

    def delete(self, v):

        BSTree.nodes_read += 1  # Reading current node to check its value

        # Delete a value from the Tree
        if self.isempty():
            return
        if v < self.value:
            self.left.delete(v)
            return
        if v > self.value:
            self.right.delete(v)
            return
        if v == self.value:
            if self.isleaf():
                self.value = None
                self.left = None
                self.right = None
                return

            elif self.left.isempty():
                self.value = self.right.value
                self.left = self.right.left
                self.right = self.right.right

                BSTree.nodes_written += 1  # Writing updated node value and children

                return
            else:
                self.value = self.left.maxval()
                self.left.delete(self.left.maxval())

                BSTree.nodes_written += 1  # Writing updated node value

                return

    @classmethod
    def get_nodes_read(cls):
        """Return total number of read nodes."""
        return cls.nodes_read

    @classmethod
    def get_nodes_written(cls):
        """Return total number of written nodes."""
        return cls.nodes_written