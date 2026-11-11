# Deep-Dive Explanation: 08-execution-timer

## 💡 Algorithmic & Architectural Thinking

`time.perf_counter()` provides the highest available resolution clock on the system and is monotonic (not subject to system clock adjustments or daylight saving changes).
Measuring duration before and after execution allows profiling bottlenecks non-invasively.

---

## 📊 Complexity Analysis

- **Time Complexity**: Two $O(1)$ clock queries.
- **Space Complexity**: $O(1)$ float storage.
