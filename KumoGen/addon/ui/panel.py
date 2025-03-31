import bpy
from bpy.types import Panel, UILayout
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
        #---Updater---
        if scn_sets.panel_tabs == "Updater":
            addon_updater_ops.check_for_update_background()

            row = layout.row(align=True)
            row.scale_y = 1.5
            col = layout.column()
            col.scale_y = 0.7
            row.operator(
                "wm.url_open", 
                text="Repository", 
                icon="URL"
            ).url = "https://github.com/hoshinome/KumoGen"
            col.label(text=f"Version: {bl_info['version']}")
            if addon_updater_ops.updater.update_ready:
                layout.label(text="Custom update message", icon="INFO")
            layout.label(text="")
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
                    box_object.alignment = "LEFT"
                    box_object.prop(wm, "altitude", icon="DOWNARROW_HLT" if wm.altitude else "RIGHTARROW", emboss=False)
                    if wm.altitude:
                        box_object.prop(bpy.data.objects['KumoGen-Clouds-Cube'], "location", index=2, text="Cloud Altitude")
                if "KumoGen-Sphere" in bpy.data.collections:
                    box_object.alignment = "LEFT"
                    box_object.prop(wm, "decimate", icon="DOWNARROW_HLT" if wm.decimate else "RIGHTARROW", emboss=False)
                    if wm.decimate:
                        box_Decimate = box_object.box()
                        box_Decimate.label(text="Decimate:", icon="MOD_DECIM")
                        box_Decimate.prop(bpy.data.objects["KumoGen-Clouds-Sphere"].modifiers["Decimate"], "ratio", text="Ratio",)
                    box_object.alignment = "LEFT"
                    box_object.prop(wm, "scale", icon="DOWNARROW_HLT" if wm.scale else "RIGHTARROW", emboss=False)
                    if wm.scale:
                        box_Scale = box_object.box()
                        box_Scale.label(text="Scale:", icon="EMPTY_ARROWS")
                        box_Scale.prop(bpy.data.objects["KumoGen-Clouds-Sphere"], "scale", text="Scale")
                #Shader Settings
                box = layout.box()
                box.label(text="Shader Settings:", icon="SHADING_RENDERED")
                box.alignment = "LEFT"
                box.prop(wm, "basic_controls", icon="DOWNARROW_HLT" if wm.basic_controls else "RIGHTARROW", emboss=False)
                if wm.basic_controls:
                    box_Basic_Controls = box.box()
                    box_Basic_Controls.label(text="Basic Controls:",icon="ANCHOR_CENTER")
                    box_Basic_Controls.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[3], "default_value", text="Color",)
                    box_Basic_Controls.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[86], "default_value", text="Animation",)
                    box_Basic_Controls.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[4], "default_value", text="Density",)
                    box_Basic_Controls.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[5], "default_value", text="Seed",)
                if "KumoGen-Sphere" in bpy.data.collections:
                    box.alignment = "LEFT"
                    box.prop(wm, "gradient", icon="DOWNARROW_HLT" if wm.gradient else "RIGHTARROW", emboss=False)
                    if wm.gradient:
                        box_Gradient = box.box()
                        box_Gradient.label(text="Gradient:", icon="GP_MULTIFRAME_EDITING")
                        box_Gradient.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[7], "default_value", text="Gradient",)
                        box_Gradient.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[8], "default_value", text="Scale",)
                        box_Gradient.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[9], "default_value", text="Detail",)
                box.alignment = "LEFT"
                box.prop(wm, "clouds", icon="DOWNARROW_HLT" if wm.clouds else "RIGHTARROW", emboss=False)
                if wm.clouds:
                    box_Clouds = box.box()
                    box_Clouds.label(text="Clouds", icon="OUTLINER_OB_VOLUME")
                    box_Clouds.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[0], "default_value", text="Cumulus",)
                    box_Clouds.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[1], "default_value", text="Cirrocumulus",)
                    box_Clouds.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[2], "default_value", text="Stratocumulus",)
                box.alignment = "LEFT"
                box.prop(wm, "layer", icon="DOWNARROW_HLT" if wm.layer else "RIGHTARROW", emboss=False)
                if wm.layer:
                    box_Layer = box.box()
                    box_Layer.label(text="Cloud Layers:", icon="MOD_INSTANCE")
                    if bool(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[0].default_value):
                        box_Cumulus = box_Layer.box()
                        box_Cumulus.label(text="Cumulus:")
                        box_Cumulus.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[11], "default_value", text="Layer 1",)
                        box_Cumulus.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[12], "default_value", text="Layer 2",)
                    if bool(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[1].default_value):
                        box_Cirrocumulus = box_Layer.box()
                        box_Cirrocumulus.label(text="Cirrocumulus:")
                        box_Cirrocumulus.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[32], "default_value", text="Layer 1",)
                        box_Cirrocumulus.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[33], "default_value", text="Layer 2",)
                    if bool(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[2].default_value):
                        box_Stratocumulus = box_Layer.box()
                        box_Stratocumulus.label(text="Stratocumulus:")
                        box_Stratocumulus.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[57], "default_value", text="Layer 1",)
                        box_Stratocumulus.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[58], "default_value", text="Layer 2",)
                box.alignment = "LEFT"
                box.prop(wm, "layer_controls", icon="DOWNARROW_HLT" if wm.layer_controls else "RIGHTARROW", emboss=False)
                if wm.layer_controls:
                    box_Layer_Controls = box.box()
                    box_Layer_Controls.label(text="Layer Controls:", icon="MOD_HUE_SATURATION")
                    if (bool(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[0].default_value) and bool(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[11].default_value) or bool(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[12].default_value)):
                        box_Layer_Controls.alignment = "LEFT"
                        box_Layer_Controls.prop(wm, "cumulus", icon="DOWNARROW_HLT" if wm.cumulus else "RIGHTARROW", emboss=False)
                        if wm.cumulus:
                            if bool(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[11].default_value):
                                box_Cumulus_Layer_1 = box_Layer_Controls.box()
                                box_Cumulus_Layer_1.label(text="Layer 1:")
                                box_Cumulus_Layer_1.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[14], "default_value", text="Coverage",)
                                box_Cumulus_Layer_1.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[15], "default_value", text="Scale",)
                                box_Cumulus_Layer_1.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[16], "default_value", text="Detail",)
                                box_Cumulus_Layer_1.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[17], "default_value", text="Roughness",)
                                box_Cumulus_Layer_1.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[18], "default_value", text="Distortion",)
                                box_Cumulus_Layer_1.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[19], "default_value", text="Location X",)
                                box_Cumulus_Layer_1.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[20], "default_value", text="Location Y",)
                                box_Cumulus_Layer_1.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[21], "default_value", text="Rotation",)
                            if bool(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[12].default_value):
                                box_Cumulus_Layer_2 = box_Layer_Controls.box()
                                box_Cumulus_Layer_2.label(text="Layer 2:")
                                box_Cumulus_Layer_2.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[23], "default_value", text="Coverage",)
                                box_Cumulus_Layer_2.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[24], "default_value", text="Scale",)
                                box_Cumulus_Layer_2.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[25], "default_value", text="Detail",)
                                box_Cumulus_Layer_2.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[26], "default_value", text="Roughness",)
                                box_Cumulus_Layer_2.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[27], "default_value", text="Distortion",)
                                box_Cumulus_Layer_2.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[28], "default_value", text="Location X",)
                                box_Cumulus_Layer_2.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[29], "default_value", text="Location Y",)
                                box_Cumulus_Layer_2.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[20], "default_value", text="Rotation",)
                    if (bool(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[1].default_value) and bool(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[32].default_value) or bool(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[33].default_value)):
                        box_Layer_Controls.alignment = "LEFT"
                        box_Layer_Controls.prop(wm, "cirrocumulus", icon="DOWNARROW_HLT" if wm.cirrocumulus else "RIGHTARROW", emboss=False)
                        if wm.cirrocumulus:
                            if bool(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[32].default_value):
                                box_Cirrocumulus_Layer_1 =box_Layer_Controls.box()
                                box_Cirrocumulus_Layer_1.label(text="Layer 1:")
                                box_Cirrocumulus_Layer_1.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[35], "default_value", text="Coverage",)
                                box_Cirrocumulus_Layer_1.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[36], "default_value", text="Scale",)
                                box_Cirrocumulus_Layer_1.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[37], "default_value", text="Distortion",)
                                box_Cirrocumulus_Layer_1.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[38], "default_value", text="Detail",)
                                box_Cirrocumulus_Layer_1.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[39], "default_value", text="Noise Scale",)
                                box_Cirrocumulus_Layer_1.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[40], "default_value", text="Noise Detail",)
                                box_Cirrocumulus_Layer_1.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[41], "default_value", text="Noise Roughness",)
                                box_Cirrocumulus_Layer_1.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[42], "default_value", text="Location X",)
                                box_Cirrocumulus_Layer_1.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[43], "default_value", text="Location Y",)
                                box_Cirrocumulus_Layer_1.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[44], "default_value", text="Rotation",)
                            if bool(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[33].default_value):
                                box_Cirrocumulus_Layer_2 =box_Layer_Controls.box()
                                box_Cirrocumulus_Layer_2.label(text="Layer 2:")
                                box_Cirrocumulus_Layer_2.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[46], "default_value", text="Coverage",)
                                box_Cirrocumulus_Layer_2.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[47], "default_value", text="Scale",)
                                box_Cirrocumulus_Layer_2.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[48], "default_value", text="Distortion",)
                                box_Cirrocumulus_Layer_2.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[49], "default_value", text="Detail",)
                                box_Cirrocumulus_Layer_2.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[50], "default_value", text="Noise Scale",)
                                box_Cirrocumulus_Layer_2.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[51], "default_value", text="Noise Detail",)
                                box_Cirrocumulus_Layer_2.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[52], "default_value", text="Noise Roughness",)
                                box_Cirrocumulus_Layer_2.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[53], "default_value", text="Location X",)
                                box_Cirrocumulus_Layer_2.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[54], "default_value", text="Location Y",)
                                box_Cirrocumulus_Layer_2.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[55], "default_value", text="Rotation",)
                    if (bool(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[2].default_value) and bool(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[57].default_value) or bool(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[58].default_value)):
                        box_Layer_Controls.alignment = "LEFT"
                        box_Layer_Controls.prop(wm, "stratocumulus", icon="DOWNARROW_HLT" if wm.stratocumulus else "RIGHTARROW", emboss=False)
                        if wm.stratocumulus:
                            if bool(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[57].default_value):
                                box_Stratocumulus_Layer_1 =box_Layer_Controls.box()
                                box_Stratocumulus_Layer_1.label(text="Layer 1:")
                                box_Stratocumulus_Layer_1.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[60], "default_value", text="Coverage",)
                                box_Stratocumulus_Layer_1.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[61], "default_value", text="Scale",)
                                box_Stratocumulus_Layer_1.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[62], "default_value", text="Detail",)
                                box_Stratocumulus_Layer_1.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[63], "default_value", text="Roughness",)
                                box_Stratocumulus_Layer_1.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[64], "default_value", text="Distortion",)
                                box_Stratocumulus_Layer_1.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[65], "default_value", text="Noise Scale",)
                                box_Stratocumulus_Layer_1.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[66], "default_value", text="Noise Detail",)
                                box_Stratocumulus_Layer_1.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[67], "default_value", text="Location X",)
                                box_Stratocumulus_Layer_1.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[68], "default_value", text="Location Y",)
                                box_Stratocumulus_Layer_1.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[69], "default_value", text="Rotation",)
                            if bool(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[58].default_value):
                                box_Stratocumulus_Layer_2 =box_Layer_Controls.box()
                                box_Stratocumulus_Layer_2.label(text="Layer 2:")
                                box_Stratocumulus_Layer_2.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[71], "default_value", text="Coverage",)
                                box_Stratocumulus_Layer_2.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[72], "default_value", text="Scale",)
                                box_Stratocumulus_Layer_2.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[73], "default_value", text="Detail",)
                                box_Stratocumulus_Layer_2.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[74], "default_value", text="Roughness",)
                                box_Stratocumulus_Layer_2.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[75], "default_value", text="Distortion",)
                                box_Stratocumulus_Layer_2.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[76], "default_value", text="Noise Scale",)
                                box_Stratocumulus_Layer_2.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[77], "default_value", text="Noise Detail",)
                                box_Stratocumulus_Layer_2.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[78], "default_value", text="Location X",)
                                box_Stratocumulus_Layer_2.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[79], "default_value", text="Location Y",)
                                box_Stratocumulus_Layer_2.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[80], "default_value", text="Rotation",)
                box.alignment = "LEFT"
                box.prop(wm, "mapping", icon="DOWNARROW_HLT" if wm.mapping else "RIGHTARROW", emboss=False)
                if wm.mapping:
                    box_Mapping = box.box()
                    box_Mapping.label(text="Mapping:", icon="EMPTY_AXIS")
                    box_Mapping.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[82], "default_value", text="Location",)
                    box_Mapping.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Clouds"].inputs[83], "default_value", text="Rotation",)
                    if "KumoGen-Cube" in bpy.data.collections:
                        box_Mapping.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Scale"].inputs[2], "default_value", text="Scale")
                    elif "KumoGen-Sphere" in bpy.data.collections:
                        box_Mapping.prop(bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Scale"].inputs[1], "default_value", text="Scale")