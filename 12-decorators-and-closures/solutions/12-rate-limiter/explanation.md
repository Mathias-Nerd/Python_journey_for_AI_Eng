# Deep-Dive Explanation: 12-rate-limiter

## 💡 Algorithmic Thinking

We implement the **Sliding Window Log** algorithm:
1. Maintain a queue of invocation timestamps (`deque`).
2. Upon invocation, evict all timestamps that fall outside the active window (`now - timestamp >= period_seconds`).
3. If the count of remaining timestamps reaches `max_calls`, reject the call by raising `RuntimeError`.
4. Otherwise, record `now` and proceed.

---

## 📊 Complexity Analysis

- **Time Complexity**: Amortized $O(1)$ per call (each timestamp is enqueued and dequeued once).
- **Space Complexity**: $O(M)$ where $M = \text{max\_calls}$.
