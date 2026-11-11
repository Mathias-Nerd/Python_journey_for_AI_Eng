# Deep-Dive Explanation: 19-circuit-breaker

## 💡 Algorithmic & Architectural Thinking

The Circuit Breaker pattern prevents catastrophic cascading failure across microservices:
- **CLOSED**: Requests flow normally. If a call fails, `failures` count increments.
- **OPEN**: When `failures >= failure_threshold`, the circuit trips open. Subsequent calls fail immediately (`RuntimeError`) without hitting the downstream resource, protecting it from being overwhelmed.

---

## 📊 Complexity Analysis

- **Time Complexity**: $O(1)$ state verification check before execution.
- **Space Complexity**: $O(1)$ state tracking in closure.
