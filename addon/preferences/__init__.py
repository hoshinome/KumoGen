
#####################################################################################################
#
# ooooooooo.                       .o88o.
# `888   `Y88.                     888 `"
#  888   .d88' oooo d8b  .ooooo.  o888oo   .ooooo.  oooo d8b  .ooooo.  ooo. .oo.    .ooooo.   .ooooo.   .oooo.o
#  888ooo88P'  `888""8P d88' `88b  888    d88' `88b `888""8P d88' `88b `888P"Y88b  d88' `"Y8 d88' `88b d88(  "8
#  888          888     888ooo888  888    888ooo888  888     888ooo888  888   888  888       888ooo888 `"Y88b.
#  888          888     888    .o  888    888    .o  888     888    .o  888   888  888   .o8 888    .o o.  )88b
# o888o        d888b    `Y8bod8P' o888o   `Y8bod8P' d888b    `Y8bod8P' o888o o888o `Y8bod8P' `Y8bod8P' 8""888P'
#
#####################################################################################################

import bpy
from . import preferences_update

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
classes +=  preferences_update.classes

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)