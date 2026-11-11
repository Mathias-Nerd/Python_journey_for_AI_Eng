# Deep-Dive Explanation: 11-retry-on-exception

## 💡 Algorithmic & Architectural Thinking

Transient network glitches, database deadlocks, and rate limits frequently resolve upon immediate retry:
- We catch only specified exception types (`exceptions: tuple`).
- If an unhandled exception occurs, it bubbles up immediately without consuming retry attempts.
- If all `max_attempts` fail, the final exception is re-raised with its original traceback intact.

---

## 📊 Complexity Analysis

- **Time Complexity**: $O(K \times T_{\text{func}})$ where $K \le \text{max\_attempts}$.
- **Space Complexity**: $O(1)$ auxiliary overhead.
