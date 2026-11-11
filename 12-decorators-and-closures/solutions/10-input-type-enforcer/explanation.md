# Deep-Dive Explanation: 10-input-type-enforcer

## 💡 Algorithmic & Architectural Thinking

Python is dynamically typed, but critical boundaries (e.g. data ingestion or RPC handlers) often require runtime type validation.
Important edge case: In Python, `bool` is a subclass of `int` (`isinstance(True, int) == True`). To strictly enforce integer parameters, we must explicitly check and reject boolean values when `exp_type is int`.

---

## 📊 Complexity Analysis

- **Time Complexity**: $O(A)$ where $A$ is the number of checked arguments.
- **Space Complexity**: $O(1)$ auxiliary memory.
