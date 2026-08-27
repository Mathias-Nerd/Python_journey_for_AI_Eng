# Implementing linked list data structure
# 1. create the node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 2. Creating the linked list blueprint


class LinkedList:
    

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
            return
        current = self.head

        while current.next is not None:
            current = current.next
        current.next = new_node

    def traverse_and_print(self):
        current = self.head
        while current is not None:
            print(f"Customer Cup: {current.data}")
            current = current.next


node = LinkedList()
node.append("Alice")
node.append("Bob")
node.traverse_and_print()
