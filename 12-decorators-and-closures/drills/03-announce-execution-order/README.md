# Drill 03: Announce Execution Order (Quest 4)

## Learning Target
Understand Quest 4 from the assessment: Why top-level decorator code runs at **definition/decoration time**, while wrapper code runs at **call time**.

---

## Problem Statement

Write a decorator `announce(log_list: list[str])` that tracks execution events:
1. When `@announce(events)` decorates a function, append `"DECORATION"` to `log_list`.
2. When the decorated function is called:
   - Append `"BEFORE"` to `log_list`.
   - Call the original function and capture its result.
   - Append `"AFTER"` to `log_list`.
   - Return the result.

---

## Examples

```python
events = []

@announce(events)
def add(a, b):
    events.append("RUNNING")
    return a + b

# events == ["DECORATION"] (before add is ever called!)

res = add(2, 3)
# res == 5
# events == ["DECORATION", "BEFORE", "RUNNING", "AFTER"]
```
