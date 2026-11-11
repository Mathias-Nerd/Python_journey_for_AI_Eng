"""
Solution for Drill 20: Plugin Registry
Module: 04-decorators-and-closures
"""


class PluginRegistry:
    """Decorator-based registry system for modular extensible plugins."""

    def __init__(self):
        self._registry = {}

    def register(self, name: str):
        """Decorator method that registers a plugin function under name."""
        def decorator(func: callable):
            self._registry[name] = func
            return func
        return decorator

    def get(self, name: str):
        """Retrieves registered plugin by name."""
        if name not in self._registry:
            raise KeyError(f"Plugin '{name}' not found")
        return self._registry[name]

    def all_plugins(self) -> list[str]:
        """Returns list of all registered plugin names."""
        return list(self._registry.keys())
