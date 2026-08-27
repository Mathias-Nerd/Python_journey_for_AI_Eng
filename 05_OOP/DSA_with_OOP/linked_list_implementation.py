# Author: Mathias Nerd
# Practicing the implementation of LInked List data structure
# Second practice of implementing LInked List data structure in python with classes
class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    #Linked list operations
    def is_empty(self):
        return self.head == None

    #append method
    def append(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node 

    #Prepend
    def prepend(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    #Traverse and print
    def traverse_and_print(self):
        current = self.head
        while current is not None:
            print(current.data, end = " -> ")
            current = current.next
    
        

# node_1 = Node(5)
# node_2 = Node(20)
# node_3 = Node(6)
# node_4 = Node(30)

# node_1.next = node_2
# node_2.next = node_3
# node_3.next = node_4


linked_list = LinkedList()

print(linked_list.is_empty())
linked_list.traverse_and_print()
linked_list = LinkedList()

linked_list.append("Alice")
linked_list.append("Bob")
linked_list.append("Charlie")

linked_list.traverse_and_print()