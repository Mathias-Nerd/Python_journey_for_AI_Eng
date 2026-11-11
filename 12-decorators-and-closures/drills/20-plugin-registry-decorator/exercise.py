"""
Drill 20: Plugin Registry Decorator
Module: 04-decorators-and-closures
"""


class PluginRegistry:
    """
    Central registry for dynamically registered plugins via @registry.register.
    """

    def __init__(self):
        self._plugins = {}

    def register(self, name: str) -> callable:
        """
        Decorator registering func in self._plugins under name.
        """
        # TODO: Implement decorator registering function
        pass

    def get(self, name: str) -> callable:
        # TODO: Retrieve plugin or raise KeyError
        pass

    def all_plugins(self) -> dict:
        return dict(self._plugins)
