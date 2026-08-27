class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

n1 = Node("A")
n2 = Node("B")
n1.next = n2

print(n1.next.val)



