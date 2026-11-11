# Drill 07: Function Call Counter (Quest 4)

## Learning Target
Implement the stateful decorator from Quest 4: a decorator that tracks how many times a function has been called, persisting count as an attribute on the callable.

---

## Problem Statement

Write a decorator `count_calls`:
- Attaches an attribute `calls` initialized to `0` on the wrapper.
- Increments `calls` by 1 on every invocation.
- Returns the underlying function's result.
- Works with any positional or keyword arguments.

---

## Examples

```python
@count_calls
def ping():
    return "pong"

ping.calls  # 0
ping()      # "pong"
ping()      # "pong"
ping.calls  # 2
```
