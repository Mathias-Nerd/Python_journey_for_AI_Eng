# Drill 04: Return Value Forwarder

## Learning Target
Understand the common bug where a decorator calls the original function but forgets to return `result`, causing the decorated function to silently return `None`.

---

## Problem Statement

Write a decorator `forward_result`:
- Calls the underlying function with any arguments.
- Strictly returns whatever the underlying function returns.
- Must work for values, `None`, empty lists, and exceptions.

---

## Examples

```python
@forward_result
def multiply(a, b):
    return a * b

multiply(3, 4)  # 12 (must NOT be None!)
```
