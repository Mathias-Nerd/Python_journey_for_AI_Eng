# Drill 07: Fibonacci with Memoization

## Learning Target
Learn the critical difference between naive tree recursion $O(2^n)$ and memoized recursion $O(n)$, and how an optional state dictionary (or default accumulator) caches subproblem solutions.

---

## Problem Statement

Write a function `fibonacci(n: int, memo: dict | None = None) -> int` that recursively computes the $n$-th Fibonacci number.

$$	ext{fib}(0) = 0, \quad 	ext{fib}(1) = 1, \quad 	ext{fib}(n) = 	ext{fib}(n - 1) + 	ext{fib}(n - 2)$$

### Rules & Constraints:
1. Do not use loops (`for`, `while`) or external libraries (e.g. `functools.lru_cache`).
2. For $n < 0$, raise `ValueError("n must be non-negative")`.
3. For non-integer inputs (or `bool`), raise `TypeError("n must be an integer")`.
4. Must complete for $n = 50$ in under 1 second (verifying $O(n)$ memoization).

---

## Examples

```python
fibonacci(0)   # 0
fibonacci(1)   # 1
fibonacci(7)   # 13
fibonacci(50)  # 12586269025
```
