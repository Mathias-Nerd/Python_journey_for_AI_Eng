# Deep-Dive Explanation: 18-authorization-role-guard

## 💡 Algorithmic & Architectural Thinking

Separation of concerns is one of the premier use cases for decorators:
- Business logic in `func` remains clean of authentication boilerplate.
- `user_getter` decouples authorization from HTTP request contexts, thread-local storage, or dependency injection containers.
- If role authorization fails, a `PermissionError` halts execution before `func` ever runs.

---

## 📊 Complexity Analysis

- **Time Complexity**: $O(1)$ role check overhead.
- **Space Complexity**: $O(1)$ memory.
