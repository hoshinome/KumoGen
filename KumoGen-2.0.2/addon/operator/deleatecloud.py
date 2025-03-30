import bpy
from bpy.types import Operator
from ..function import deleate_cloud

class DeleteCloudOperator(Operator):
    bl_idname = "kumogen.deletecloud"
    bl_label = "Delete Cloud"

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        deleate_cloud.deleate_cloud()
        return {"FINISHED"}