import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import time

from btree import BTree
from binarysearchtree import BinarySearchTree


class PlotGenerator:

    def __init__(self):
        self.read_counts = []
        self.write_counts = []
        self.times = []

    # method that measures time performance for each operation
    def measure_tree_performance(self, tree, keys, performance):
        self.read_counts = []
        self.write_counts = []
        self.times = []

        isbtree = isinstance(tree, BTree)

        for key in keys:
            start_time = time.perf_counter()  # time in sec

            if performance == "Insert":
                tree.insert(key)
            elif performance == "Search":
                tree.search(key)
            elif performance == "Delete":
                if isbtree:
                    # btree_instance.delete(btree_instance.root, key)
                    tree.delete(tree.root, key)
                else:  # means that we have binarysearchtree instance
                    tree.delete(key)
                    # bstree_instance.delete(key)
                    # print("bstre_instance nr: " + str(bstree_instance.nodes_read))
                    # print("bstre_instance nw: " + str(bstree_instance.nodes_written))

            end_time = time.perf_counter()
            self.times.append(end_time - start_time)
            self.read_counts.append(tree.nodes_read)
            self.write_counts.append(tree.nodes_written)

    # infographic data from measured performance
    def plot_performance(self, keys, performance):
        plt.figure(figsize=(10, 6))
        plt.subplot(3, 1, 1)

        if performance == "Insert":
            plt.scatter(keys, self.times, label="Insert Time", s=10)
        if performance == "Search":
            plt.scatter(keys, self.times, label="Search Time", s=10)
        if performance == "Delete":
            plt.scatter(keys, self.times, label="Delete Time", s=10)

        plt.ylabel('Time (s)')
        plt.legend()

        plt.subplot(3, 1, 2)
        plt.scatter(keys, self.read_counts, label="Read Nodes", color='orange', s=10)
        plt.ylabel('Read Nodes')
        plt.legend()

        plt.subplot(3, 1, 3)
        plt.ylabel('Written Nodes')
        if performance == "Insert" or performance == "Delete":
            plt.scatter(keys, self.write_counts, label="Written Nodes", color='green', s=10)
        else:
            plt.plot(0, 0, label="Written Nodes", color='green')
        plt.legend()

        if performance == "Insert":
            plt.xlabel('Added keys')
        if performance == "Delete":
            plt.xlabel('Deleted keys')

        plt.tight_layout()
        plt.show()
