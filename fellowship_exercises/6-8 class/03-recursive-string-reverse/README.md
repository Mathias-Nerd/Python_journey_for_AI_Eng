# Drill 03: Recursive String Reversal

## Learning Target
Understand head-and-tail recursive decomposition on sequence data types without relying on indexing tricks or built-in reverse helpers.

---

## Problem Statement

Write a function `reverse_string(text: str) -> str` that recursively reverses a given string.

### Rules & Constraints:
1. Do not use `text[::-1]`, `reversed()`, loops (`for`, `while`), or `join()`.
2. Base case: an empty string `""` or a single-character string returns itself.
3. If input is not a `str`, raise a `TypeError("Input must be a string")`.
4. Recursive step: take a character from one end and combine it with the reversed remainder.

---

## Examples

```python
reverse_string("hello")  # "olleh"
reverse_string("a")      # "a"
reverse_string("")       # ""
reverse_string("12345")  # "54321"
```

---

## Testing Your Solution
Run the test suite in this directory:
```bash
python test_exercise.py
```
