import bpy
from . import addon_updater_ops
from ... import bl_info

def register():
	addon_updater_ops.register(bl_info)

def unregister():
	addon_updater_ops.unregister()