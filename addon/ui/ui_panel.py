
#####################################################################################################
#
# ooooo     ooo ooooo    ooooooooo.                                   oooo  
# `888'     `8' `888'    `888   `Y88.                                 `888
#  888       8   888      888   .d88'  .oooo.   ooo. .oo.    .ooooo.   888
#  888       8   888      888ooo88P'  `P  )88b  `888P"Y88b  d88' `88b  888
#  888       8   888      888          .oP"888   888   888  888ooo888  888
#  `88.    .8'   888      888         d8(  888   888   888  888    .o  888
#    `YbodP'    o888o    o888o        `Y888""8o o888o o888o `Y8bod8P' o888o
#
#####################################################################################################

import bpy
from bpy.types import Panel, UILayout, Context
from ..resources import icons
from ..utils import ui
from ..settings.scene import KUMOGEN_PG_tabs
from ... import addon_updater_ops, version, panel_label

#   .oooooo.   oooo                              .o8
#  d8P'  `Y8b  `888                             "888
# 888           888   .ooooo.  oooo  oooo   .oooo888   .oooo.o 
# 888           888  d88' `88b `888  `888  d88' `888  d88(  "8 
# 888           888  888   888  888   888  888   888  `"Y88b.  
# `88b    ooo   888  888   888  888   888  888   888  o.  )88b 
#  `Y8bood8P'  o888o `Y8bod8P'  `V88V"V8P' `Y8bod88P" 8""888P' 

def draw_clouds (self, context):
    wm = bpy.context.window_manager.MeshTypes
    layout = self.layout
    layout.prop(wm, "mesh_types", text="")
    col = layout.column(align=True)
    row = col.row(align=True)
    row.scale_x = 1.5
    row.scale_y = 2
    row.operator("kumogen.addclouds", text="Import Clouds",icon_value=icons.get("K_cloud"))
    row.alert = True
    row.operator("kumogen.deleteclouds",text="",icon="TRASH")
    wm = context.scene.kumogen_WM
    #Panel
    if "KumoGen-Sphere" in bpy.data.objects or "KumoGen-Cube" in bpy.data.objects:
        #Object Settings
        box = self.layout.box()
        box.label(text="Object Settings:", icon="OBJECT_DATA")
        if "KumoGen-Cube" in bpy.data.objects:
            ui.kumogen_tabs(box, wm, "altitude", "Altitude")
            if wm.altitude:
                box.prop(bpy.data.objects["KumoGen-Cube"], "location", index=2, text="Cloud Altitude")
        if "KumoGen-Sphere" in bpy.data.objects:
            ui.kumogen_tabs(box, wm, "decimate", "Decimate")
            if wm.decimate:
                box_Decimate = box.box()
                box_Decimate.label(text="Decimate:", icon="MOD_DECIM")
                box_Decimate.prop(bpy.data.objects["KumoGen-Sphere"].modifiers["Decimate"], "ratio", text="Ratio",)
            ui.kumogen_tabs(box, wm, "scale", "Scale")
            if wm.scale:
                box_Scale = box.box()
                box_Scale.label(text="Scale:", icon="EMPTY_ARROWS")
                box_Scale.prop(bpy.data.objects["KumoGen-Sphere"], "scale", text="Scale")
        # Shader Settings
        box = self.layout.box()
        box.label(text="Shader Settings:", icon="SHADING_RENDERED")
        ui.kumogen_tabs(box, wm, "basic_controls", "Basic Controls")
        if wm.basic_controls:
            box2 = box.box()
            box2.label(text="Basic Controls:", icon="ANCHOR_CENTER")
            box2.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[3], "default_value", text="Color")
            box2.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[86], "default_value", text="Animation")
            box2.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[4], "default_value", text="Density")
            box2.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[5], "default_value", text="Seed")
        if "KumoGen-Sphere" in bpy.data.collections:
            ui.kumogen_tabs(box, wm, "gradient", "Gradient")
            if wm.gradient:
                box2 = box.box()
                box2.label(text="Gradient:", icon="GP_MULTIFRAME_EDITING")
                box2.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[7], "default_value", text="Gradient")
                box2.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[8], "default_value", text="Scale")
                box2.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[9], "default_value", text="Detail")
        ui.kumogen_tabs(box, wm, "clouds", "Clouds")
        if wm.clouds:
            box2 = box.box()
            box2.label(text="Clouds", icon="OUTLINER_OB_VOLUME")
            box2.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[0], "default_value", text="Cumulus")
            box2.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[1], "default_value", text="Cirrocumulus")
            box2.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[2], "default_value", text="Stratocumulus")
        ui.kumogen_tabs(box, wm, "layer", "Cloud Layers")
        if wm.layer:
            box2 = box.box()
            box2.label(text="Cloud Layers:", icon="MOD_INSTANCE")
            if bool(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[0].default_value):
                box3 = box2.box()
                box3.label(text="Cumulus:")
                box3.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[11], "default_value", text="Layer 1")
                box3.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[12], "default_value", text="Layer 2")
            if bool(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[1].default_value):
                box3 = box2.box()
                box3.label(text="Cirrocumulus:")
                box3.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[32], "default_value", text="Layer 1")
                box3.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[33], "default_value", text="Layer 2")
            if bool(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[2].default_value):
                box3 = box2.box()
                box3.label(text="Stratocumulus:")
                box3.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[57], "default_value", text="Layer 1")
                box3.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[58], "default_value", text="Layer 2")
        ui.kumogen_tabs(box, wm, "layer_controls", "Layer Controls")
        if wm.layer_controls:
            box2 = box.box()
            box2.label(text="Layer Controls:", icon="MOD_HUE_SATURATION")
            layer_controls(box2, wm)
        ui.kumogen_tabs(box, wm, "mapping", "Mapping")
        if wm.mapping:
            box2 = box.box()
            box2.label(text="Mapping:", icon="EMPTY_AXIS")
            box2.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[82], "default_value", text="Location")
            box2.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[83], "default_value", text="Rotation")
            if "KumoGen-Cube" in bpy.data.objects:
                box2.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Scale"].inputs[2], "default_value", text="Scale")
            elif "KumoGen-Sphere" in bpy.data.objects:
                box2.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Scale"].inputs[1], "default_value", text="Scale")

