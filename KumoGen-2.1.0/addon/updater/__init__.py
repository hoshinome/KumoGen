import bpy
from . import addon_updater_ops
from ... import VERSION

def register():
	addon_updater_ops.register({"version": VERSION})

def unregister():
	addon_updater_ops.unregister()