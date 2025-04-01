import bpy
from bpy.props import BoolProperty
from bpy.types import PropertyGroup

class KumoGen_Tabs(PropertyGroup):
    layer: BoolProperty(
        name="Cloud Layers",
        default=True
    ) 
    basic_controls: BoolProperty(
        name="Basic Controls",
        default=True
    )
    gradient: BoolProperty(
        name="Gradient",
        default=False
    )
    layer_controls: BoolProperty(
        name="Layer Controls",
        default=True
    )
    mapping: BoolProperty(
        name="Mapping",
        default=False
    )
    decimate: BoolProperty(
        name="Decimate",
        default=False
    )
    scale: BoolProperty(
        name="Scale",
        default=False
    )
    
    clouds: BoolProperty(
        name="Clouds",
        default=True
    )
    
    cumulus: BoolProperty(
        name="Cumulus",
        default=True
    )

    cirrocumulus: BoolProperty(
        name="Cirrocumulus",
        default=True
    )

    stratocumulus: BoolProperty(
        name="Stratocumulus",
        default=True
    )

    altitude: BoolProperty(
        name="Altitude",
        default=True
    )