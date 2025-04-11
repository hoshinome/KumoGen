import bpy
from bpy.types import Operator
from ..utils import delete

class KUMOGEN_OT_delete_clouds(Operator):
    bl_idname = "kumogen.deleteclouds"
    bl_label = ""
    bl_label = "Delete Clouds"

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        delete.deleteclouds()
        return {"FINISHED"}
    
classes = (
    KUMOGEN_OT_delete_clouds,
)