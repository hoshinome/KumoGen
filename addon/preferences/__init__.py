import bpy
from . import preferences

classes = (
    preferences.KumoGen_Updater_Preferences,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)