# Drill 14: Three-Tier Parametric Decorator (`@repeat`)

## Learning Target
Master the 3-level function nesting pattern required when a decorator accepts configuration arguments:
1. Outer function receives decorator arguments.
2. Middle function receives the target callable `func`.
3. Inner wrapper receives `*args, **kwargs` on call.

---

## Problem Statement

Write a decorator `repeat(num_times: int)`:
- Executes the underlying function `num_times`.
- Returns the result of the final execution.

---

## Examples

```python
count = 0

@repeat(num_times=3)
def tick():
    global count
    count += 1
    return count

tick() # returns 3, count == 3
```
