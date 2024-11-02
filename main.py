import random

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import time


from btree import BTree
from binarysearchtree import BinarySearchTree


btree_instance = BTree(3)
bstree_instance = BinarySearchTree()
#bstree_instance.insert(1)

def measure_tree_performance(tree, keys, performance):
    read_counts = []
    write_counts = []
    times = []

    btree = isinstance(tree, BTree)

    for key in keys:
        start_time = time.perf_counter() # time in sec

        if(performance == "Insert"):
          if(btree):
            btree_instance.insert(key)
          else:
            bstree_instance.insert(key)
        elif(performance == "Search"):
          if(btree):
            btree_instance.search(key)
          else:
            bstree_instance.search(key)
        elif(performance == "Delete"):
          if(btree):
            btree_instance.delete(btree_instance.root, key)
          else:
            bstree_instance.delete(key)

        end_time = time.perf_counter()
        times.append(end_time - start_time)
        read_counts.append(tree.nodes_read)
        write_counts.append(tree.nodes_written)
        # if(btree):
        #   read_counts.append(tree.nodes_read)
        #   write_counts.append(tree.nodes_written)
        # else:
        #   read_counts.append(tree.get_nodes_read())
        #   write_counts.append(tree.get_nodes_written())

    return times, read_counts, write_counts

#graphics generation
def plot_performance(keys, times, read_counts, write_counts, performance):
    plt.figure(figsize=(10, 6))


    plt.subplot(3, 1, 1)

    if(performance == "Insert"):
      plt.plot(keys, times, label="Insert Time")
    if(performance == "Search"):
      plt.scatter(keys, times, label="Search Time", s = 10)
    if(performance == "Delete"):
     plt.scatter(keys, times, label="Delete Time", s = 10)

    plt.ylabel('Time (ms)')
    plt.legend()


    plt.subplot(3, 1, 2)
    plt.plot(keys, read_counts, label="Read Nodes", color='orange')
    plt.ylabel('Read Nodes')
    plt.legend()

    plt.subplot(3, 1, 3)
    plt.ylabel('Written Nodes')
    if(performance == "Insert" or performance == "Delete"):
        plt.scatter(keys, write_counts, label="Written Nodes", color='green', s = 10)
    else:
        plt.plot(0,0, label = "Written Nodes", color = 'green')
    plt.legend()

    if(performance == "Insert"):
        plt.xlabel('Added keys')
    if(performance == "Delete"):
        plt.xlabel('Deleted keys')

    plt.tight_layout()
    plt.show()

#-----------------------------------------------------------------------------
#btree perfomances with linear 99 keys
keys = list(range(1, 100))  # [1, .... , 99] keys
#keys = [random.randint(1,100) for _ in range (100)]

times, reads, writes = measure_tree_performance(btree_instance, keys, "Insert")
plot_performance(keys, times, reads, writes, "Insert")
times, reads, writes = measure_tree_performance(btree_instance, keys, "Search")
plot_performance(keys, times, reads, writes, "Search")
times, reads, writes = measure_tree_performance(btree_instance, keys, "Delete")
plot_performance(keys, times, reads, writes, "Delete")
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
#btree performances with random 999 keys
# keys = [random.randint(1,1000) for _ in range (1000)] # random 999 keys
#
# times, reads, writes = measure_tree_performance(bstree_instance, keys, "Insert")
# plot_performance(keys, times, reads, writes, "Insert")
# times, reads, writes = measure_tree_performance(bstree_instance, keys, "Search")
# plot_performance(keys, times, reads, writes, "Search")
# times, reads, writes = measure_tree_performance(bstree_instance, keys, "Delete")
# plot_performance(keys, times, reads, writes, "Delete")

# #-----------------------------------------------------------------------------
#bstree perfomances with 99 keys
#keys = list(range(1, 150))  # [1, .... , 99] keys

# times, reads, writes = measure_tree_performance(bstree_instance, keys, "Insert")
# plot_performance(keys, times, reads, writes, "Insert")
# times, reads, writes = measure_tree_performance(bstree_instance, keys, "Search")
# plot_performance(keys, times, reads, writes, "Search")
# times, reads, writes = measure_tree_performance(bstree_instance, keys, "Delete")
# plot_performance(keys, times, reads, writes, "Delete")
#
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