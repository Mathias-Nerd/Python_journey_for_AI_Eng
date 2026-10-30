# Drill 02: Safe Factorial

## Learning Target
Master input boundary validation, mathematical edge cases ($0! = 1$), and handling invalid domains (negative numbers and non-integers) recursively.

---

## Problem Statement

Write a function `factorial(n: int) -> int` that calculates the factorial of a non-negative integer $n$ recursively.

$$\text{factorial}(n) = n \times (n - 1) \times \dots \times 1$$
$$\text{factorial}(0) = 1$$

### Rules & Constraints:
1. Do not use loops (`for`, `while`) or `math.factorial`.
2. For $n < 0$, raise a `ValueError("Factorial is not defined for negative numbers")`.
3. For non-integer inputs (including `float`, `str`, `bool`), raise a `TypeError("Input must be an integer")`.
4. Must use recursion to compute the value.

---

## Examples

```python
factorial(5)  # 120 (5 * 4 * 3 * 2 * 1)
factorial(1)  # 1
factorial(0)  # 1 (by mathematical definition)
factorial(-2) # raises ValueError
factorial(3.5) # raises TypeError
```

---

## Testing Your Solution
Run the test suite in this directory:
```bash
python test_exercise.py
```
