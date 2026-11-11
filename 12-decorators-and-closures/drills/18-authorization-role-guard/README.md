# Drill 18: Role-Based Authorization Guard

## Learning Target
Implement access control gates (common in web frameworks like Flask, FastAPI, Django) using decorators.

---

## Problem Statement

Write a decorator `require_role(required_role: str, user_getter: callable)`:
- `user_getter(*args, **kwargs)` extracts the current user dict (e.g. `{"role": "admin"}`).
- If user's role matches `required_role`, execute `func`.
- Otherwise, raise `PermissionError("Access denied: requires role <role>")`.

---

## Examples

```python
user = {"role": "guest"}

@require_role("admin", user_getter=lambda *a, **kw: user)
def delete_database():
    return "deleted"

delete_database() # raises PermissionError!
```
