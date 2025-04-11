
#####################################################################################################
#
# ooooo
# `888'
#  888   .ooooo.   .ooooo.  ooo. .oo.    .oooo.o
#  888  d88' `"Y8 d88' `88b `888P"Y88b  d88(  "8
#  888  888       888   888  888   888  `"Y88b.
#  888  888   .o8 888   888  888   888  o.  )88b
# o888o `Y8bod8P' `Y8bod8P' o888o o888o 8""888P'
#
#####################################################################################################

import glob
import os
from pathlib import Path

import bpy

from ..vendor.t3dn_bip import previews

previews.settings.WARNINGS = False

folder = Path(__file__).parent.parent / "icons"
collection: previews.ImagePreviewCollection = None
all_icons = {}
extension = "png"
icon_prefix = "K_"

def load_all_icons_from_folder(folder_path: str):
    global all_icons
    for path in Path(folder_path).glob(f"*.{extension}"):
        icon_name = f"{icon_prefix}{path.stem}" 
        all_icons[icon_name] = path.as_posix()

def get(name: str) -> int:
    name = name.removesuffix(f".{extension}") if name.endswith(f".{extension}") else name
    if collection is None:
        return None
    icon = all_icons.get(name)
    if icon is None:
        icon = all_icons.get('not_selected')
    return collection.load_safe(icon, icon, 'IMAGE').icon_id

def register():
    global collection
    collection = previews.new(max_size=(128, 128), lazy_load=False)
    load_all_icons_from_folder(folder.as_posix())

def unregister():
    previews.remove(collection)