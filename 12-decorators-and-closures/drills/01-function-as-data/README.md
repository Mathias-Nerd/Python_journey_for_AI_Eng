# Drill 01: Functions as First-Class Citizens

## Learning Target
Understand that in Python, functions are first-class objects: they can be assigned to variables, passed as arguments to other functions, stored in data structures, and returned from functions.

---

## Problem Statement

Implement:
1. `apply_pipeline(data: list[int], operations: list[callable]) -> list[int]`:
   - Passes `data` through each transformation function sequentially.
2. `make_multiplier(factor: int) -> callable`:
   - Returns a new function that multiplies its single numeric argument by `factor`.

---

## Examples

```python
double = make_multiplier(2)
double(5)  # 10

def add_ten(x): return x + 10
apply_pipeline([1, 2, 3], [double, add_ten]) # [12, 14, 16]
```
