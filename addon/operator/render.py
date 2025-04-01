import bpy

class RenderOperator(bpy.types.Operator):
    bl_idname = "kumogen.render"
    bl_label = "render"

    def execute(self, context):
        bpy.context.scene.render.engine = 'CYCLES'
        bpy.context.scene.cycles.device = 'GPU'
        bpy.context.scene.cycles.shading_system = True
        bpy.context.scene.cycles.use_preview_adaptive_sampling = False
        bpy.context.scene.cycles.use_preview_adaptive_sampling = True
        bpy.context.scene.cycles.preview_samples = 32
        bpy.context.scene.cycles.use_preview_denoising = True
        bpy.context.scene.cycles.preview_denoising_start_sample = 32
        bpy.context.scene.cycles.use_adaptive_sampling = True
        bpy.context.scene.cycles.samples = 128
        bpy.context.scene.cycles.use_denoising = True
        bpy.context.scene.cycles.use_fast_gi = True
        bpy.context.scene.cycles.volume_preview_step_rate = 0.4
        bpy.context.scene.cycles.volume_step_rate = 0.4
        bpy.context.scene.cycles.volume_max_steps = 1024
        bpy.context.scene.render.compositor_device = 'GPU'
        bpy.context.space_data.clip_end = 1000000
        if context.scene.camera:
            context.scene.camera.data.clip_end = 1000000
        return {"FINISHED"}

