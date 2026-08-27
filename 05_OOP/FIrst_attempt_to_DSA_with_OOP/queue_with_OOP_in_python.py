# Implementing queue data structure
from collections import deque


class Queue:
    def __init__(self):
        self._items = deque()

    def __repr__(self):
        return f"Queue({self._items})"

    def __len__(self):
        return len(self._items)
    # Queue methods
    # Is_empty method

    def is_empty(self):
        return len(self._items) == 0
    # peek method

    def peek(self):
        if self.is_empty():
            raise IndexError("There is no item in the queue")
        return self._items[0]
    # Enqueue method

    def enqueue(self, item):
        self._items.append(item)
        # DEqueue method

    def dequeue(self):
        if self.is_empty():
            raise IndexError("There is no item in the queue")
        return self._items.popleft()


queue = Queue()
print(queue)
queue.enqueue("Mathias")
print(queue)
queue.enqueue("David")
print(queue)
queue.enqueue("Sodiq")
print(queue)
queue.enqueue("Aniekan")
print(queue)
queue.dequeue()
print(queue)
queue.dequeue()
print(queue)
queue.dequeue()
print(queue)
queue.dequeue()
print(queue)
queue.dequeue()
print(queue)