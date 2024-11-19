import random

from packaging.tags import platform_tags

from performanceInfographic import PlotGenerator
from btree import BTree
from binarysearchtree import BinarySearchTree

pltGen = PlotGenerator()
btree_instance = BTree(3)
bstree_instance = BinarySearchTree()


keys = random.sample(range(1001), 900) #900 random keys taken from random interval [0-1000]
                                       #for insert operations
timeInsBST = pltGen.measure_tree_performanceBST(bstree_instance, keys, "Insert")
timeInsBT = pltGen.measure_tree_performanceBT(btree_instance, keys, "Insert")

keys = random.sample(range(1001), 900)# 900 random keys taken from random interval [0-1000]
                                       #for delete operations
timeDelBST = pltGen.measure_tree_performanceBST(bstree_instance, keys, "Delete")
timeDelBT = pltGen.measure_tree_performanceBT(btree_instance, keys, "Delete")

pltGen.plotComparingPerformances(keys, "Delete")

print("Tot Insert time bstree: " + str(timeInsBST))
print("Tot Insert time btree: " + str(timeInsBT))
print("Tot Delete time bstree: " + str(timeDelBST))
print("Tot Delete time btree: " + str(timeDelBT))

