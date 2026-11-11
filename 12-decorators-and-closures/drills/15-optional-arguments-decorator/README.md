# Drill 15: Optional Arguments Decorator

## Learning Target
Learn the advanced Python pattern of decorators that can be used **with or without parentheses**:
`@prefix` OR `@prefix(tag="LOG")`

---

## Problem Statement

Write a decorator `prefix`:
- If used as `@prefix`, defaults tag to `"INFO"`.
- If used as `@prefix(tag="CUSTOM")`, uses the specified tag.
- Prepends `f"[{tag}] "` to string returns.

---

## Examples

```python
@prefix
def msg1(): return "hello"
msg1() # "[INFO] hello"

@prefix(tag="DEBUG")
def msg2(): return "world"
msg2() # "[DEBUG] world"
```
