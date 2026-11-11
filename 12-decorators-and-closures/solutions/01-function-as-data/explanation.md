# Deep-Dive Explanation: 01-function-as-data

## 💡 Algorithmic & Architectural Thinking

In Python, functions are first-class citizens. They can be:
1. Created dynamically at runtime inside other functions.
2. Passed as arguments to other functions.
3. Returned from functions as return values.
4. Stored in data structures like lists and dictionaries.

`make_multiplier` creates a closure over `factor`. `apply_pipeline` chains these first-class callables into a sequential transformation pipeline.

---

## 📊 Complexity Analysis

- **`make_multiplier`**: $O(1)$ time, $O(1)$ space.
- **`apply_pipeline`**: $O(N \times K)$ where $N$ is data length and $K$ is number of operations.
