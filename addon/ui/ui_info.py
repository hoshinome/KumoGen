
#####################################################################################################
#
# ooooo     ooo ooooo      ooooo              .o88o.           
# `888'     `8' `888'      `888'              888 `"           
#  888       8   888        888  ooo. .oo.   o888oo   .ooooo.  
#  888       8   888        888  `888P"Y88b   888    d88' `88b 
#  888       8   888        888   888   888   888    888   888 
#  `88.    .8'   888        888   888   888   888    888   888 
#    `YbodP'    o888o      o888o o888o o888o o888o   `Y8bod8P' 
#                          
#####################################################################################################                               

import bpy
from bpy.types import Panel, UILayout
from ..resources import icons
from ... import panel_label

class KUMOGEN_PT_info(Panel):
    bl_idname = "KUMOGEN_PT_info"
    bl_label = "Info"
    bl_category = panel_label
    bl_space_type  = "VIEW_3D"
    bl_region_type = "UI"
    bl_context     = ""
    bl_order       = 2

    def draw_header(self, context: bpy.types.Context):
        self.layout.label(icon_value=icons.get("K_info"))

    def draw(self, context):
        layout: UILayout = self.layout
        col = layout.column()
        col.scale_y = 1.25
        col.operator("wm.url_open", text="BOOTH", icon_value=icons.get("K_link")).url = "https://booth.pm/ja/items/6720921"
        col.operator("wm.url_open", text="GitHub", icon_value=icons.get("K_link")).url = "https://github.com/hoshinome/KumoGen"
        layout.separator()
        row = layout.row()
        row.alignment = "CENTER"
        row.label(text="KUMOGEN", icon_value=icons.get("K_kumogen"))

classes = (
    KUMOGEN_PT_info,
)