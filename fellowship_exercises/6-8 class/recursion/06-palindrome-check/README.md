# Drill 06: Recursive Palindrome Check

## Learning Target
Learn two-pointer recursive convergence (shrinking from both ends simultaneously toward the center).

---

## Problem Statement

Write a function `is_palindrome(text: str, left: int = 0, right: int | None = None) -> bool` that returns `True` if `text` is a palindrome, and `False` otherwise.

### Rules & Constraints:
1. Do not use `text[::-1]`, `reversed()`, loops (`for`, `while`), or list conversion.
2. Comparison should be case-sensitive.
3. Use two pointer indices (`left` and `right`) to avoid slicing the string.
4. If input is not a `str`, raise `TypeError("Input must be a string")`.
5. Empty string `""` and single-character strings are palindromes by definition.

---

## Examples

```python
is_palindrome("racecar")  # True
is_palindrome("madam")    # True
is_palindrome("noon")     # True
is_palindrome("python")   # False
is_palindrome("")         # True
is_palindrome("a")        # True
```

---

## Testing Your Solution
Run the test suite in this directory:
```bash
python test_exercise.py
```
