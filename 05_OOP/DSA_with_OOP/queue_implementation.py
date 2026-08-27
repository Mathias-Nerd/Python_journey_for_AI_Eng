# Author: Mathias Nerd
# Practicing the implementation of queue data structure
# Second practice of implementing queue data structure in python with classes
from collections import deque


class Queue:
    # overwrting some dunder methods
    def __init__(self):
        self._items = deque()

    def __repr__(self):
        return f"Queue: ({self._items})"

    def __len__(self):
        return len(self._items)

    # Queue functions
    # is_empty
    def is_empty(self):
        return len(self._items) == 0
    # peek

    def peek(self):
        if self.is_empty():
            raise IndexError("The queue is already empty")
        return self._items[0]
    # enqueue

    def enqueue(self, item):
        self._items.append(item)
    # dequeue

    def dequeue(self):
        if self.is_empty():
            raise IndexError("You are trying to access an invalid ")
        return self._items.popleft()


queue = Queue()
queue.enqueue(5)
print(queue)
queue.enqueue(10)
queue.enqueue(50)
queue.enqueue(10)
print(queue)
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
print(queue)
queue.peek()
