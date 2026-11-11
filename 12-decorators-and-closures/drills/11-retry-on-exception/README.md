# Drill 11: Retry on Exception with Backoff

## Learning Target
Implement resilience patterns: retrying failing network or database calls up to $N$ times before raising the final error.

---

## Problem Statement

Write a decorator `retry(max_attempts: int = 3, exceptions: tuple = (Exception,))`:
- Retries executing the decorated function if it raises any exception in `exceptions`.
- If it fails `max_attempts` times, raises the final exception.

---

## Examples

```python
attempts = 0

@retry(max_attempts=3)
def unstable():
    global attempts
    attempts += 1
    if attempts < 3:
        raise ValueError("temporary error")
    return "success"

unstable() # "success" on 3rd attempt
```
