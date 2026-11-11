# Deep-Dive Explanation: 15-optional-arguments-decorator

## 💡 Algorithmic & Architectural Thinking

Supporting both `@prefix` (no parentheses) and `@prefix(tag="CUSTOM")` (with arguments) requires checking whether the first positional argument `_func` is a callable:
- If called without arguments (`@prefix`), Python passes the decorated function as `_func`. `prefix` returns `decorator(_func)`.
- If called with arguments (`@prefix(tag="ALERT")`), `_func` is `None` and keyword arguments are bound. `prefix` returns `decorator`.

---

## 📊 Complexity Analysis

- **Time Complexity**: $O(1)$ decorator dispatch.
- **Space Complexity**: $O(1)$ memory.
