# Drill 12: Rate Limiter Decorator

## Learning Target
Protect APIs and resources by enforcing a maximum call frequency per time window.

---

## Problem Statement

Write a decorator `rate_limit(max_calls: int, period_seconds: float)`:
- Allows up to `max_calls` within the trailing `period_seconds`.
- If call frequency is exceeded, raises `RuntimeError("Rate limit exceeded")`.

---

## Examples

```python
@rate_limit(max_calls=2, period_seconds=1.0)
def fetch_data():
    return "data"

fetch_data() # OK
fetch_data() # OK
fetch_data() # raises RuntimeError!
```
