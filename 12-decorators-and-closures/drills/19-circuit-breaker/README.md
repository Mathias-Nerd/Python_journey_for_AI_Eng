# Drill 19: Circuit Breaker Decorator

## Learning Target
Build a production-grade resilience circuit breaker that trips after consecutive failures to protect downstream systems.

---

## Problem Statement

Write a decorator `circuit_breaker(failure_threshold: int = 3)`:
- Tracks consecutive exceptions.
- If consecutive failures reach `failure_threshold`, the circuit **opens**.
- While open, subsequent calls immediately raise `RuntimeError("Circuit is OPEN")` without calling the wrapped function.
- A successful call resets the consecutive failure count to `0`.

---

## Examples

```python
@circuit_breaker(failure_threshold=2)
def api_call(fail=False):
    if fail: raise ConnectionError()
    return "ok"

api_call(True)  # raises ConnectionError (failures = 1)
api_call(True)  # raises ConnectionError (failures = 2 -> circuit trips OPEN)
api_call(False) # raises RuntimeError("Circuit is OPEN")
```
