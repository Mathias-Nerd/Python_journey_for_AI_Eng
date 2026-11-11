# Drill 06: Metadata Preserver (`functools.wraps`)

## Learning Target
Learn to use `@functools.wraps(func)` to preserve the original function's `__name__`, `__doc__`, and introspection signatures when decorated.

---

## Problem Statement

Write a decorator `logged(func)`:
- Prints or executes behavior before/after.
- Preserves the original `func.__name__` and `func.__doc__` using `functools.wraps`.

---

## Examples

```python
@logged
def calculate(a, b):
    """Calculates sum."""
    return a + b

calculate.__name__  # "calculate" (NOT "wrapper"!)
calculate.__doc__   # "Calculates sum."
```
