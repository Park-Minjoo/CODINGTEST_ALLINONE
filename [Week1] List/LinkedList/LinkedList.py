from Node import Node

class LinkedList(object):
    def __init__ (self):
        self.head = None
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            # current = self.head
            # while(current.next):
            #     current = current.next
            # current.next = new_node
            self.tail.next = new_node
            self.tail = self.tail.next
    def get(self, idx):
        current = self.head
        for _ in range(idx):
            current = current.next
        return current.value
    def insert(self, idx, value):
        new_node = Node(value)
        current = self.head
        for _ in range(idx-1):
            current = current.next
            new_node.next = current.next
            current.next = new_node
    def remove(self, idx):
        current = self.head
        for _ in range(idx-1):
            current.next = current.next.next

ll = LinkedList()
