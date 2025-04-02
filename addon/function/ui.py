import bpy

def kumogen_prop(layout, materials, nodes, inputs, text):
    layout.prop(bpy.data.materials[materials].node_tree.nodes[nodes].inputs[inputs], "default_value", text=text,)

def kumogen_tabs (layout, wm, name):
    layout.alignment = "LEFT"
    layout.prop(wm, name, icon="DOWNARROW_HLT" if getattr(wm, name) else "RIGHTARROW", emboss=False)