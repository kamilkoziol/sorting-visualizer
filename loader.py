import importlib
from typing import List


class PluginInterface:

    @staticmethod
    def initialize() -> None:
        pass

def import_module(name: str):
    return importlib.import_module(name["algorithm"])

def load_plugins(plugins: List[str]) -> None:
    for plugin_name in plugins:
        plugin = import_module(plugin_name)
        plugin.initialize()


