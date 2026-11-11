# Deep-Dive Explanation: 07-call-counter-decorator

## 💡 Algorithmic & Architectural Thinking

Functions in Python are full objects. You can attach arbitrary attributes to them:
```python
wrapper.calls = 0
```
Inside `wrapper`, each invocation increments `wrapper.calls += 1`. This pattern avoids the need for global state or external dictionaries for invocation counting.

---

## 📊 Complexity Analysis

- **Time Complexity**: $O(1)$ integer increment per call.
- **Space Complexity**: $O(1)$ memory.
