import bpy

def deleteclouds():
    #Object
    if 'KumoGen-Sphere' in bpy.data.objects:
        bpy.data.objects.remove(bpy.data.objects['KumoGen-Sphere'], do_unlink=True)
    elif 'KumoGen-Cube' in bpy.data.objects:
        bpy.data.objects.remove(bpy.data.objects['KumoGen-Cube'], do_unlink=True)
    #Collections
    if 'KumoGen-Clouds' in bpy.data.collections:
        bpy.data.collections.remove(bpy.data.collections['KumoGen-Clouds'], do_unlink=True)
    #Node Group
    if 'KumoGen-Clouds' in bpy.data.node_groups:
        bpy.data.node_groups.remove(bpy.data.node_groups['KumoGen-Clouds'], do_unlink=True)
    if 'KumoGen-Cumulus' in bpy.data.node_groups:
        bpy.data.node_groups.remove(bpy.data.node_groups['KumoGen-Cumulus'], do_unlink=True)
    if 'KumoGen-Cirrocumulus' in bpy.data.node_groups:
        bpy.data.node_groups.remove(bpy.data.node_groups['KumoGen-Cirrocumulus'], do_unlink=True)
    if 'KumoGen-Stratocumulus' in bpy.data.node_groups:
        bpy.data.node_groups.remove(bpy.data.node_groups['KumoGen-Stratocumulus'], do_unlink=True)
    if 'KumoGen-Scale' in bpy.data.node_groups:
        bpy.data.node_groups.remove(bpy.data.node_groups['KumoGen-Scale'], do_unlink=True)
    #Materials
    if 'KumoGen-Clouds' in bpy.data.materials:
        bpy.data.materials.remove(bpy.data.materials['KumoGen-Clouds'], do_unlink=True)