import bpy
from . import (ui,
               operator,
               settings,
               preferences,
               resources)

modules = (
    ui,
    operator,
    settings,
    preferences,
    resources,
)

def register():
    for mod in modules:
        mod.register()

def unregister():
    for mod in reversed(modules):
        mod.unregister()