# 88        db    Yb  dP 888888 88""Yb      dP""b8  dP"Yb  88b 88 888888 88""Yb  dP"Yb  88     .dP"Y8 
# 88       dPYb    YbdP  88__   88__dP     dP   `" dP   Yb 88Yb88   88   88__dP dP   Yb 88     `Ybo." 
# 88  .o  dP__Yb    8P   88""   88"Yb      Yb      Yb   dP 88 Y88   88   88"Yb  Yb   dP 88  .o o.`Y8b 
# 88ood8 dP""""Yb  dP    888888 88  Yb      YboodP  YbodP  88  Y8   88   88  Yb  YbodP  88ood8 8bodP' 

#---Cumulus---
def layer_controls(box2,wm):
    if (bool(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[0].default_value) and
        bool(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[11].default_value) or 
        bool(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[12].default_value)):
        ui.kumogen_tabs(box2, wm, "cumulus", "Cumulus")
        if wm.cumulus:
            # Layer 1
            if bool(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[11].default_value):
                box3 = box2.box()
                box3.label(text="Layer 1:")
                box3.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[14], "default_value", text="Coverage")
                box3.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[15], "default_value", text="Scale")
                box3.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[16], "default_value", text="Detail")
                box3.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[17], "default_value", text="Roughness")
                box3.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[18], "default_value", text="Distortion")
                box3.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[19], "default_value", text="Location X")
                box3.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[20], "default_value", text="Location Y")
                box3.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[21], "default_value", text="Rotation")
            # Layer 2
            if bool(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[12].default_value):
                box3 = box2.box()
                box3.label(text="Layer 2:")
                box3.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[23], "default_value", text="Coverage")
                box3.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[24], "default_value", text="Scale")
                box3.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[25], "default_value", text="Detail")
                box3.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[26], "default_value", text="Roughness")
                box3.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[27], "default_value", text="Distortion")
                box3.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[28], "default_value", text="Location X")
                box3.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[29], "default_value", text="Location Y")
                box3.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[30], "default_value", text="Rotation")
#---Ciccrocumulus---
    if (bool(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[1].default_value) and
        bool(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[32].default_value) or
        bool(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[33].default_value)):
        ui.kumogen_tabs(box2, wm, "cirrocumulus", "Cirrocumulus")
        if wm.cirrocumulus:
            #Layer 1
            if bool(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[32].default_value):
                box3 = box2.box()
                box3.label(text="Layer 1:")
                box3.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[35], "default_value", text="Coverage")
                box3.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[36], "default_value", text="Scale")
                box3.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[37], "default_value", text="Detail")
                box3.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[38], "default_value", text="Roughness")
                box3.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[39], "default_value", text="Distortion")
                box3.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[40], "default_value", text="Location X")
                box3.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[41], "default_value", text="Location Y")
                box3.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[42], "default_value", text="Rotation")
            # Layer 2
            if bool(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[33].default_value):
                box3 = box2.box()
                box3.label(text="Layer 2:")
                box3.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[46], "default_value", text="Coverage")
                box3.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[47], "default_value", text="Scale")
                box3.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[48], "default_value", text="Detail")
                box3.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[49], "default_value", text="Roughness")
                box3.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[50], "default_value", text="Distortion")
                box3.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[51], "default_value", text="Location X")
                box3.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[52], "default_value", text="Location Y")
                box3.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[53], "default_value", text="Rotation")
