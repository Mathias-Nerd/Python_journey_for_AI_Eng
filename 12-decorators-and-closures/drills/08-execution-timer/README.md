# Drill 08: Execution Timer Decorator

## Learning Target
Measure performance bottlenecks using high-precision performance timers (`time.perf_counter()`).

---

## Problem Statement

Write a decorator `time_execution`:
- Records elapsed execution time in seconds on `wrapper.last_duration`.
- Preserves metadata and returns the original function's return value.

---

## Examples

```python
import time

@time_execution
def sleep_a_bit():
    time.sleep(0.05)
    return "done"

res = sleep_a_bit() # "done"
sleep_a_bit.last_duration >= 0.05 # True
```
