# Deep-Dive Explanation: 02-closure-state-accumulator

## 💡 Algorithmic & Architectural Thinking

A closure occurs when an inner function references variables from its enclosing outer scope.
- Without `nonlocal`, reassigning `total = total + amount` inside `accumulate` would cause Python to treat `total` as an uninitialized local variable (`UnboundLocalError`).
- The `nonlocal` keyword explicitly informs Python that `total` belongs to the nearest non-global enclosing scope.
- Each invocation of `make_accumulator` creates an independent environment in memory (`__closure__` cell).

---

## 📊 Complexity Analysis

- **Time Complexity**: $O(1)$ per accumulation call.
- **Space Complexity**: $O(1)$ persistent cell reference.
