import bpy

def deleate_cloud():
    if 'KumoGen-Cube' in bpy.data.collections or 'KumoGen-Sphere' in bpy.data.collections:
        #Object
        if 'KumoGen-Clouds-Sphere' in bpy.data.objects:
            bpy.data.objects.remove(bpy.data.objects['KumoGen-Clouds-Sphere'], do_unlink=True)
        elif 'KumoGen-Clouds-Cube' in bpy.data.objects:
            bpy.data.objects.remove(bpy.data.objects['KumoGen-Clouds-Cube'], do_unlink=True)
        #Collections
        if 'KumoGen-Cube' in bpy.data.collections:
            bpy.data.collections.remove(bpy.data.collections['KumoGen-Cube'], do_unlink=True)
        elif 'KumoGen-Sphere' in bpy.data.collections:
            bpy.data.collections.remove(bpy.data.collections['KumoGen-Sphere'], do_unlink=True)
    #Node Groups
    if 'KumoGen-Clouds' in bpy.data.node_groups:
        bpy.data.node_groups.remove(bpy.data.node_groups['KumoGen-Clouds'], do_unlink=True)
        bpy.data.node_groups.remove(bpy.data.node_groups['KumoGen-Cumulus'], do_unlink=True)
        bpy.data.node_groups.remove(bpy.data.node_groups['KumoGen-Cirrocumulus'], do_unlink=True)
        bpy.data.node_groups.remove(bpy.data.node_groups['KumoGen-Stratocumulus'], do_unlink=True)
        bpy.data.node_groups.remove(bpy.data.node_groups['KumoGen-Scale'], do_unlink=True)
    #Materials
    if 'KumoGen-Clouds' in bpy.data.materials:
        bpy.data.materials.remove(bpy.data.materials['KumoGen-Clouds'], do_unlink=True)