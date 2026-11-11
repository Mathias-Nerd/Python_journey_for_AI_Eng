# Deep-Dive Explanation: 05-arguments-forwarder

## 💡 Algorithmic & Architectural Thinking

Using `*args` and `**kwargs` allows the wrapper to accept any call signature without knowing parameter names in advance.
Assigning attributes (`last_args`, `last_kwargs`) directly onto `wrapper` turns the wrapper into an inspectable callable, enabling testing and auditing frameworks to verify function invocations.

---

## 📊 Complexity Analysis

- **Time Complexity**: $O(1)$ attribute assignment overhead.
- **Space Complexity**: $O(A + K)$ to store references to arguments.
