# Deep-Dive Explanation: 09-memoization-cache

## 💡 Algorithmic Thinking

Memoization trades memory for speed by caching the output of deterministic functions:
- To use `args` and `kwargs` as a dictionary key, they must be hashable.
- `args` is already a tuple (hashable).
- `kwargs` is a dictionary, which is unhashable; converting `kwargs.items()` to a sorted tuple makes it hashable and deterministic.
- Cache lookups run in expected $O(1)$ time.

---

## 📊 Complexity Analysis

- **Time Complexity**: $O(1)$ expected on cache hit; $O(T_{\text{func}})$ on cache miss.
- **Space Complexity**: $O(U)$ where $U$ is the number of unique argument signatures called.