#---Stratocumulus---
    if (bool(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[2].default_value) and
        bool(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[57].default_value) or
        bool(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[58].default_value)):
        ui.kumogen_tabs(box2, wm, "stratocumulus", "Stratocumulus")
        if wm.stratocumulus:
            #Layer 1
            if bool(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[57].default_value):
                box3 =box2.box()
                box3.label(text="Layer 1:")
                box3.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[60], "default_value", text="Coverage")
                box3.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[61], "default_value", text="Scale")
                box3.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[62], "default_value", text="Detail")
                box3.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[63], "default_value", text="Roughness")
                box3.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[64], "default_value", text="Distortion")
                box3.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[65], "default_value", text="Noise Scale")
                box3.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[66], "default_value", text="Noise Detail")
                box3.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[67], "default_value", text="Location X")
                box3.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[68], "default_value", text="Location Y")
                box3.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[69], "default_value", text="Rotation")
            #Layer 2
            if bool(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[58].default_value):
                box3 =box2.box()
                box3.label(text="Layer 2:")
                box3.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[71], "default_value", text="Coverage")
                box3.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[72], "default_value", text="Scale")
                box3.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[73], "default_value", text="Detail")
                box3.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[74], "default_value", text="Roughness")
                box3.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[75], "default_value", text="Distortion")
                box3.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[76], "default_value", text="Noise Scale")
                box3.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[77], "default_value", text="Noise Detail")
                box3.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[78], "default_value", text="Location X")
                box3.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[79], "default_value", text="Location Y")
                box3.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[80], "default_value", text="Rotation")

# ooooooooo.                               .o8
# `888   `Y88.                            "888
#  888   .d88'  .ooooo.  ooo. .oo.    .oooo888   .ooooo.  oooo d8b
#  888ooo88P'  d88' `88b `888P"Y88b  d88' `888  d88' `88b `888""8P
#  888`88b.    888ooo888  888   888  888   888  888ooo888  888
#  888  `88b.  888    .o  888   888  888   888  888    .o  888
# o888o  o888o `Y8bod8P' o888o o888o `Y8bod88P" `Y8bod8P' d888b

def draw_render(self,context,scene):
    cscene = scene.cycles
    layout = self.layout
    col = layout.column(align=True)
    col.scale_x = 2
    col.scale_y = 1.5
    col.operator("kumogen.render", text="Render Setting")
    layout.label(text="Format:")
    layout.prop(context.scene.render, "use_border", text="Camera Render Region")
    layout.prop(context.space_data, "use_render_border", text="Viewport Render Region")
    layout.label(text="Light Paths:")
    layout.prop(cscene, "use_fast_gi", text="Fast GI Approximation")
    layout.label(text="Volumes:")
    layout.prop(cscene, "volume_step_rate", text="Step Rate Render")
    layout.prop(cscene, "volume_preview_step_rate", text="Viewport")
    layout.label(text="Clip End")
    layout.prop(context.space_data, "clip_end", text="View End")
    if context.scene.camera:
        layout.prop(scene.camera.data, "clip_end", text="Camera End")

#   .oooooo.   oooo
#  d8P'  `Y8b  `888
# 888           888   .oooo.    .oooo.o  .oooo.o  .ooooo.   .oooo.o
# 888           888  `P  )88b  d88(  "8 d88(  "8 d88' `88b d88(  "8
# 888           888   .oP"888  `"Y88b.  `"Y88b.  888ooo888 `"Y88b.
# `88b    ooo   888  d8(  888  o.  )88b o.  )88b 888    .o o.  )88b
#  `Y8bood8P'  o888o `Y888""8o 8""888P' 8""888P' `Y8bod8P' 8""888P'

class KUMOGEN_PT_main(Panel):
    bl_idname      = "KUMOGEN_PT_main"
    bl_label       = "KumoGen"
    bl_category    = panel_label
    bl_space_type  = "VIEW_3D"
    bl_region_type = "UI"
    bl_context     = ""
    bl_order       = 0

    def draw_header(self, context: bpy.types.Context):
        self.layout.label(icon_value=icons.get("K_kumogen"))
    
    def draw_header_preset(self, context: Context):
        self.layout.label(text=f"v{version}")

    def draw(self, context):
        addon_updater_ops.check_for_update_background()
        layout = self.layout
        scn_sets: 'KUMOGEN_PG_tabs' = context.scene.kumogen
        self.scn_sets = scn_sets
        scene = context.scene
        row = layout.row(align=True)
        row.scale_y = 1.5
        row.prop(context.scene.kumogen, "panel_tabs", expand=True)
        #---Render---
        if scn_sets.panel_tabs == "Render":
            draw_render(self,context,scene)
        #---Clouds---
        if scn_sets.panel_tabs == "Clouds":
            draw_clouds(self,context)

classes = (
    KUMOGEN_PT_main,
)