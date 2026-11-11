# Deep-Dive Explanation: 06-metadata-preserver

## 💡 Algorithmic & Architectural Thinking

When a function is replaced by a wrapper, its `__name__`, `__doc__`, and `__annotations__` are replaced by the wrapper's metadata unless preserved.
`@functools.wraps(func)` copies these internal attributes (and adds `__wrapped__`), ensuring documentation generators (Sphinx), debuggers, and introspection tools see the original function's true identity.

---

## 📊 Complexity Analysis

- **Time Complexity**: $O(1)$ metadata copy at decoration time.
- **Space Complexity**: $O(1)$ auxiliary overhead.
