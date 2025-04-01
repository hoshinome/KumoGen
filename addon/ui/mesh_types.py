import bpy
from bpy.props import EnumProperty
from bpy.types import PropertyGroup

class KumoGen_MeshTypes(PropertyGroup):
    mesh_types: EnumProperty(
        name="Mesh",
        items=[("SPHERE", "Sphere", ""),
               ("CUBE", "Cube", "")],
        default="SPHERE",
    )