import bpy
from bpy.props import PointerProperty
from . import mesh_types, panel, tabs

classes = (
    panel.KumoGen_Panel,
    tabs.KumoGen_Tabs,
    mesh_types.KumoGen_MeshTypes,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.WindowManager.KumoGen_Tabs = PointerProperty(type=tabs.KumoGen_Tabs)
    bpy.types.WindowManager.KumoGen_Mesh_Types = PointerProperty(type=mesh_types.KumoGen_MeshTypes)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
