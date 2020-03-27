class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        # reference to the head of the list
        self.head = None

    def add_to_head(self, value):
        node = Node(value)
        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False
        # get a reference to the node we're currently at; update this as we
        # traverse the list
        current = self.head
        # check to see if we're at a valid node
        while current:
            # return True if the current value we're looking at matches our
            # target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False

    def reverse_list(self, node, prev):
        # You must use recursion for this solution

        current_node = self.head
        prev_node = None

        # Iterate through the single linked list

        # While current_node exists (head node at first) sets base
        while current_node is not None:
            # Store next_node as the next node past the head
            next_node = current_node.get_next()
            # Set the node thats past the head to the previous node (Shifts over the value)
            current_node.set_next(prev_node)
            # Now set prev_node equal to current_node (value change)
            prev_node = current_node
            # And current_node equal to next_node (values reversed)
            current_node = next_node
        self.head = prev_node
