# Drill 10: Input Type Enforcer Decorator

## Learning Target
Enforce runtime type safety by validating argument types against specified allowed types.

---

## Problem Statement

Write a decorator `enforce_types(*expected_types)`:
- Compares each positional argument against its corresponding expected type.
- If an argument doesn't match (`not isinstance(arg, expected_type)` or is `bool` when `int` expected), raise a `TypeError`.

---

## Examples

```python
@enforce_types(int, str)
def repeat(times, text):
    return text * times

repeat(3, "ha")   # "hahaha"
repeat("3", "ha") # raises TypeError!
```
