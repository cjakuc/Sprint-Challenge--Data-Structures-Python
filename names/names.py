import time
from binary_search_tree import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)

end_time = time.time()
print("----------")
print("Original Solution")
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")
print("----------")

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# My solution

# Instantiate the root node to make a BST
bst = BSTNode(names_1[0])
# Insert the rest of the nodes/names into the tree
for name_1 in names_1[1:]:
    bst.insert(name_1)
# Loop through the second list of names
for name_2 in names_2:
    # See if each name in names_2 is in the BST
    if bst.contains(name_2):
        # If they are, append them to duplicates
        duplicates.append(name_2)

end_time = time.time()
print("----------")
print("BST Solution")
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")
print("----------")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Use a dictionary to store all the names in name_1 as keys
my_dict = {name:0 for name in names_1}

# If a name in name_2 is a key in my_dict, append it to duplicates
for name_2 in names_2:
    if name_2 in list(my_dict.keys()):
        duplicates.append(name_1)


end_time = time.time()
print("----------")
print("List/Dict Solution")
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")
print("----------")

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

intersections = set(names_1).intersection(names_2)
for name in intersections:
    duplicates.append(name)


end_time = time.time()
print("----------")
print("List/Set Solution")
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")
print("----------")