# Drill 05: Arguments Forwarder (`*args, **kwargs`)

## Learning Target
Master universal argument passing using `*args` (positional tuple) and `**kwargs` (keyword dictionary) in wrapper functions.

---

## Problem Statement

Write a decorator `record_call_args`:
- Stores the last call's arguments in attributes on the decorated function:
  - `func.last_args`: tuple of positional arguments.
  - `func.last_kwargs`: dict of keyword arguments.
- Returns the original function's result.

---

## Examples

```python
@record_call_args
def profile(name, age, city="Lagos"):
    return f"{name}-{age}-{city}"

profile("Tunde", 25, city="Abuja")
profile.last_args    # ("Tunde", 25)
profile.last_kwargs  # {"city": "Abuja"}
```
