import random

from packaging.tags import platform_tags

from performanceInfographic import PlotGenerator
from btree import BTree
from binarysearchtree import BinarySearchTree

pltGen = PlotGenerator()
btree_instance = BTree(3)
bstree_instance = BinarySearchTree()


keys = random.sample(range(1001), 900)
#keys = list(range(1,30))
timeInsBST = pltGen.measure_tree_performanceBST(bstree_instance, keys, "Insert")
timeInsBT = pltGen.measure_tree_performanceBT(btree_instance, keys, "Insert")
#pltGen.plot_performance(bstree_instance, keys, "Insert")
keys = random.sample(range(1001), 900)
timeDelBST = pltGen.measure_tree_performanceBST(bstree_instance, keys, "Delete")
timeDelBT = pltGen.measure_tree_performanceBT(btree_instance, keys, "Delete")
pltGen.plotComparingPerformances(keys, "Delete")
print("Tot Insert time bstree: " + str(timeInsBST))
print("Tot Insert time btree: " + str(timeInsBT))
print("Tot Delete time bstree: " + str(timeDelBST))
print("Tot Delete time btree: " + str(timeDelBT))

#keys = random.sample(range(1001), 300)
#timeDelBST = pltGen.measure_tree_performanceBST(bstree_instance, keys, "Delete")
#timeDelBT = pltGen.measure_tree_performanceBT(btree_instance, keys, "Delete")
#pltGen.plotComparingPerformances(keys, "Delete")
#print("Tot Delete time bstree: " + str(timeDelBST))
#print("Tot Delete time btree: " + str(timeDelBT))
#keys = list(range(1,30))

# pltGen.measure_tree_performance(bstree_instance, keys, "Delete")
# pltGen.plot_performance(keys, "Delete")
# -----------------------------------------------------------------------------
# btree perfomances with linear 99 keys
#keys = list(range(1, 100))  # [1, .... , 99] keys
# keys = [random.randint(1,100) for _ in range (100)]

# times, reads, writes = measure_tree_performance(btree_instance, keys, "Insert")
# plot_performance(keys, times, reads, writes, "Insert")
# times, reads, writes = measure_tree_performance(btree_instance, keys, "Search")
# plot_performance(keys, times, reads, writes, "Search")
# times, reads, writes = measure_tree_performance(btree_instance, keys, "Delete")
# plot_performance(keys, times, reads, writes, "Delete")
# #-----------------------------------------------------------------------------
# #btree perfomances with linear 999 keys
# btree_instance = BTree(3)
# keys = list(range(1, 1000)) # [1, ... , 999] keys
#
# times, reads, writes = measure_tree_performance(btree_instance, keys, "Insert")
# plot_performance(keys, times, reads, writes, "Insert")
# times, reads, writes = measure_tree_performance(btree_instance, keys, "Search")
# plot_performance(keys, times, reads, writes, "Search")
# times, reads, writes = measure_tree_performance(btree_instance, keys, "Delete")
# plot_performance(keys, times, reads, writes, "Delete")
# #-----------------------------------------------------------------------------
# #btree performances with random 99 keys
# keys = [random.randint(1, 100) for _ in range(100)] # 99 random keys
#
# times, reads, writes = measure_tree_performance(btree_instance, keys, "Insert")
# plot_performance(keys, times, reads, writes, "Insert")
# times, reads, writes = measure_tree_performance(btree_instance, keys, "Search")
# plot_performance(keys, times, reads, writes, "Search")
# times, reads, writes = measure_tree_performance(btree_instance, keys, "Delete")
# plot_performance(keys, times, reads, writes, "Delete")
# #-----------------------------------------------------------------------------
# btree performances with random 999 keys
# keys = [random.randint(1,1000) for _ in range (1000)] # random 999 keys
#
# times, reads, writes = measure_tree_performance(bstree_instance, keys, "Insert")
# plot_performance(keys, times, reads, writes, "Insert")
# times, reads, writes = measure_tree_performance(bstree_instance, keys, "Search")
# plot_performance(keys, times, reads, writes, "Search")
# times, reads, writes = measure_tree_performance(bstree_instance, keys, "Delete")
# plot_performance(keys, times, reads, writes, "Delete")

# #-----------------------------------------------------------------------------
# bstree perfomances with 99 keys
# keys = list(range(1, 10))  # Crea una lista di numeri da 1 a 10
# random.shuffle(keys) # mescola la lista in ordine casuale
#
# for key in keys:
#     bstree_instance.insert(key)
# print(bstree_instance._print_tree(bstree_instance.root))
#
# for key in keys:
#     bstree_instance.delete(key)
#     print("after delete key " + str(key) + ": " + str(bstree_instance._print_tree(bstree_instance.root)))
#
# print(bstree_instance.nodes_read)
# print(bstree_instance.nodes_written)
# print(bstree_instance._print_tree(bstree_instance.root))
#
# bstree_instance.insert(2)
# print(bstree_instance._print_tree(bstree_instance.root))




# keys = [random.randint(1, 500) for _ in range(500)] # 99 random keys
# times, reads, writes = measure_tree_performance(bstree_instance, keys, "Insert")
# plot_performance(keys, times, reads, writes, "Insert")
# times, reads, writes = measure_tree_performance(bstree_instance, keys, "Search")
# plot_performance(keys, times, reads, writes, "Search")
# times, reads, writes = measure_tree_performance(bstree_instance, keys, "Delete")
# plot_performance(keys, times, reads, writes, "Delete")

# bstree_instance.insert(10)
# bstree_instance.insert(5)
# bstree_instance.insert(30)
# bstree_instance.insert(25)
# bstree_instance.insert(50)
# bstree_instance.insert(60)
# bstree_instance.insert(7)
# bstree_instance.insert(9)
# print(bstree_instance.print_tree())
#
# bstree_instance.delete(30)
# print(bstree_instance.print_tree())
#
# bstree_instance.delete(60)
# print(bstree_instance.print_tree())
#
# bstree_instance.delete(10)
# print(bstree_instance.print_tree())
# # #-----------------------------------------------------------------------------
# #bstree perfomances with 149 keys
# keys = list(range(1, 150))  # [1, .... , 999] keys
#
# times, reads, writes = measure_tree_performance(bstree_instance, keys, "Insert")
# plot_performance(keys, times, reads, writes, "Insert")
# times, reads, writes = measure_tree_performance(bstree_instance, keys, "Delete")
# plot_performance(keys, times, reads, writes, "Delete")
# #-----------------------------------------------------------------------------
# #bstree perfomances with 199 keys
# keys = list(range(1, 200))  # [1, .... , 99] keys
#
# times, reads, writes = measure_tree_performance(bstree_instance, keys, "Insert")
# plot_performance(keys, times, reads, writes, "Insert")
# times, reads, writes = measure_tree_performance(bstree_instance, keys, "Delete")
# plot_performance(keys, times, reads, writes, "Delete")
# #-----------------------------------------------------------------------------
