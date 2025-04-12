
#####################################################################################################
# 
# ooooo     ooo ooooo      ooooo     ooo                  .o8                .             
# `888'     `8' `888'      `888'     `8'                 "888              .o8             
#  888       8   888        888       8  oo.ooooo.   .oooo888   .oooo.   .o888oo  .ooooo.  
#  888       8   888        888       8   888' `88b d88' `888  `P  )88b    888   d88' `88b 
#  888       8   888        888       8   888   888 888   888   .oP"888    888   888ooo888 
#  `88.    .8'   888        `88.    .8'   888   888 888   888  d8(  888    888 . 888    .o 
#    `YbodP'    o888o         `YbodP'     888bod8P' `Y8bod88P" `Y888""8o   "888" `Y8bod8P' 
#                                         888                                              
#                                        o888o                                             
# 
#####################################################################################################

import bpy
from bpy.types import Panel, UILayout, Context
from ... import addon_updater_ops, version, panel_label
from ..resources import icons

class KUMOGEN_PT_update(Panel):
    bl_idname      = "KUMOGEN_PT_update"
    bl_label       = "Update"
    bl_category    = panel_label
    bl_space_type  = "VIEW_3D"
    bl_region_type = "UI"
    bl_context     = ""
    bl_order       = 1
    bl_options = {'DEFAULT_CLOSED'}

    def draw_header(self, context: bpy.types.Context):
        self.layout.label(icon_value=icons.get("K_update"))
        
    def draw(self, context):
        addon_updater_ops.check_for_update_background()
        layout: UILayout = self.layout
        col = layout.column()
        col.scale_y = 0.7
        if addon_updater_ops.updater.update_ready:
            col.label(text="Update", icon="INFO")
        else:
            col.label(text="No Update", icon="CHECKMARK")
        col.label(text=f"Version: {version}")
        addon_updater_ops.update_notice_box_ui(self, context)

classes = (
    KUMOGEN_PT_update,
)