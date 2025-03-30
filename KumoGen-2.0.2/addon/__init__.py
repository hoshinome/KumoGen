import bpy
from . import ui, operator, settings, updater, preferences

modules = (
    ui,
    operator,
    settings,
    preferences,
    updater
)

def register():
    for mod in modules:
        mod.register()

def unregister():
    for mod in reversed(modules):
        mod.unregister()