
#####################################################################################################
#
# ooooo     ooo ooooo 
# `888'     `8' `888' 
#  888       8   888  
#  888       8   888  
#  888       8   888  
#  `88.    .8'   888  
#    `YbodP'    o888o
# 
#####################################################################################################

import bpy
from bpy.props import PointerProperty
from . import ui_info, ui_panel, ui_update, ui_helpers

# ooooooooo.
# `888   `Y88.
#  888   .d88'  .ooooo.   .oooooooo 
#  888ooo88P'  d88' `88b 888' `88b  
#  888`88b.    888ooo888 888   888  
#  888  `88b.  888    .o `88bod8P'  
# o888o  o888o `Y8bod8P' `8oooooo.  
#                        d"     YD  
#                        "Y88888P'  

classes  =  []
classes +=  ui_panel.classes
classes +=  ui_update.classes
classes +=  ui_info.classes
classes +=  ui_helpers.classes

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.kumogen_WM = PointerProperty(type=ui_helpers.KUMOGEN_PG_wm)
    bpy.types.WindowManager.MeshTypes = PointerProperty(type=ui_helpers.KUMOGEN_PG_mt)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
