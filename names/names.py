import time

from bst import BinarySearchTree

start_time = time.time()

f = open('./names/names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('./names/names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements

# Initiate binary string
nameBST = BinarySearchTree(names_1[0])

# Search through list 1
for name_1 in names_1:
    nameBST.insert(name_1)
# search through list 2
for name_2 in names_2:
    if nameBST.contains(name_2):
        # append duplicates to data structure provided
        duplicates.append(name_2)

'''
The original runtime of the 2 "for loops" would be O(n^2) 
The new runtime with 1 "for loop" and an "if" statement would be O(n)
original == 11.9 seconds
new ==  0.2 seconds
'''

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
