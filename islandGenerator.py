#Test commit


#works in blender 2.65

import bpy

bpy.data.window_managers["WinMan"].addon_search = "ant"

# new screen and deletion of default cube

bpy.ops.screen.new()
bpy.ops.object.delete(use_global=False)

# basic Island generator, low NoiseDepth means smoother surface, Falloff=2 means flatter beaches, Offset is set to allow some water inland

bpy.ops.mesh.landscape_add(AutoUpdate=True, SphereMesh=False, SmoothMesh=True, Subdivision=64, MeshSize=16, RandomSeed=0, NoiseSize=5, NoiseType='0', BasisType='0', VLBasisType='0', Distortion=1, HardNoise=True, NoiseDepth=3, mDimension=1.18, mLacunarity=2, mOffset=1, mGain=1, MarbleBias='0', MarbleSharp='0', MarbleShape='0', Invert=False, Height=4, Offset=-1, Falloff='2', Sealevel=-0.1, Plateaulevel=7, Strata=3, StrataType='0')


