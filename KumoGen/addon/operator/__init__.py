import bpy
from . import addcloud, deleatecloud, render

classes = (
    addcloud.CloudAddOperator,
    deleatecloud.DeleteCloudOperator,
    render.RenderOperator,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)