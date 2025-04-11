
#####################################################################################################
#
#  .oooooo..o               .       .    o8o
# d8P'    `Y8             .o8     .o8    `"'
# Y88bo.       .ooooo.  .o888oo .o888oo oooo  ooo. .oo.    .oooooooo  .oooo.o
#  `"Y8888o.  d88' `88b   888     888   `888  `888P"Y88b  888' `88b  d88(  "8
#      `"Y88b 888ooo888   888     888    888   888   888  888   888  `"Y88b.
# oo     .d8P 888    .o   888 .   888 .  888   888   888  `88bod8P'  o.  )88b
# 8""88888P'  `Y8bod8P'   "888"   "888" o888o o888o o888o `8oooooo.  8""888P'
#                                                         d"     YD
#                                                         "Y88888P'
#
#####################################################################################################

import bpy
from bpy.props import PointerProperty
from . import scene

# ooooooooo.
# `888   `Y88.
#  888   .d88'  .ooooo.   .oooooooo 
#  888ooo88P'  d88' `88b 888' `88b  
#  888`88b.    888ooo888 888   888  
#  888  `88b.  888    .o `88bod8P'  
# o888o  o888o `Y8bod8P' `8oooooo.  
#                        d"     YD  
#                        "Y88888P'  

classes = []
classes +=  scene.classes

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.kumogen = PointerProperty(type = scene.KUMOGEN_PG_tabs)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)