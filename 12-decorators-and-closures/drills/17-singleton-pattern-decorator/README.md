# Drill 17: Singleton Pattern Class Decorator

## Learning Target
Implement the Singleton creational pattern using a class decorator with an internal instance cache.

---

## Problem Statement

Write a class decorator `singleton(cls)`:
- Ensures only one instance of the decorated class is ever created.
- Subsequent calls to `Class()` return the existing instance.

---

## Examples

```python
@singleton
class DatabaseConnection:
    def __init__(self):
        self.connected = True

db1 = DatabaseConnection()
db2 = DatabaseConnection()
db1 is db2  # True!
```
