class Node:
    # constructor
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


# A Linked List class with a single head node
class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.current = None

    # insertion method for the linked list
    def insert(self, data):
        new_node = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def get_head(self):
        return self.head

    def get_current(self):

        if self.current is None:
            self.current = self.head
        else:
            self.current = self.current.next
            if self.current is None:
                self.current = self.head

        return self.current
