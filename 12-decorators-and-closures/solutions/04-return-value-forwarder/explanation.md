# Deep-Dive Explanation: 04-return-value-forwarder

## 💡 Algorithmic & Architectural Thinking

A frequent pitfall in custom decorators is forgetting to return the result of `func(*args, **kwargs)`, causing wrapped functions to return `None` silently.
`forward_result` guarantees that whatever `func` produces (integers, strings, falsy values like `[]`, `None`, or `0`) is faithfully forwarded back to the caller.

---

## 📊 Complexity Analysis

- **Time Complexity**: $O(1)$ decorator overhead.
- **Space Complexity**: $O(1)$ auxiliary memory.
