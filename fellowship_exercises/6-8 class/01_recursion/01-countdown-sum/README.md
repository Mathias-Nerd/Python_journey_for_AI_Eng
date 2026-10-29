# Drill 01: Countdown Sum of Odd Integers

## 🎯 Learning Target
Understand the foundational mechanics of the recursive call stack, base case conditions, and progression towards termination without relying on loops or built-in shortcuts.

---

## 📝 Problem Statement

Write a function `countdown_sum(n: int) -> int` that recursively computes the sum of **odd positive integers** from `n` down to `1`.

### Rules & Constraints:
1. **Forbidden**: Do NOT use `for` or `while` loops, `sum()`, list/set/dict comprehensions, or `count()`.
2. If `n <= 0`, return `0`.
3. If `n` is non-integer (e.g. `float` or `str`), raise a `TypeError`.
4. Your recursive call must make strict progress toward the base case.

---

## 💡 Examples

```python
countdown_sum(5)   # 9  (5 + 3 + 1)
countdown_sum(4)   # 4  (3 + 1)
countdown_sum(1)   # 1  (1)
countdown_sum(0)   # 0
countdown_sum(-5)  # 0
```

---

## 🔍 Tracing Guide
For `countdown_sum(5)`:
- `5` is odd, so it contributes `5 + countdown_sum(4)`.
- `4` is even, so it contributes `0 + countdown_sum(3)`.
- `3` is odd, so it contributes `3 + countdown_sum(2)`.
- `2` is even, so it contributes `0 + countdown_sum(1)`.
- `1` is odd, so it contributes `1 + countdown_sum(0)`.
- `0` is base case $\to$ returns `0`.
- Unwinds: $1 + 3 + 5 = 9$.

---

## 🧪 Testing Your Solution
Run the test suite in this directory:
```bash
python test_exercise.py
```
