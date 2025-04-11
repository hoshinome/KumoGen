import bpy
from ..resources import icons
from bpy.props import EnumProperty
from bpy.types import PropertyGroup

class KUMOGEN_PG_tabs(PropertyGroup):
    panel_tabs: EnumProperty(
        items=[
            ("Clouds", "Clouds", "Cloud Settings", "NONE", 0),
            ("Render", "Render", "Render Settings", "NONE", 1),
        ]
    )

classes = (
    KUMOGEN_PG_tabs,
)