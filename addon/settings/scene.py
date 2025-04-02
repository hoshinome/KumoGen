import bpy
from bpy.props import EnumProperty
from bpy.types import PropertyGroup

class KumoGen_Scene(PropertyGroup):
    panel_tabs: EnumProperty(
        items=[
            ("Clouds", "Clouds", "Cloud Settings", "NONE", 0),
            ("Render", "Render", "Render Settings", "NONE", 1),
            ("Update", "", "Update Tab", "TOOL_SETTINGS", 2),
        ]
    )