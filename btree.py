class NodeBT:
    def __init__(self, leaf=False):
        self.keys = []  # array of keys
        self.children = []  # array of children
        self.leaf = leaf  # boolean attribute


class BTree:
    def __init__(self, t):
        self.root = NodeBT(True)
        self.t = t  # minimun tree degree
        self.nodes_read = 0  # counter read nodes
        self.nodes_written = 0  # counter written node

    def read_node(self, node):
        self.nodes_read += 1
        return node

    def write_node(self, node):
        self.nodes_written += 1

    def search(self, key):
        """
        Find the key inside B tree from the root through recursive call
        """
        self.nodes_read = 0  # reset counter when we start a new search
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):

        # read current node
        if node != self.root:
            self.read_node(node)

        # Find key's position inside the node
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1

        # key founded, return node with key's index
        if i < len(node.keys) and key == node.keys[i]:
            return node, i

        # If the node is a leaf, then the search failed because there is no such key
        if node.leaf:
            return None

        # otherwise search inside proper son
        return self._search_recursive(node.children[i], key)

    def insert(self, k):
        # reset counter when we start each new insert operation
        self.nodes_read = 0
        self.nodes_written = 0
        return self.insert_rec(k)

    def insert_rec(self, k):  # k: key to insert
        t = self.t
        root = self.root

        # if root is full, create a new node ---> tree's height grows by 1
        if len(root.keys) == (2 * t) - 1:  # if the root is full then the tree
            # height must increase
            new_root = NodeBT()  # a new empty node will be the new root
            self.root = new_root  # update the reference to the root
            new_root.children.insert(0, root)  # the old root become the first
                                               # new root's child

            self.split_child(new_root, 0)  # calling this method we'll have
                                           # the median key moving to the new root
            # self.write_node(new_root)

            self.insert_non_full(new_root, k)  # the new root necessarily will be
                                               # non full, hence is possible
                                               # insert the key without further
                                               # divisions
        else:  # the root is non full
            self.insert_non_full(root, k)

    def split_child(self, x, i):  # when a node is full, i.e. contains the max
                                  # number of possible keys, then I have to call
                                  # this method in order to preserve the b-tree
                                  # property, splitting the current node
        t = self.t

        y = x.children[i]  # y is a full child of x
                           # hence y is node to split

        # self.read_node(y)

        # create a new node and add it to x's list of children
        z = NodeBT(y.leaf)  # if y was a leaf then z has to maintain the same
                            # state

        x.children.insert(i + 1, z)  # we have to append a new child to the x's
                                     # children list

        # insert the median of the full child y into x
        x.keys.insert(i, y.keys[t - 1])  # we extract the median key of y, then
                                         # it is added to node x

        # split apart y's keys into y & z
        z.keys = y.keys[t: (2 * t) - 1]  # all the right keys of y are moved in z
        y.keys = y.keys[0: t - 1]  # all the left keys of y remain in y

        # if y is not a leaf, we reassign y's children to y & z
        if not y.leaf:
            z.children = y.children[t: 2 * t]  # we reassign y's children placed
                                               # at the right of median key to
                                               # z node
            y.children = y.children[0: t]  # y's children placed at the left of
                                           # median key remain in y

        self.write_node(y)
        self.read_node(z)
        self.write_node(x)

    def insert_non_full(self, x, k):
        t = self.t
        i = len(x.keys) - 1  # i is equal to the index of the last key of x, in
                             # order to move backward for founding the correct
                             # spot of insert

        # self.read_node(x)

        # find the correct spot in the leaf to insert the key
        if x.leaf:
            x.keys.append(None)  # append a null spot for the new key
            while i >= 0 and k < x.keys[i]: # we move backward
                x.keys[i + 1] = x.keys[i]  # moving current key one spot to the
                                           # right to make room for k
                i -= 1  # moving backward
            x.keys[i + 1] = k  # assign k to the correct spot

            self.write_node(x)

        # if x is not a leaf, find the correct subtree to insert the key
        else:
            while i >= 0 and k < x.keys[i]:
                i -= 1
            i += 1  # increase i in order to obtain correct index that reference
                    # the child where go down

            self.read_node(x.children[i])

            # if child node is full, split it
            if len(x.children[i].keys) == (2 * t) - 1:
                self.split_child(x, i)  # this method move the median key in x,
                                        # then divide the child
                self.write_node(x.children[i])
                if k > x.keys[i]:  # after division, if the k is greater than
                                   # median key just added in x, the insert must
                                   # go on the right subtree
                    i += 1  # increase i means move to the new child

            self.insert_non_full(x.children[i], k)  # recursive call on the
                                                    # correct subtree

    def delete(self, x, k):
        # reset counters for every new delete operation
        self.nodes_read = 0
        self.nodes_written = 0
        self.delete_rec(x, k)

    def delete_rec(self, x, k):  # k: key to delete
        t = self.t
        i = 0  # index used to scan x's keys

        if x != self.root:
            self.read_node(x)

        while i < len(x.keys) and x.keys[i] is not None and k > x.keys[i]:
            # scan keys to find k's position
            i += 1

        if x.leaf:  # case 1: deleting key from a leaf
                    # (means that I have achived lower level of the tree)
            self.write_node(x)
            if i < len(x.keys) and x.keys[i] == k:
                x.keys.pop(i)  # delete k directly from leaf node
                               # write node after deletion
            return  # end method here for leaf deletion

        if i < len(x.keys) and x.keys[i] == k:  # case 2: delete from internal node
            return self.delete_internal_node(x, k, i)

        # case 3a: child has enough keys to avoid deficit
        elif i < len(x.children) and len(x.children[i].keys) >= t:
            self.delete_rec(x.children[i], k)

        else:  # rebalancing child node with siblings
            if 0 < i < len(x.children) - 1: # or in ohter word
                                            # i > 0 and i < len(x.children) - 1:
                if len(x.children[i - 1].keys) >= t:  # rebalance with left sibling
                    self.read_node(x.children[i - 1])
                    self.delete_sibling(x, i, i - 1)
                elif len(x.children[i + 1].keys) >= t:  # rebalance with right sibling
                    self.read_node(x.children[i + 1])
                    self.delete_sibling(x, i, i + 1)
                else:  # if neither sibling has enough keys
                    self.read_node(x.children[i + 1])
                    self.delete_merge(x, i, i + 1)

            elif i == 0:  # rebalance with right sibling if i is the first child
                if len(x.children[i + 1].keys) >= t:
                    self.read_node(x.children[i + 1])
                    self.delete_sibling(x, i, i + 1)
                else:
                    self.read_node(x.children[i + 1])
                    self.delete_merge(x, i, i + 1)

            elif i == len(x.children) - 1:  # rebalance with left sibling if i is last child
                if len(x.children[i - 1].keys) >= t:
                    self.read_node(x.children[i - 1])
                    self.delete_sibling(x, i, i - 1)
                else:
                    self.read_node(x.children[i - 1])
                    self.delete_merge(x, i, i - 1)

            # Recursive delete on child node after rebalancing
            if i < len(x.children):  # Check if child index is still valid
                self.delete_rec(x.children[i], k)

    def delete_internal_node(self, x, k, i):  # method for deleting key k from
                                              # internal node x at position i
        t = self.t
        if x.leaf:
            if x.keys[i] == k:
                x.keys.pop(i)
            self.write_node(x)
            return

        if len(x.children[i].keys) >= t:  # case 2a: left child has at least t
                                          # keys

            # substitute k with predecessor key, i.e. the greater key of left
            # subtree
            self.read_node(x.children[i])
            x.keys[i] = self.delete_predecessor(x.children[i])
            self.write_node(x)
            return

        elif len(x.children[i + 1].keys) >= t:  # case 2b: right child has at
                                                # least t keys

            # substitute k with successor key, i.e. the minor key of right
            # subtree
            self.read_node(x.children[i])
            x.keys[i] = self.delete_successor(x.children[i + 1])
            self.write_node(x)
            return

        else:  # case 2c: both child have t-1 keys
            self.delete_merge(x, i, i + 1)  # unite the two child
            self.delete_internal_node(x.children[i], k, self.t - 1)

    def delete_predecessor(self, x):  # this method remove and return the
                                      # predecessor of x , i.e. the greater key
                                      # of left subtree
        if x.leaf:
            self.write_node(x)
            return x.keys.pop()  # if x is a leaf then predecessor is the last
                                 # element of array keys

        n = len(x.keys) - 1  # n is the index of the last key in x (the greater
                             # key of the node)
        self.read_node(x.children[n])
        if len(x.children[n].keys) >= self.t:  # if right child of x has at least
                                               # t keys

            self.delete_sibling(x, n + 1, n)  # then we can borrow a key from
                                              # sibling and balance the tree
        else:  # the sibling has no sufficient keys to balance
            self.delete_merge(x, n, n + 1)  # hence we have to union the two
                                            # children

        self.delete_predecessor(x.children[n])  # recursive call

    def delete_successor(self, x):  # this method remove and return the
                                    # successor of x, i.e. the minor key of the
                                    # right subtree
        if x.leaf:
            self.write_node(x)
            return x.keys.pop(0)  # if x is leaf node, then successor is simply
                                  # the minor key of x

        self.read_node(x.children[1])
        if len(x.children[1].keys) >= self.t:  # if the left child of x (that
                                               # contains his successor) has at
                                               # least t keys
            self.delete_sibling(x, 0, 1)  # then we have to balance x with left
                                          # sibling

        else:  # if the left child has no enough keys
            self.delete_merge(x, 0, 1)  # union of the two children

        self.read_node(x.children[0])
        self.delete_successor(x.children[0])  # recursive call

    # this following method is used to fusion two children nodes (i,j) of x when one or
    # both have minus of t-1 keys. This fusion is necessarily in order to
    # preserve structural properties of b-tree
    def delete_merge(self, x, i, j):
        cnode = x.children[i]  # left child of x
        self.write_node(x.children[i])
        self.write_node(x.children[j])

        if j > i:  # then i is the left child of x and j is the right child
            rsnode = x.children[j]  # right child of x
            cnode.keys.append(x.keys[i])

            for k in range(len(rsnode.keys)):  # scan all right child's keys
                cnode.keys.append(rsnode.keys[k])  # add every key of right child
                                                   # to left child
                if len(rsnode.children) > 0:  # verify if right child has child,
                                              # i.e. it is not a leaf
                    cnode.children.append(rsnode.children[k])  # if true then
                                                               # we add every
                                                               # child to left
                                                               # child
            if len(rsnode.children) > 0:
                # last child of right child j become last child of left child i
                cnode.children.append(rsnode.children.pop())

            new = cnode  # new fusion node
            x.keys.pop(i)  # key that is moved to left child it is removed from
                           # parent x
            x.children.pop(j)  # right child (x.children[j]) is removed from x
                               # because it is fused with left child

        else:  # this block manages the union with right child, hence it is
               # symmetric to the previous block
            lsnode = x.children[j]
            lsnode.keys.append(x.keys[j])
            for i in range(len(cnode.keys)):
                lsnode.keys.append(cnode.keys[i])
                if len(lsnode.children) > 0:
                    lsnode.children.append(cnode.children[i])
            if len(lsnode.children) > 0:
                lsnode.children.append(cnode.children.pop())
            new = lsnode
            x.keys.pop(j)
            x.children.pop(i)

        if x == self.root and len(x.keys) == 0:
            self.root = new

    # this method is necessarily to rebalance the b-tree when a node has less
    # than t-1 keys (t is order of the tree). delete_sibling() borrows a key
    # from sibling node in order to preserve the properties of the b-tree
    def delete_sibling(self, x, i, j):  # x: parent node
                                        # i: index of the current child of x
                                        # j: index of the child of x that borrows
                                        #    a key
        cnode = x.children[i]  # cnode now needs a key
        self.write_node(x.children[i])
        self.write_node(x.children[j])

        if i < j:  # then j node is on the right respect child i
            rsnode = x.children[j]  # rsnode reference to right sibling
            cnode.keys.append(x.keys[i])  # add to the current node the key of
                                          # parent x at particular index i
            x.keys[i] = rsnode.keys[0]  # the first key of right sibling is moved
                                        # to the position of that key of x just
                                        # shifted to the current node
            if len(rsnode.children) > 0:  # means that rsnode is not a leaf
                cnode.children.append(rsnode.children[0])  # the first child of
                                                           # rsnode is moved as
                                                           # current node (we
                                                           # just are moving a
                                                           # subtree from rsnode
                                                           # to cnode)

                rsnode.children.pop(0)  # removing first child of rsnode that
                                        # just moved
            rsnode.keys.pop(0)  # removing the first key of rsnode, which it is
                                # moved to parent x; now rsnode has one less key
                                # and cnode is been rebalanced
        else:  # in this block it is reported the code for the symmetric
               # scenario, i.e. when j node is on the left respect child i
            lsnode = x.children[j]
            cnode.keys.insert(0, x.keys[i - 1])
            x.keys[i - 1] = lsnode.keys.pop()
            if len(lsnode.children) > 0:
                cnode.children.insert(0, lsnode.children.pop())

    def print_tree(self, x, level=0):
        print(f'Level {level}', end=": ")

        for i in x.keys:
            print(i, end=" ")

        print()
        level += 1

        if len(x.children) > 0:
            for i in x.children:
                self.print_tree(i, level)
