# from stack import Stack
# from queue import MyQueue
# from singly_linked_list import *

# class MyQueue:
#     def __init__(self):
#         self.size = 0
#         self.storage = LinkedList()

#     def __len__(self):
#         return self.size

#     def enqueue(self, value):
#         self.storage.add_to_tail(value)
#         self.size += 1

#     def dequeue(self):
#         if self.storage.head:
#             self.size -= 1
#             return self.storage.remove_head()
#         return None

"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.

* Should have the methods `insert`, `contains`, `get_max`.
  * `insert` adds the input value to the binary search tree, adhering to the rules of the ordering of elements in a binary search tree.
  * `contains` searches the binary search tree for the input value, returning a boolean indicating whether the value exists in the tree or not.
  * `get_max` returns the maximum value in the binary search tree.
  * `for_each` performs a traversal of _every_ node in the tree, executing the passed-in callback function on each tree node value.
     There is a myriad of ways to perform tree traversal; in this case any of them should work. 
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Instantiate new_node w/ value
        new_node = BSTNode(value=value)
        # If value is less than root value
        if self.value > value:
            # If self.left doesn't exist make, set it to the new node
            if self.left is None:
                self.left = new_node
                return
            # Else, use recursion on self.left
            else:
                self.left.insert(value)
        # If value is greater than root value
        else:
            # If self.right doesn't exist make, set it to the new node
            if self.right is None:
                self.right = new_node
                return
            # Else, use recursion on self.right
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Case 1: self.value equals target
        if self.value == target:
            return True
        # Case 2: self.value is greater than target
        if self.value > target:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        # Case 3: self.value is less than target
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # Iterative approach
        # current = self
        # max_val = 0
        # if current is None:
        #     return max_val
        # while current is not None:
        #     max_val = current.value
        #     current = current.right
        # return max_val

        # Recursive approach
        if self is None:
            return None
        if self.right is None:
            return self.value
        return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        # # Solution with for_each method
        # arr = []
        # fn = lambda x: arr.append(x)
        # self.for_each(fn=fn)
        # arr.sort()
        # print(*arr, sep="\n")

        # Matt's solution
        if self is None:
            return
        # Check if we can move left
        if self.left is not None:
            self.left.in_order_print()
        # Visit the node by printing its value
        print(self.value)

        # Check if we can't move right
        if self.right is not None:
            self.right.in_order_print()
        

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        # Iterative solutio without Queue class
        # Use a queue to form a line for the nodes to get in
        # Start by placing the root node in the queue
        queue = [self]

        # Need a while loop to iterate (not recursion for BFT)
        while len(queue) > 0:
            # dequeue item from front of queue
            # print its value
            temp = queue.pop(0)
            print(temp.value)

            # Place current item's left node in queue if not None
            if temp.left is not None:
                queue.append(temp.left)
            # Place current item's right node in the queue if not None
            if temp.right is not None:
                queue.append(temp.right)

        # # Solution using Queue class
        # queue = MyQueue()
        # queue.enqueue(self.value)

        # current = self
        # while len(queue) > 0:
        #     temp = queue.dequeue()
        #     print(temp)

        #     if temp.left is not None:
        #         queue.enqueue(current.left.value)
        #         # current = current.left
        #     if temp.right is not None:
        #         queue.enqueue(current.right.value)
        #         # current = current.right            

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        # # Solution with for_each method (recursive)
        # fn = lambda x: print(x)
        # self.for_each(fn=fn)

        # Iterative approach without Stack class
        # Create a stack to put nodes in, start with root node in it
        stack = [self]

        # While loop to manage iteration
        while len(stack) > 0:
            # Pop item off stack and print its value
            temp = stack.pop(-1)
            print(temp.value)

            # Place current item's left node in stack if not None
            if temp.left:
                stack.append(temp.left)
            # Place current item's left node in stack if not None
            if temp.right:
                stack.append(temp.right)


    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
