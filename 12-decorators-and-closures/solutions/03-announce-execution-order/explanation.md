# Deep-Dive Explanation: 03-announce-execution-order

## 💡 Algorithmic & Architectural Thinking

Understanding decorator evaluation timing is critical:
1. **Decoration Time**: Executes immediately when the module is imported or defined (`log_list.append("DECORATION")`).
2. **Call Time (Before)**: Intercepts before the wrapped function executes (`BEFORE`).
3. **Wrapped Execution**: The original target function runs.
4. **Call Time (After)**: Post-processing runs before returning to the caller (`AFTER`).

---

## 📊 Complexity Analysis

- **Decoration Cost**: $O(1)$ single execution at definition.
- **Call Cost**: $O(1)$ overhead plus runtime of `func`.
