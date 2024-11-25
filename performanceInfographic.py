import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import time

from btree import BTree
from binarysearchtree import BinarySearchTree


class PlotGenerator:

    def __init__(self):
        self.read_countsBST = []
        self.write_countsBST = []
        self.timesBST = []

        self.read_countsBT = []
        self.write_countsBT = []
        self.timesBT = []

    # method that measures time performance for each operation
    def measure_tree_performanceBST(self, bstree, keys, performance):
        self.read_countsBST = []
        self.write_countsBST = []
        self.timesBST = []

        for key in keys:
            start_time = time.perf_counter()  # time in sec

            if performance == "Insert":
                bstree.insert(key)
            elif performance == "Search":
                bstree.search(key)
            elif performance == "Delete":
                bstree.delete(key)

            end_time = time.perf_counter()
            self.timesBST.append(end_time - start_time)
            self.read_countsBST.append(bstree.nodes_read)
            self.write_countsBST.append(bstree.nodes_written)

        return sum(self.timesBST)


    def measure_tree_performanceBT(self, btree, keys, performance):
        self.read_countsBT = []
        self.write_countsBT = []
        self.timesBT = []

        for key in keys:
            start_time = time.perf_counter()  # time in sec

            if performance == "Insert":
                btree.insert(key)
            elif performance == "Search":
                btree.search(key)
            elif performance == "Delete":
                btree.delete(btree.root, key)

            end_time = time.perf_counter()
            self.timesBT.append(end_time - start_time)
            self.read_countsBT.append(btree.nodes_read)
            self.write_countsBT.append(btree.nodes_written)

        return sum(self.timesBT)



    # infographic data from measured performance
    def plot_performance(self, tree, keys, performance):

        isbtree = isinstance(tree, BTree)

        plt.figure(figsize=(10, 6))
        plt.subplot(3, 1, 1)

        if(not isbtree):
            if performance == "Insert":
                plt.scatter(keys, self.timesBST, label="Insert Time", s=4)
            if performance == "Search":
                plt.scatter(keys, self.timesBST, label="Search Time", s=4)
            if performance == "Delete":
                plt.scatter(keys, self.timesBST, label="Delete Time", s=4)
        else:
            if performance == "Insert":
                plt.scatter(keys, self.timesBT, label="Insert Time", s=4)
            if performance == "Search":
                plt.scatter(keys, self.timesBT, label="Search Time", s=4)
            if performance == "Delete":
                plt.scatter(keys, self.timesBT, label="Delete Time", s=4)

        plt.ylabel('Time (s)')
        plt.legend()

        plt.subplot(3, 1, 2)
        if(not isbtree):
            plt.scatter(keys, self.read_countsBST, label="Read Nodes", color='orange', s=4)
            plt.yticks(range(min(self.read_countsBST), max(self.read_countsBST) + 1, 2))
        else:
            plt.scatter(keys, self.read_countsBT, label="Read Nodes", color='orange', s=4)
            plt.yticks(range(min(self.read_countsBT), max(self.read_countsBT) + 1, 2))

        plt.ylabel('Read Nodes')
        plt.legend()

        plt.subplot(3, 1, 3)
        plt.ylabel('Written Nodes')
        if performance == "Insert" or performance == "Delete":
            if(not isbtree):
                plt.scatter(keys, self.write_countsBST, label="Written Nodes", color='green', s=4)
                plt.yticks(range(min(self.write_countsBST), max(self.write_countsBST) + 1))
            else:
                plt.scatter(keys, self.write_countsBT, label="Written Nodes", color='green', s=4)
                plt.yticks(range(min(self.write_countsBT), max(self.write_countsBT) + 1))
        else:
            plt.plot(0, 0, label="Written Nodes", color='green')
        plt.legend()

        if performance == "Insert":
            plt.xlabel('Added keys')
        if performance == "Delete":
            plt.xlabel('Deleted keys')

        plt.tight_layout()
        plt.show()


    def plotComparingPerformances(self, keys, performance):
        plt.figure(figsize=(10, 6))
        plt.subplot(3, 1, 1)

        if performance == "Insert":
            plt.scatter(keys, self.timesBST, label="Insert Time BST", color='blue', s = 4)
            plt.scatter(keys, self.timesBT, label="Insert Time BT", color='purple', s = 4)
        if performance == "Search":
            plt.scatter(keys, self.timesBST, label="Search Time BST", color='blue', s = 4)
            plt.scatter(keys, self.timesBT, label="Search Time BT", color='purple', s = 4)
        if performance == "Delete":
            plt.scatter(keys, self.timesBST, label="Delete Time BST", color='blue', s = 4)
            plt.scatter(keys, self.timesBT, label="Delete Time BT", color='purple', s = 4)
            #plt.yticks(range(min(self.timesBT), max(self.timesBT) + 1))

        plt.ylabel('Time (s)')
        plt.legend()

        plt.subplot(3, 1, 2)
        plt.scatter(keys, self.read_countsBST, label="Read Nodes BST", color='orange', s = 4)
        plt.scatter(keys, self.read_countsBT, label="Read Nodes BT", color='red', s = 4)
        #plt.yticks(range(min(self.read_counts), max(self.read_counts) + 1))
        plt.ylabel('Read Nodes')
        plt.legend()

        plt.subplot(3, 1, 3)
        plt.ylabel('Written Nodes')
        if performance == "Insert" or performance == "Delete":
            plt.scatter(keys, self.write_countsBST, label="Written Nodes BST", color='green', s = 4)
            plt.scatter(keys, self.write_countsBT, label="Written Nodes BT", color='yellow', s = 4)
            #plt.yticks(range(min(self.write_counts), max(self.write_counts) + 1))
        else:
            plt.plot(0, 0, label="Written Nodes", color='green')
        plt.legend()

        if performance == "Insert":
            plt.xlabel('Added keys')
        if performance == "Delete":
            plt.xlabel('Deleted keys')

        plt.tight_layout()
        plt.show()
