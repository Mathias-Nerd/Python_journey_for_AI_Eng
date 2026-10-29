# Drill 05: Count Target Occurrences

## Learning Target
Practice recursive search and accumulation with conditional contributions across a linear data structure using an index pointer.

---

## Problem Statement

Write a function `count_occurrences(items: list, target, index: int = 0) -> int` that recursively counts how many times `target` appears in `items`.

### Rules & Constraints:
1. Do not use `.count()`, loops (`for`, `while`), or comprehensions.
2. Do not slice the list. Use `index` to track the current position.
3. If `items` is not a list, raise `TypeError("items must be a list")`.
4. Empty list `[]` returns `0`.

---

## Examples

```python
count_occurrences([1, 2, 3, 2, 4, 2], 2)       # 3
count_occurrences(["a", "b", "a", "c"], "a")   # 2
count_occurrences([1, 2, 3], 99)               # 0
count_occurrences([], 5)                       # 0
```

---

## Testing Your Solution
Run the test suite in this directory:
```bash
python test_exercise.py
```
