# Deep-Dive Explanation: 16-class-decorator

## 💡 Algorithmic & Architectural Thinking

Decorators can mutate classes just as easily as functions:
- The class decorator receives the class object `cls`.
- We attach a new method implementation (`cls.__repr__ = __repr__`).
- Inside `__repr__`, `self.__dict__.items()` extracts all public and private instance attributes dynamically.
- The modified class object is returned.

---

## 📊 Complexity Analysis

- **Time Complexity**: $O(1)$ class mutation at definition time; $O(K)$ during `repr()` where $K$ is attribute count.
- **Space Complexity**: $O(1)$ overhead.
