# Drill 16: Class Decorator for Method Instrumentation

## Learning Target
Understand how decorators can receive a `class` object, inspect its attributes, and wrap methods dynamically.

---

## Problem Statement

Write a class decorator `add_repr`:
- Automatically adds a clean `__repr__` method to the decorated class displaying all `self.__dict__` attributes: `ClassName(attr1=val1, attr2=val2)`.

---

## Examples

```python
@add_repr
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(3, 4)
repr(p) # "Point(x=3, y=4)"
```
