import bpy
from bpy.types import Panel
from ..function import ui
from ..settings.scene import KumoGen_Scene
from ... import addon_updater_ops, bl_info

class KumoGen_Panel(Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "KumoGen"
    bl_category = "KumoGen"
    bl_idname = "KUMOGEN_PT_panel"

    def draw(self, context):
        layout = self.layout
        self.context = context
        scn_sets: 'KumoGen_Scene' = context.scene.kumogen
        self.scn_sets = scn_sets
        scene = context.scene
        row = layout.row(align=True)
        row.scale_y = 1.5
        row.prop(scn_sets, "panel_tabs", expand=True)
        #---Update---
        if scn_sets.panel_tabs == "Update":
            addon_updater_ops.check_for_update_background()
            row = layout.row(align=True)
            row.scale_y = 1.5
            col = layout.column()
            col.scale_y = 0.7
            row.operator("wm.url_open", text="Website", icon="URL").url = "https://github.com/hoshinome/KumoGen"
            col.label(text=f"Version: {bl_info['version']}")
            if addon_updater_ops.updater.update_ready:
                layout.label(text="KumoGen Update", icon="INFO")
            addon_updater_ops.update_notice_box_ui(self, context)
        #---Render---
        if scn_sets.panel_tabs == "Render":
            layout = self.layout
            col = layout.column(align=True)
            cscene = scene.cycles
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
        #---Clouds---
        if scn_sets.panel_tabs == "Clouds":
            layout = self.layout
            wm = bpy.context.window_manager.KumoGen_Mesh_Types
            layout.prop(wm, "mesh_types", text="")
            box = layout.row(align=True)
            box = layout.split(align=True, factor=0.8)
            box.scale_x = 3.0
            box.scale_y = 2
            box.operator("kumogen.addcloud", text="Import Clouds", icon="OUTLINER_OB_VOLUME")
            box.operator("kumogen.deletecloud",text="",icon="TRASH")
            wm = bpy.context.window_manager.KumoGen_Tabs
            #Object Settings
            if "KumoGen-Clouds-Sphere" in bpy.data.objects or "KumoGen-Clouds-Cube" in bpy.data.objects:
                box_object = layout.box()
                box_object.label(text="Object Settings:", icon="OBJECT_DATA")
                if "KumoGen-Cube" in bpy.data.collections:
                    ui.kumogen_tabs(box_object, wm, "altitude")
                    if wm.altitude:
                        box_object.prop(bpy.data.objects["KumoGen-Clouds-Cube"], "location", index=2, text="Cloud Altitude")
                if "KumoGen-Sphere" in bpy.data.collections:
                    ui.kumogen_tabs(box_object, wm, "decimate")
                    if wm.decimate:
                        box_Decimate = box_object.box()
                        box_Decimate.label(text="Decimate:", icon="MOD_DECIM")
                        box_Decimate.prop(bpy.data.objects["KumoGen-Clouds-Sphere"].modifiers["Decimate"], "ratio", text="Ratio",)
                    ui.kumogen_tabs(box_object, wm, "scale")
                    if wm.scale:
                        box_Scale = box_object.box()
                        box_Scale.label(text="Scale:", icon="EMPTY_ARROWS")
                        box_Scale.prop(bpy.data.objects["KumoGen-Clouds-Sphere"], "scale", text="Scale")
                #Shader Settings
                box = layout.box()
                box.label(text="Shader Settings:", icon="SHADING_RENDERED")
                ui.kumogen_tabs(box, wm, "basic_controls")
                if wm.basic_controls:
                    box_Basic_Controls = box.box()
                    box_Basic_Controls.label(text="Basic Controls:",icon="ANCHOR_CENTER")
                    ui.kumogen_prop(box_Basic_Controls, "KumoGen-Clouds", "KumoGen-Clouds", 3, "Color")
                    ui.kumogen_prop(box_Basic_Controls, "KumoGen-Clouds", "KumoGen-Clouds", 86, "Animation")
                    ui.kumogen_prop(box_Basic_Controls, "KumoGen-Clouds", "KumoGen-Clouds", 4, "Density")
                    ui.kumogen_prop(box_Basic_Controls, "KumoGen-Clouds", "KumoGen-Clouds", 5, "Seed")
                if "KumoGen-Sphere" in bpy.data.collections:
                    ui.kumogen_tabs(box, wm, "gradient")
                    if wm.gradient:
                        box_Gradient = box.box()
                        box_Gradient.label(text="Gradient:", icon="GP_MULTIFRAME_EDITING")
                        ui.kumogen_prop(box_Gradient,"KumoGen-Clouds","KumoGen-Clouds",7,"Gradient")
                        ui.kumogen_prop(box_Gradient,"KumoGen-Clouds","KumoGen-Clouds",8,"Scale")
                        ui.kumogen_prop(box_Gradient,"KumoGen-Clouds","KumoGen-Clouds",9,"Detail")
                ui.kumogen_tabs(box, wm, "clouds")
                if wm.clouds:
                    box_Clouds = box.box()
                    box_Clouds.label(text="Clouds", icon="OUTLINER_OB_VOLUME")
                    ui.kumogen_prop(box_Clouds, "KumoGen-Clouds", "KumoGen-Clouds", 0, "Cumulus")
                    ui.kumogen_prop(box_Clouds, "KumoGen-Clouds", "KumoGen-Clouds", 1, "Cirrocumulus")
                    ui.kumogen_prop(box_Clouds, "KumoGen-Clouds", "KumoGen-Clouds", 2, "Stratocumulus")
                ui.kumogen_tabs(box, wm, "layer")
                if wm.layer:
                    box_Layer = box.box()
                    box_Layer.label(text="Cloud Layers:", icon="MOD_INSTANCE")
                    if bool(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[0].default_value):
                        box_Cumulus = box_Layer.box()
                        box_Cumulus.label(text="Cumulus:")
                        ui.kumogen_prop(box_Cumulus, "KumoGen-Clouds", "KumoGen-Clouds", 11, "Layer 1")
                        ui.kumogen_prop(box_Cumulus, "KumoGen-Clouds", "KumoGen-Clouds", 12, "Layer 2")
                    if bool(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[1].default_value):
                        box_Cirrocumulus = box_Layer.box()
                        box_Cirrocumulus.label(text="Cirrocumulus:")
                        ui.kumogen_prop(box_Cirrocumulus, "KumoGen-Clouds", "KumoGen-Clouds", 32, "Layer 1")
                        ui.kumogen_prop(box_Cirrocumulus, "KumoGen-Clouds", "KumoGen-Clouds", 33, "Layer 2")
                    if bool(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[2].default_value):
                        box_Stratocumulus = box_Layer.box()
                        box_Stratocumulus.label(text="Stratocumulus:")
                        ui.kumogen_prop(box_Stratocumulus, "KumoGen-Clouds", "KumoGen-Clouds", 57, "Layer 1")
                        ui.kumogen_prop(box_Stratocumulus, "KumoGen-Clouds", "KumoGen-Clouds", 58, "Layer 2")
                ui.kumogen_tabs(box, wm, "layer_controls")
                if wm.layer_controls:
                    box_Layer_Controls = box.box()
                    box_Layer_Controls.label(text="Layer Controls:", icon="MOD_HUE_SATURATION")
                    cumulus(box_Layer_Controls, wm)
                    cirrocumulus(box_Layer_Controls, wm)
                    stratocumulus(box_Layer_Controls, wm)
                ui.kumogen_tabs(box, wm, "mapping")
                if wm.mapping:
                    box_Mapping = box.box()
                    box_Mapping.label(text="Mapping:", icon="EMPTY_AXIS")
                    ui.kumogen_prop(box_Mapping, "KumoGen-Clouds", "KumoGen-Clouds", 82, "Location")
                    ui.kumogen_prop(box_Mapping, "KumoGen-Clouds", "KumoGen-Clouds", 83, "Rotation")
                    if "KumoGen-Cube" in bpy.data.collections:
                        ui.kumogen_prop(box_Mapping, "KumoGen-Clouds", "KumoGen-Scale", 2, "Scale")
                    elif "KumoGen-Sphere" in bpy.data.collections:
                        ui.kumogen_prop(box_Mapping, "KumoGen-Clouds", "KumoGen-Scale", 1, "Scale")
#---Clouds---
#---Cumulus---
def cumulus(box_Layer_Controls, wm):
    if (bool(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[0].default_value) and
    bool(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[11].default_value) or 
    bool(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[12].default_value)):
        ui.kumogen_tabs(box_Layer_Controls, wm, "cumulus")
        if wm.cumulus:
            # Layer 1
            if bool(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[11].default_value):
                box_Cumulus_Layer_1 = box_Layer_Controls.box()
                box_Cumulus_Layer_1.label(text="Layer 1:")
                ui.kumogen_prop(box_Cumulus_Layer_1, "KumoGen-Clouds", "KumoGen-Clouds", 14, "Coverage")
                ui.kumogen_prop(box_Cumulus_Layer_1, "KumoGen-Clouds", "KumoGen-Clouds", 15, "Scale")
                ui.kumogen_prop(box_Cumulus_Layer_1, "KumoGen-Clouds", "KumoGen-Clouds", 16, "Detail")
                ui.kumogen_prop(box_Cumulus_Layer_1, "KumoGen-Clouds", "KumoGen-Clouds", 17, "Roughness")
                ui.kumogen_prop(box_Cumulus_Layer_1, "KumoGen-Clouds", "KumoGen-Clouds", 18, "Distortion")
                ui.kumogen_prop(box_Cumulus_Layer_1, "KumoGen-Clouds", "KumoGen-Clouds", 19, "Location X")
                ui.kumogen_prop(box_Cumulus_Layer_1, "KumoGen-Clouds", "KumoGen-Clouds", 20, "Location Y")
                ui.kumogen_prop(box_Cumulus_Layer_1, "KumoGen-Clouds", "KumoGen-Clouds", 21, "Rotation")
            # Layer 2
            if bool(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[12].default_value):
                box_Cumulus_Layer_2 = box_Layer_Controls.box()
                box_Cumulus_Layer_2.label(text="Layer 2:")
                ui.kumogen_prop(box_Cumulus_Layer_2, "KumoGen-Clouds", "KumoGen-Clouds", 23, "Coverage")
                ui.kumogen_prop(box_Cumulus_Layer_2, "KumoGen-Clouds", "KumoGen-Clouds", 24, "Scale")
                ui.kumogen_prop(box_Cumulus_Layer_2, "KumoGen-Clouds", "KumoGen-Clouds", 25, "Detail")
                ui.kumogen_prop(box_Cumulus_Layer_2, "KumoGen-Clouds", "KumoGen-Clouds", 26, "Roughness")
                ui.kumogen_prop(box_Cumulus_Layer_2, "KumoGen-Clouds", "KumoGen-Clouds", 27, "Distortion")
                ui.kumogen_prop(box_Cumulus_Layer_2, "KumoGen-Clouds", "KumoGen-Clouds", 28, "Location X")
                ui.kumogen_prop(box_Cumulus_Layer_2, "KumoGen-Clouds", "KumoGen-Clouds", 29, "Location Y")
                ui.kumogen_prop(box_Cumulus_Layer_2, "KumoGen-Clouds", "KumoGen-Clouds", 20, "Rotation")
#---Ciccrocumulus---
def cirrocumulus(box_Layer_Controls, wm):
    if (bool(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[1].default_value) and
        bool(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[32].default_value) or
        bool(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[33].default_value)):
        ui.kumogen_tabs(box_Layer_Controls, wm, "cirrocumulus")
        if wm.cirrocumulus:
            #Layer 1
            if bool(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[32].default_value):
                box_Cirrocumulus_Layer_1 =box_Layer_Controls.box()
                box_Cirrocumulus_Layer_1.label(text="Layer 1:")
                ui.kumogen_prop(box_Cirrocumulus_Layer_1, "KumoGen-Clouds", "KumoGen-Clouds", 35, "Coverage")
                ui.kumogen_prop(box_Cirrocumulus_Layer_1, "KumoGen-Clouds", "KumoGen-Clouds", 36, "Scale")
                ui.kumogen_prop(box_Cirrocumulus_Layer_1, "KumoGen-Clouds", "KumoGen-Clouds", 37, "Distortion")
                ui.kumogen_prop(box_Cirrocumulus_Layer_1, "KumoGen-Clouds", "KumoGen-Clouds", 38, "Detail")
                ui.kumogen_prop(box_Cirrocumulus_Layer_1, "KumoGen-Clouds", "KumoGen-Clouds", 39, "Noise Scale")
                ui.kumogen_prop(box_Cirrocumulus_Layer_1, "KumoGen-Clouds", "KumoGen-Clouds", 40, "Noise Detail")
                ui.kumogen_prop(box_Cirrocumulus_Layer_1, "KumoGen-Clouds", "KumoGen-Clouds", 41, "Noise Roughness")
                ui.kumogen_prop(box_Cirrocumulus_Layer_1, "KumoGen-Clouds", "KumoGen-Clouds", 42, "Location X")
                ui.kumogen_prop(box_Cirrocumulus_Layer_1, "KumoGen-Clouds", "KumoGen-Clouds", 43, "Location Y")
                ui.kumogen_prop(box_Cirrocumulus_Layer_1, "KumoGen-Clouds", "KumoGen-Clouds", 44, "Rotation")
            #Layer 2
            if bool(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[33].default_value):
                box_Cirrocumulus_Layer_2 =box_Layer_Controls.box()
                box_Cirrocumulus_Layer_2.label(text="Layer 2:")
                ui.kumogen_prop(box_Cirrocumulus_Layer_2, "KumoGen-Clouds", "KumoGen-Clouds", 46, "Coverage")
                ui.kumogen_prop(box_Cirrocumulus_Layer_2, "KumoGen-Clouds", "KumoGen-Clouds", 47, "Scale")
                ui.kumogen_prop(box_Cirrocumulus_Layer_2, "KumoGen-Clouds", "KumoGen-Clouds", 48, "Distortion")
                ui.kumogen_prop(box_Cirrocumulus_Layer_2, "KumoGen-Clouds", "KumoGen-Clouds", 49, "Detail")
                ui.kumogen_prop(box_Cirrocumulus_Layer_2, "KumoGen-Clouds", "KumoGen-Clouds", 50, "Noise Scale")
                ui.kumogen_prop(box_Cirrocumulus_Layer_2, "KumoGen-Clouds", "KumoGen-Clouds", 51, "Noise Detail")
                ui.kumogen_prop(box_Cirrocumulus_Layer_2, "KumoGen-Clouds", "KumoGen-Clouds", 52, "Noise Roughness")
                ui.kumogen_prop(box_Cirrocumulus_Layer_2, "KumoGen-Clouds", "KumoGen-Clouds", 53, "Location X")
                ui.kumogen_prop(box_Cirrocumulus_Layer_2, "KumoGen-Clouds", "KumoGen-Clouds", 54, "Location Y")
                ui.kumogen_prop(box_Cirrocumulus_Layer_2, "KumoGen-Clouds", "KumoGen-Clouds", 55, "Rotation")
#---Stratocumulus---
def stratocumulus(box_Layer_Controls, wm):
    if (bool(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[2].default_value) and
        bool(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[57].default_value) or
        bool(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[58].default_value)):
        ui.kumogen_tabs(box_Layer_Controls, wm, "stratocumulus")
        if wm.stratocumulus:
            #Layer 1
            if bool(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[57].default_value):
                box_Stratocumulus_Layer_1 =box_Layer_Controls.box()
                box_Stratocumulus_Layer_1.label(text="Layer 1:")
                ui.kumogen_prop(box_Stratocumulus_Layer_1, "KumoGen-Clouds", "KumoGen-Clouds", 60, "Coverage")
                ui.kumogen_prop(box_Stratocumulus_Layer_1, "KumoGen-Clouds", "KumoGen-Clouds", 61, "Scale")
                ui.kumogen_prop(box_Stratocumulus_Layer_1, "KumoGen-Clouds", "KumoGen-Clouds", 62, "Detail")
                ui.kumogen_prop(box_Stratocumulus_Layer_1, "KumoGen-Clouds", "KumoGen-Clouds", 63, "Roughness")
                ui.kumogen_prop(box_Stratocumulus_Layer_1, "KumoGen-Clouds", "KumoGen-Clouds", 64, "Distortion")
                ui.kumogen_prop(box_Stratocumulus_Layer_1, "KumoGen-Clouds", "KumoGen-Clouds", 65, "Noise Scale")
                ui.kumogen_prop(box_Stratocumulus_Layer_1, "KumoGen-Clouds", "KumoGen-Clouds", 66, "Noise Detail")
                ui.kumogen_prop(box_Stratocumulus_Layer_1, "KumoGen-Clouds", "KumoGen-Clouds", 67, "Location X")
                ui.kumogen_prop(box_Stratocumulus_Layer_1, "KumoGen-Clouds", "KumoGen-Clouds", 68, "Location Y")
                ui.kumogen_prop(box_Stratocumulus_Layer_1, "KumoGen-Clouds", "KumoGen-Clouds", 69, "Rotation")
            #Layer 2
            if bool(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[58].default_value):
                box_Stratocumulus_Layer_2 =box_Layer_Controls.box()
                box_Stratocumulus_Layer_2.label(text="Layer 2:")
                ui.kumogen_prop(box_Stratocumulus_Layer_2, "KumoGen-Clouds", "KumoGen-Clouds", 71, "Coverage")
                ui.kumogen_prop(box_Stratocumulus_Layer_2, "KumoGen-Clouds", "KumoGen-Clouds", 72, "Scale")
                ui.kumogen_prop(box_Stratocumulus_Layer_2, "KumoGen-Clouds", "KumoGen-Clouds", 73, "Detail")
                ui.kumogen_prop(box_Stratocumulus_Layer_2, "KumoGen-Clouds", "KumoGen-Clouds", 74, "Roughness")
                ui.kumogen_prop(box_Stratocumulus_Layer_2, "KumoGen-Clouds", "KumoGen-Clouds", 75, "Distortion")
                ui.kumogen_prop(box_Stratocumulus_Layer_2, "KumoGen-Clouds", "KumoGen-Clouds", 76, "Noise Scale")
                ui.kumogen_prop(box_Stratocumulus_Layer_2, "KumoGen-Clouds", "KumoGen-Clouds", 77, "Noise Detail")
                ui.kumogen_prop(box_Stratocumulus_Layer_2, "KumoGen-Clouds", "KumoGen-Clouds", 78, "Location X")
                ui.kumogen_prop(box_Stratocumulus_Layer_2, "KumoGen-Clouds", "KumoGen-Clouds", 79, "Location Y")
                ui.kumogen_prop(box_Stratocumulus_Layer_2, "KumoGen-Clouds", "KumoGen-Clouds", 80, "Rotation")