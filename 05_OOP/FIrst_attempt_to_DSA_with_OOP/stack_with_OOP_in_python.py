# Building a stack data structure
# 1. Create a class called stack
class Stack:
    # 2. set the __init__ to initialise an empty list
    def __init__(self):
        self._items = []  # creating an empty list
# 3. set the __len__ to measure the length of the list

    def __len__(self):
        return len(self._items)
# 4. set the __repr__ to print the that this is a stack

    def __repr__(self):
        """Provides a developer-friendly representation."""
        return f"Stack({self._items})"
# 5. Start building the push, pop, is_empty and peek
    # 5.A. is_empty method

    def is_empty(self):
        return len(self._items) == 0
    # 5. B. peek method

    def peek(self):
        if self.is_empty():
            raise IndexError("The stack is empty")
        return self._items[-1]
    # 5. C. Push method

    def push(self, item):
        self._items.append(item)
    # 5. D.pop method

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        return self._items.pop()


cities = Stack()
print(cities)
cities.push("Boston")
print(cities)
cities.push("Sydney")
print(cities)
print(cities.peek())
# cities.push("Seattle")
# print(cities)
# cities.push("Broklyn")
# print(cities)
# cities.push("Utah")
# print(cities)
# cities.pop()
# print(cities)
# cities.pop()
# print(cities)
# cities.pop()
# cities.pop()
# cities.pop()
# print(cities)
# cities.pop()
