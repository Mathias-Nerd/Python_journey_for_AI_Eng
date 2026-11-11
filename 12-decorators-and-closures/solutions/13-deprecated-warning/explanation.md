# Deep-Dive Explanation: 13-deprecated-warning

## 💡 Algorithmic & Architectural Thinking

`warnings.warn` provides standard Python library deprecation signaling:
- `category=DeprecationWarning` allows developer environments and linters to catch obsolete API usage without halting production code.
- `stacklevel=2` ensures the warning points to the caller of the deprecated function rather than the line inside the decorator wrapper.

---

## 📊 Complexity Analysis

- **Time Complexity**: $O(1)$ warning dispatch overhead.
- **Space Complexity**: $O(1)$ memory.
