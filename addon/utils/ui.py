import bpy
from bpy.types import UILayout

def tabs(layout: UILayout, wm, name,text):
    row = layout.row(align=True)
    row.alignment = "LEFT"
    row.prop(wm, name,
        icon="DOWNARROW_HLT" if getattr(wm, name) else "RIGHTARROW",
        emboss=False,
        text=text
    )