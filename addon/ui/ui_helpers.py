
#####################################################################################################
#
# ooooo     ooo ooooo    ooooo   ooooo           oooo
# `888'     `8' `888'    `888'   `888'           `888
#  888       8   888      888     888   .ooooo.   888  oo.ooooo.   .ooooo.  oooo d8b  .oooo.o
#  888       8   888      888ooooo888  d88' `88b  888   888' `88b d88' `88b `888""8P d88(  "8
#  888       8   888      888     888  888ooo888  888   888   888 888ooo888  888     `"Y88b.
#  `88.    .8'   888      888     888  888    .o  888   888   888 888    .o  888     o.  )88b
#    `YbodP'    o888o    o888o   o888o `Y8bod8P' o888o  888bod8P' `Y8bod8P' d888b    8""888P'
#                                                       888
#                                                      o888o
#
#####################################################################################################
import bpy
from ..resources import icons
from bpy.props import BoolProperty, EnumProperty
from bpy.types import PropertyGroup

# ooo        ooooo                    oooo           ooooooooooooo
# `88.       .888'                    `888           8'   888   `8
#  888b     d'888   .ooooo.   .oooo.o  888 .oo.           888      oooo    ooo oo.ooooo.   .ooooo.   .oooo.o 
#  8 Y88. .P  888  d88' `88b d88(  "8  888P"Y88b          888       `88.  .8'   888' `88b d88' `88b d88(  "8 
#  8  `888'   888  888ooo888 `"Y88b.   888   888          888        `88..8'    888   888 888ooo888 `"Y88b.  
#  8    Y     888  888    .o o.  )88b  888   888          888         `888'     888   888 888    .o o.  )88b 
# o8o        o888o `Y8bod8P' 8""888P' o888o o888o        o888o         .8'      888bod8P' `Y8bod8P' 8""888P' 
#                                                                  .o..P'       888
#                                                                  `Y8P'       o888o

class KUMOGEN_PG_mt(PropertyGroup):
    mesh_types: EnumProperty(
        name="Mesh Types",
        items=[("SPHERE", "Sphere", ""),
               ("CUBE", "Cube", "")],
        default="SPHERE",
    )

# oooooo   oooooo     oooo  o8o                    .o8                                ooo        ooooo
#  `888.    `888.     .8'   `"'                   "888                                `88.       .888'
#   `888.   .8888.   .8'   oooo  ooo. .oo.    .oooo888   .ooooo.  oooo oooo    ooo     888b     d'888   .oooo.   ooo. .oo.    .oooo.    .oooooooo  .ooooo.  oooo d8b
#    `888  .8'`888. .8'    `888  `888P"Y88b  d88' `888  d88' `88b  `88. `88.  .8'      8 Y88. .P  888  `P  )88b  `888P"Y88b  `P  )88b  888' `88b  d88' `88b `888""8P
#     `888.8'  `888.8'      888   888   888  888   888  888   888   `88..]88..8'       8  `888'   888   .oP"888   888   888   .oP"888  888   888  888ooo888  888
#      `888'    `888'       888   888   888  888   888  888   888    `888'`888'        8    Y     888  d8(  888   888   888  d8(  888  `88bod8P'  888    .o  888
#       `8'      `8'       o888o o888o o888o `Y8bod88P" `Y8bod8P'     `8'  `8'        o8o        o888o `Y888""8o o888o o888o `Y888""8o `8oooooo.  `Y8bod8P' d888b
#                                                                                                                                      d"     YD
#                                                                                                                                      "Y88888P'

class KUMOGEN_PG_wm(PropertyGroup):
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

classes = (
    KUMOGEN_PG_wm,
    KUMOGEN_PG_mt,
)