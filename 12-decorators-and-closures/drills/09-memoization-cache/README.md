# Drill 09: Memoization Cache Decorator

## Learning Target
Implement your own `@memoize` caching decorator from scratch using a closure dictionary.

---

## Problem Statement

Write a decorator `memoize`:
- Caches results keyed by positional arguments `args`.
- If called with previously seen arguments, returns the cached result without re-executing `func`.
- Attaches `wrapper.cache` exposing the internal dictionary.

---

## Examples

```python
call_count = 0

@memoize
def square(n):
    global call_count
    call_count += 1
    return n * n

square(4)  # 16, call_count == 1
square(4)  # 16, call_count == 1 (returned from cache!)
```
