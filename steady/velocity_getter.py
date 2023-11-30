import paraview.simple as pv

case_path = "./steady.foam"

steadyfoam = pv.OpenFOAMReader(registrationName='steady.foam', FileName='/Users/felipeandrade/openfoam/wind_tunnel/steady/steady.foam')
steadyfoam.CaseType = 'Decomposed Case'
steadyfoam.MeshRegions = ['internalMesh']
steadyfoam.CellArrays = ['Q', 'U', 'epsilon', 'k', 'nut', 'omega', 'p', 'vorticity', 'yPlus']

slice1 = pv.Slice(registrationName='Slice2', Input=steadyfoam)
slice1.SliceType = 'Plane'
slice1.HyperTreeGridSlicer = 'Plane'
slice1.Triangulatetheslice = 0
slice1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Origin = [0.5, 0.0, 0.0]

# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice1.HyperTreeGridSlicer.Origin = [1.280000001192093, 0.0, 0.0]

extract_block = pv.ExtractBlock(slice1)
extract_block.Selectors = "U"

out_put = pv.SaveData('./steady.csv', proxy=extract_block)
out_put.FieldAssociation = 'Points'
out_put.FieldData = ['U']
out_put.UpdatePipeline()
