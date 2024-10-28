import random

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import time

from btree import BTree
from binarysearchtree import BSTree

btree_instance = BTree(3)
bstree_instance = BSTree(1)

def measure_tree_performance(tree, keys, performance):
    read_counts = []
    write_counts = []
    times = []

    btree = isinstance(tree, BTree)

    for key in keys:
        start_time = time.perf_counter()*1000 #time in ms

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

        end_time = time.perf_counter()*1000
        times.append(end_time - start_time)
        if(btree):
          read_counts.append(tree.nodes_read)
          write_counts.append(tree.nodes_written)
        else:
          read_counts.append(tree.get_nodes_read())
          write_counts.append(tree.get_nodes_written())

    return times, read_counts, write_counts

#graphics generation
def plot_performance(keys, times, read_counts, write_counts, performance):
    plt.figure(figsize=(10, 6))

    plt.subplot(3, 1, 1)
    if(performance == "Insert"):
      plt.scatter(keys, times, label="Insert Time")
    if(performance == "Search"):
      plt.scatter(keys, times, label="Search Time")
    if(performance == "Delete"):
     plt.scatter(keys, times, label="Delete Time")

    plt.ylabel('Time (ms)')
    plt.legend()

    plt.subplot(3, 1, 2)
    plt.scatter(keys, read_counts, label="Read Nodes", color='orange')
    plt.ylabel('Read Nodes')
    plt.legend()

    plt.subplot(3, 1, 3)
    plt.scatter(keys, write_counts, label="Written Nodes", color='green')
    plt.ylabel('Written Nodes')
    plt.legend()

    if(performance == "Insert"):
      plt.xlabel('Added keys')
    if(performance == "Delete"):
      plt.xlabel('Deleted keys')
    plt.tight_layout()
    plt.show()

#-----------------------------------------------------------------------------
#btree perfomances with 99 keys
#keys = list(range(1, 100))  # [1, .... , 99] keys
keys = [random.randint(1, 20) for _ in range(20)]

times, reads, writes = measure_tree_performance(btree_instance, keys, "Insert")
plot_performance(keys, times, reads, writes, "Insert")
times, reads, writes = measure_tree_performance(btree_instance, keys, "Delete")
plot_performance(keys, times, reads, writes, "Delete")

#-----------------------------------------------------------------------------
#btree perfomances with 999 keys
keys = list(range(1, 1000))  # [1, .... , 999] keys

times, reads, writes = measure_tree_performance(btree_instance, keys, "Insert")
plot_performance(keys, times, reads, writes, "Insert")
times, reads, writes = measure_tree_performance(btree_instance, keys, "Delete")
plot_performance(keys, times, reads, writes, "Delete")

#-----------------------------------------------------------------------------


#-----------------------------------------------------------------------------
#bstree perfomances with 99 keys
keys = list(range(1, 100))  # [1, .... , 99] keys

times, reads, writes = measure_tree_performance(bstree_instance, keys, "Insert")
plot_performance(keys, times, reads, writes, "Insert")
times, reads, writes = measure_tree_performance(bstree_instance, keys, "Delete")
plot_performance(keys, times, reads, writes, "Delete")
#-----------------------------------------------------------------------------
#bstree perfomances with 149 keys
keys = list(range(1, 150))  # [1, .... , 999] keys

times, reads, writes = measure_tree_performance(bstree_instance, keys, "Insert")
plot_performance(keys, times, reads, writes, "Insert")
times, reads, writes = measure_tree_performance(bstree_instance, keys, "Delete")
plot_performance(keys, times, reads, writes, "Delete")
#-----------------------------------------------------------------------------
#bstree perfomances with 199 keys
keys = list(range(1, 200))  # [1, .... , 99] keys

times, reads, writes = measure_tree_performance(bstree_instance, keys, "Insert")
plot_performance(keys, times, reads, writes, "Insert")
times, reads, writes = measure_tree_performance(bstree_instance, keys, "Delete")
plot_performance(keys, times, reads, writes, "Delete")
#-----------------------------------------------------------------------------