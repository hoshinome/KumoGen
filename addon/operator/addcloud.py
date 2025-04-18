import bpy, os
from bpy.types import Operator
from ..utils import delete

def property_exists(prop_path, glob, loc):
    try:
        eval(prop_path, glob, loc)
        return True
    except:
        return False

class KUMOGEN_OT_add_clouds(Operator):
    bl_idname = "kumogen.addclouds"
    bl_label = ""
    bl_description = "Add Clouds"

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        blend_file = os.path.join(os.path.dirname(__file__), '..', 'assets', 'cloud.blend')
        if not os.path.exists(blend_file):
            self.report({'ERROR'}, f"File not found: {blend_file}")
            return {'CANCELLED'}

        if (property_exists("bpy.data.objects", globals(), locals()) and 
            ('KumoGen-Cube' in bpy.data.objects or 'KumoGen-Sphere' in bpy.data.objects)):
            pass
        else:
            delete.deleteclouds()

            selected_objects = context.selected_objects
            active_object = context.view_layer.objects.active

            # Create or get KumoGen-Clouds collection
            if "KumoGen" not in bpy.data.collections:
                cloud_collection = bpy.data.collections.new("KumoGen")
                context.scene.collection.children.link(cloud_collection)
            else:
                cloud_collection = bpy.data.collections["KumoGen"]

            # Append based on mesh type
            wm = bpy.context.window_manager.MeshTypes

            # Store original object count to identify new objects
            original_objects = set(bpy.data.objects)

            if wm.mesh_types == 'CUBE':
                bpy.ops.wm.append(
                    directory=os.path.join(blend_file, 'Object'),
                    filename='KumoGen-Cube'
                )
                bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Scale"].inputs[0].default_value = 1     
            elif wm.mesh_types == 'SPHERE':
                bpy.ops.wm.append(
                    directory=os.path.join(blend_file, 'Object'),
                    filename='KumoGen-Sphere'
                )
                bpy.data.materials["KumoGen-Clouds"].node_tree.nodes["KumoGen-Scale"].inputs[0].default_value = 0
            # Find newly added object(s)
            new_objects = set(bpy.data.objects) - original_objects
            if new_objects:
                appended_object = list(new_objects)[0]  # Get the first new object

                # Remove from other collections first
                for coll in appended_object.users_collection:
                    if coll.name != "KumoGen":
                        coll.objects.unlink(appended_object)

                # Link to KumoGen-Clouds if not already there
                if appended_object.name not in cloud_collection.objects:
                    cloud_collection.objects.link(appended_object)

            bpy.ops.object.select_all(action='DESELECT')
            for obj in selected_objects:
                obj.select_set(True)
            if active_object:
                context.view_layer.objects.active = active_object

        return {'FINISHED'}

classes = (
    KUMOGEN_OT_add_clouds,
)