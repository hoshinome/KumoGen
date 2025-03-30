import bpy
from bpy.props import PointerProperty
from . import scene

classes = (
    scene.KumoGen_Scene,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.kumogen = PointerProperty(type = scene.KumoGen_Scene)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)