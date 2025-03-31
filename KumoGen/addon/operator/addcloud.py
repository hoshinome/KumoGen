import bpy, os
from bpy.types import Operator
from ..function import deleate_cloud

def property_exists(prop_path, glob, loc):
    try:
        eval(prop_path, glob, loc)
        return True
    except:
        return False

class CloudAddOperator(Operator):
    bl_idname = "kumogen.addcloud"
    bl_label = "Cloud"

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        blend_file= os.path.join(os.path.dirname(__file__), '..', 'assets', 'Cloud.blend')
        if (property_exists("bpy.data.collections", globals(), locals()) and ('KumoGen-Cube' in bpy.data.collections or 'KumoGen-Sphere' in bpy.data.collections)):
            pass
        else:
            if not os.path.exists(blend_file):
                self.report({'ERROR'}, f"File not found: {blend_file}")
                return {'CANCELLED'}
            deleate_cloud.deleate_cloud()#雲を削除
            before_data = context.view_layer.active_layer_collection
            context.view_layer.active_layer_collection = context.view_layer.layer_collection
            wm = bpy.context.window_manager.KumoGen_Mesh_Types
            if wm.mesh_types == 'CUBE':#立方体
                bpy.ops.wm.append(directory=os.path.join(blend_file, 'Collection'),filename='KumoGen-Cube')
                bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Scale"].inputs[0].default_value = 1
            elif wm.mesh_types == 'SPHERE':#球体
                bpy.ops.wm.append(directory=os.path.join(blend_file, 'Collection'),filename='KumoGen-Sphere')
                bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Scale"].inputs[0].default_value = 0
            context.view_layer.active_layer_collection = before_data
            bpy.ops.object.select_all(action='DESELECT')
        
        return {"FINISHED"}