from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # If the capacity is equal to the storage length
        if self.capacity == self.storage.length:
            # If it is not equal to self.current (none)
            if not self.current:
                # Then self.current equals the head of this structure
                self.current = self.storage.head
            # If the current value is the same as the set value for the head
            if self.current.value == self.storage.head.value:
                # Remove the previous value
                self.storage.remove_from_head()
                # Add this item to the head instead
                self.storage.add_to_head(item)
                # set this current value to the next node, after the head
                self.current = self.current.next
            # Otherwise
            else:
                self.current.insert_after(item)
                # If the node after the current node is there
                if self.current.next.next:
                    # The new_current equals that node value
                    new_current = self.current.next.next
                # Otherwise
                else:
                    # The new_current equals the storage head node
                    new_current = self.storage.head
                # Delete this value
                self.storage.delete(self.current)
                # Add length to the storage
                self.storage.length += 1
                # Set the current equal to the new_current
                self.current = new_current
        # Otherwise
        else:
            # Add value as tail node
            self.storage.add_to_tail(item)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here

        # Node equals the head value
        node = self.storage.head
        # While node exists
        while node:
            # Append that value to the array
            list_buffer_contents.append(node.value)
            # Set node as node.next to move throughout the elements
            node = node.next
        # Return that array
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
