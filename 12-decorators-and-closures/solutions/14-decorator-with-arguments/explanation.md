# Deep-Dive Explanation: 14-decorator-with-arguments

## 💡 Algorithmic & Architectural Thinking

When a decorator accepts configuration arguments (`@repeat(num_times=4)`), a 3-level function nesting hierarchy is required:
1. **Outer Factory** (`repeat`): Receives configuration arguments (`num_times`).
2. **Intermediate Decorator** (`decorator`): Receives the target function (`func`).
3. **Inner Wrapper** (`wrapper`): Receives runtime function arguments (`*args, **kwargs`).

---

## 📊 Complexity Analysis

- **Time Complexity**: $O(K \times T_{\text{func}})$ where $K = \text{num\_times}$.
- **Space Complexity**: $O(1)$ auxiliary overhead.
