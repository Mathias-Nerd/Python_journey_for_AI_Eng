# Author: Mathias Nerd
# Practicing the implementation for stack data structure
# Second practice of implementing stack data structure in python with classes  
class Stack:
    def __init__(self):
        self._items = []

    # The len method overrride
    def __len__(self):
        return len(self._items)

    # The repr override
    def __repr__(self):
        return f"Stack: ({self._items})"

    # The stack methods
    def is_empty(self):
        return len(self._items) == 0

    def peek(self):
        if self.is_empty():
            raise ValueError("No element inside stack")
        return self._items[-1]

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow")
        return self._items.pop()

    def push(self, item):
        self._items.append(item)


stack = Stack()
print(stack)
stack.push("Massachussetts")
print(stack)
stack.push("Los Angeles")
stack.push("Broklyn")
print(stack)
stack.pop()
print(stack)
print(stack.peek())
stack.pop()
stack.pop()
print(stack)
stack.pop()
print(stack.peek())
stack.pop()
stack.pop()
print(stack)
