# Drill 13: Deprecated Warning Decorator

## Learning Target
Manage library lifecycles and migrations by warning developers when using deprecated functions.

---

## Problem Statement

Write a decorator `deprecated(replacement_name: str | None = None)`:
- Emits a `warnings.warn(..., category=DeprecationWarning)` on call.
- Warning message must mention the deprecated function name and optional replacement.

---

## Examples

```python
@deprecated(replacement_name="new_function")
def old_function():
    return 1
```
