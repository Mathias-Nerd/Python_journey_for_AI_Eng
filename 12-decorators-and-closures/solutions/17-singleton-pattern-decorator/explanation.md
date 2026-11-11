# Deep-Dive Explanation: 17-singleton-pattern-decorator

## 💡 Algorithmic & Architectural Thinking

The Singleton pattern guarantees that a class has only one instance and provides a global access point to it:
- The closure variable `instances` stores created instances keyed by `cls`.
- Subsequent instantiations return the pre-existing cached instance rather than constructing a new one.

---

## 📊 Complexity Analysis

- **Time Complexity**: $O(1)$ dictionary lookup on subsequent instantiations.
- **Space Complexity**: $O(1)$ reference storage.
