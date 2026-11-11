# Drill 02: Closure State Accumulator (`nonlocal`)

## Learning Target
Understand how inner functions bind and retain access to outer variables via lexical closures, and how the `nonlocal` keyword allows mutating state in the enclosing scope.

---

## Problem Statement

Write a function `make_accumulator(initial_value: int = 0) -> callable`:
- Returns a function `accumulate(delta: int = 1) -> int`.
- Each call to `accumulate(delta)` adds `delta` to the running total and returns the updated total.
- State is strictly maintained in the closure.

---

## Examples

```python
acc = make_accumulator(10)
acc(5)   # 15
acc(2)   # 17
acc(-10) # 7
```
