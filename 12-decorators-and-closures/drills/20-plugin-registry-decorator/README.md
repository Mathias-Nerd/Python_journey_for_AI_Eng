# Drill 20: Plugin Registry Decorator

## Learning Target
Build extensible plugin architectures (like pytest, Flask route registers, or serializers) where functions register themselves into a central registry upon definition.

---

## Problem Statement

Implement `PluginRegistry`:
- `register(name: str) -> callable`: Decorator that registers the function under `name` in its internal dict.
- `get(name: str) -> callable`: Retrieves registered function (or raises `KeyError`).
- `all_plugins() -> dict`: Returns map of all registered plugins.

---

## Examples

```python
registry = PluginRegistry()

@registry.register("json")
def parse_json(raw): return f"json:{raw}"

registry.get("json")("data") # "json:data"
```
