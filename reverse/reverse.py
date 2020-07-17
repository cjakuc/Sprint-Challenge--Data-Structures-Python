class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # If self.head is None or we are at the end of the list, make the head the current node and return
        if (self.head is None) or (node.get_next() is None):
            self.head = node
            return

        # Recurse through all the nodes
        self.reverse_list(node.get_next(), prev)
        # Grab the now previous node, the former next node
        prev = node.get_next()
        # Make the next node of the previous node the current node
        prev.set_next(node)
        # Make the next node of the current node none
        node.set_next(None)

        return