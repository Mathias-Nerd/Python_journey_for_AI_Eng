# Drill 04: Pure Recursive List Sum

## Learning Target
Learn to traverse linear sequences recursively using index pointers rather than creating expensive sliced list copies at each step.

---

## Problem Statement

Write a function `sum_list(numbers: list[int | float], index: int = 0) -> int | float` that returns the sum of all numeric elements in a list.

### Rules & Constraints:
1. Do not use `sum()`, loops (`for`, `while`), or comprehensions.
2. Do not mutate the list or slice the list (`numbers[1:]` is forbidden because it allocates new lists at every recursive call, making it $O(n^2)$ space).
3. Use the `index` parameter to track the current position.
4. If input is not a list, raise a `TypeError("Input must be a list")`.
5. An empty list `[]` must return `0`.

---

## Examples

```python
sum_list([1, 2, 3, 4, 5])  # 15
sum_list([10, -5, 2])       # 7
sum_list([])                # 0
sum_list([4.5, 2.5])        # 7.0
```

---

## Testing Your Solution
Run the test suite in this directory:
```bash
python test_exercise.py
```
