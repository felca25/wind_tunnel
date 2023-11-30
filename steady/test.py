# state file generated using paraview version 5.11.1
import paraview
paraview.compatibility.major = 5
paraview.compatibility.minor = 11

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [1874, 722]
renderView1.InteractionMode = '2D'
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [1.280000001192093, 0.0, 0.0]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [1.1366022834192753, 0.026776321658356184, 7.410256645705769]
renderView1.CameraFocalPoint = [1.1366022834192753, 0.026776321658356184, 0.0]
renderView1.CameraViewUp = [-0.0023213630720972933, 0.9999973056331141, 0.0]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 1.0755911162217027
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = materialLibrary1

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.AssignView(0, renderView1)
layout1.SetSize(1874, 722)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'OpenFOAMReader'
openFOAMReader3 = OpenFOAMReader(registrationName='OpenFOAMReader3', FileName='./steady.foam')

# create a new 'OpenFOAMReader'
openFOAMReader5 = OpenFOAMReader(registrationName='OpenFOAMReader5', FileName='./steady.foam')
openFOAMReader5.CaseType = 'Decomposed Case'

# create a new 'OpenFOAMReader'
openFOAMReader6 = OpenFOAMReader(registrationName='OpenFOAMReader6', FileName='./steady.foam')
openFOAMReader6.CaseType = 'Decomposed Case'

# create a new 'OpenFOAMReader'
openFOAMReader4 = OpenFOAMReader(registrationName='OpenFOAMReader4', FileName='./steady.foam')
openFOAMReader4.CaseType = 'Decomposed Case'

# create a new 'OpenFOAMReader'
openFOAMReader2 = OpenFOAMReader(registrationName='OpenFOAMReader2', FileName='./steady.foam')

# create a new 'OpenFOAMReader'
steadyfoam = OpenFOAMReader(registrationName='steady.foam', FileName='/Users/felipeandrade/openfoam/wind_tunnel/steady/steady.foam')
steadyfoam.CaseType = 'Decomposed Case'
steadyfoam.MeshRegions = ['internalMesh']
steadyfoam.CellArrays = ['Q', 'U', 'epsilon', 'k', 'nut', 'omega', 'p', 'vorticity', 'yPlus']

# create a new 'OpenFOAMReader'
steadyfoam_1 = OpenFOAMReader(registrationName='steady.foam', FileName='/Users/felipeandrade/openfoam/wind_tunnel/steady/steady.foam')
steadyfoam_1.CaseType = 'Decomposed Case'
steadyfoam_1.MeshRegions = ['patch/rotor']
steadyfoam_1.CellArrays = ['Q', 'U', 'epsilon', 'k', 'nut', 'omega', 'p', 'vorticity', 'yPlus']

# create a new 'Slice'
slice1 = Slice(registrationName='Slice1', Input=steadyfoam)
slice1.SliceType = 'Plane'
slice1.HyperTreeGridSlicer = 'Plane'
slice1.Triangulatetheslice = 0
slice1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Normal = [0.0, 0.0, 1.0]

# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice1.HyperTreeGridSlicer.Origin = [1.280000001192093, 0.0, 0.0]

# create a new 'Stream Tracer'
streamTracer1 = StreamTracer(registrationName='StreamTracer1', Input=slice1,
    SeedType='Line')
streamTracer1.Vectors = ['POINTS', 'U']
streamTracer1.MaximumStreamlineLength = 3.439999997615814

# init the 'Line' selected for 'SeedType'
streamTracer1.SeedType.Point1 = [-0.1, -0.6000000238418579, 0.0]
streamTracer1.SeedType.Point2 = [-0.1, 0.6000000238418579, 0.0]
streamTracer1.SeedType.Resolution = 100

# create a new 'Contour'
contour3 = Contour(registrationName='Contour3', Input=steadyfoam_1)
contour3.ContourBy = ['POINTS', 'p']
contour3.Isosurfaces = [-118.77073097229004, -282.5190124511719, -279.21096636068944, -275.90292027020695, -272.5948741797245, -269.286828089242, -265.9787819987596, -262.6707359082771, -259.36268981779466, -256.05464372731217, -252.74659763682973, -249.43855154634727, -246.1305054558648, -242.82245936538234, -239.51441327489988, -236.20636718441742, -232.89832109393495, -229.5902750034525, -226.28222891297003, -222.9741828224876, -219.6661367320051, -216.35809064152267, -213.05004455104017, -209.74199846055774, -206.43395237007527, -203.1259062795928, -199.81786018911035, -196.50981409862788, -193.20176800814542, -189.89372191766296, -186.58567582718052, -183.27762973669803, -179.9695836462156, -176.6615375557331, -173.35349146525067, -170.04544537476818, -166.73739928428574, -163.42935319380328, -160.12130710332082, -156.81326101283835, -153.5052149223559, -150.19716883187343, -146.88912274139096, -143.5810766509085, -140.27303056042604, -136.96498446994357, -133.65693837946114, -130.34889228897867, -127.04084619849621, -123.73280010801375, -120.42475401753128, -117.11670792704882, -113.80866183656636, -110.5006157460839, -107.19256965560143, -103.88452356511897, -100.5764774746365, -97.26843138415404, -93.96038529367158, -90.65233920318914, -87.34429311270668, -84.03624702222422, -80.72820093174175, -77.42015484125929, -74.11210875077683, -70.80406266029436, -67.4960165698119, -64.18797047932944, -60.87992438884697, -57.57187829836451, -54.26383220788205, -50.95578611739958, -47.64774002691715, -44.339693936434685, -41.03164784595222, -37.72360175546976, -34.415555664987295, -31.10750957450483, -27.799463484022368, -24.491417393539905, -21.18337130305747, -17.875325212574978, -14.567279122092543, -11.259233031610052, -7.951186941127617, -4.643140850645125, -1.33509476016269, 1.9729513303198019, 5.280997420802237, 8.589043511284729, 11.897089601767163, 15.205135692249598, 18.51318178273209, 21.821227873214525, 25.129273963697017, 28.43732005417945, 31.745366144661944, 35.05341223514438, 38.36145832562687, 41.669504416109305, 44.9775505065918]
contour3.PointMergeMethod = 'Uniform Binning'

# create a new 'Contour'
contour1 = Contour(registrationName='Contour1', Input=slice1)
contour1.ContourBy = ['POINTS', 'p']
contour1.Isosurfaces = [-36.8702392578125, -36.54934471935483, -36.22845018089716, -35.90755564243949, -35.586661103981825, -35.26576656552415, -34.94487202706649, -34.623977488608816, -34.30308295015114, -33.98218841169348, -33.661293873235806, -33.34039933477814, -33.01950479632047, -32.6986102578628, -32.37771571940513, -32.056821180947466, -31.735926642489794, -31.41503210403212, -31.094137565574457, -30.773243027116784, -30.452348488659116, -30.131453950201447, -29.810559411743778, -29.48966487328611, -29.168770334828437, -28.847875796370772, -28.5269812579131, -28.20608671945543, -27.885192180997763, -27.564297642540094, -27.243403104082425, -26.922508565624753, -26.601614027167088, -26.280719488709416, -25.959824950251747, -25.638930411794078, -25.31803587333641, -24.99714133487874, -24.67624679642107, -24.355352257963403, -24.03445771950573, -23.713563181048062, -23.392668642590394, -23.071774104132725, -22.750879565675056, -22.429985027217384, -22.10909048875972, -21.788195950302047, -21.467301411844378, -21.14640687338671, -20.82551233492904, -20.504617796471372, -20.183723258013703, -19.862828719556035, -19.541934181098362, -19.221039642640694, -18.900145104183025, -18.579250565725356, -18.258356027267688, -17.93746148881002, -17.61656695035235, -17.295672411894678, -16.97477787343701, -16.65388333497934, -16.332988796521672, -16.012094258064003, -15.691199719606335, -15.370305181148666, -15.049410642690994, -14.728516104233325, -14.407621565775656, -14.086727027317988, -13.765832488860319, -13.44493795040265, -13.124043411944982, -12.80314887348731, -12.48225433502964, -12.161359796571972, -11.840465258114303, -11.519570719656635, -11.198676181198966, -10.877781642741297, -10.556887104283625, -10.235992565825956, -9.915098027368288, -9.594203488910619, -9.27330895045295, -8.952414411995282, -8.631519873537613, -8.31062533507994, -7.989730796622272, -7.668836258164603, -7.3479417197069345, -7.027047181249266, -6.706152642791597, -6.3852581043339285, -6.064363565876256, -5.743469027418588, -5.422574488960919, -5.10167995050325, -4.7807854120455815, -4.459890873587909, -4.138996335130244, -3.818101796672572, -3.4972072582149067, -3.1763127197572345, -2.8554181812995694, -2.534523642841897, -2.213629104384225, -1.8927345659265598, -1.5718400274688875, -1.2509454890112224, -0.9300509505535501, -0.609156412095885, -0.28826187363821276, 0.03263266481945948, 0.3535272032771246, 0.6744217417347969, 0.995316280192462, 1.3162108186501342, 1.6371053571077994, 1.9579998955654716, 2.278894434023144, 2.599788972480809, 2.920683510938481, 3.2415780493961464, 3.5624725878538186, 3.8833671263114837, 4.204261664769156, 4.525156203226828, 4.846050741684493, 5.166945280142166, 5.487839818599831, 5.808734357057503, 6.129628895515168, 6.45052343397284, 6.771417972430513, 7.092312510888178, 7.41320704934585, 7.734101587803515, 8.054996126261187, 8.375890664718852, 8.696785203176525, 9.017679741634197, 9.338574280091862, 9.659468818549534, 9.9803633570072, 10.301257895464872, 10.622152433922537, 10.943046972380209, 11.263941510837881, 11.584836049295546, 11.905730587753219, 12.226625126210884, 12.547519664668556, 12.868414203126221, 13.189308741583893, 13.510203280041566, 13.83109781849923, 14.151992356956903, 14.472886895414568, 14.79378143387224, 15.114675972329906, 15.435570510787578, 15.75646504924525, 16.077359587702915, 16.398254126160587, 16.719148664618253, 17.040043203075925, 17.36093774153359, 17.681832279991262, 18.002726818448934, 18.3236213569066, 18.644515895364272, 18.965410433821937, 19.28630497227961, 19.607199510737274, 19.928094049194947, 20.24898858765262, 20.569883126110284, 20.890777664567956, 21.21167220302562, 21.532566741483294, 21.85346127994096, 22.17435581839863, 22.495250356856303, 22.81614489531397, 23.13703943377164, 23.457933972229306, 23.778828510686978, 24.099723049144643, 24.420617587602315, 24.741512126059988, 25.062406664517653, 25.383301202975325, 25.70419574143299, 26.025090279890662, 26.345984818348327, 26.666879356806, 26.987773895263665]
contour1.PointMergeMethod = 'Uniform Binning'

# create a new 'OpenFOAMReader'
openFOAMReader1 = OpenFOAMReader(registrationName='OpenFOAMReader1', FileName='./steady.foam')

# create a new 'Slice'
slice2 = Slice(registrationName='Slice2', Input=steadyfoam)
slice2.SliceType = 'Plane'
slice2.HyperTreeGridSlicer = 'Plane'
slice2.Triangulatetheslice = 0
slice2.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice2.SliceType.Origin = [0.5, 0.0, 0.0]

# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice2.HyperTreeGridSlicer.Origin = [1.280000001192093, 0.0, 0.0]

# create a new 'Contour'
contour2 = Contour(registrationName='Contour2', Input=slice2)
contour2.ContourBy = ['POINTS', 'p']
contour2.Isosurfaces = [2.398975133895874, -3.8656697273254395, -3.7391112452805646, -3.6125527632356893, -3.4859942811908144, -3.359435799145939, -3.2328773171010643, -3.1063188350561894, -2.979760353011314, -2.8532018709664393, -2.7266433889215644, -2.600084906876689, -2.4735264248318143, -2.3469679427869394, -2.220409460742064, -2.0938509786971893, -1.9672924966523142, -1.8407340146074391, -1.7141755325625643, -1.587617050517689, -1.4610585684728141, -1.3345000864279388, -1.207941604383064, -1.0813831223381891, -0.9548246402933138, -0.828266158248439, -0.7017076762035641, -0.5751491941586888, -0.44859071211381396, -0.3220322300689391, -0.1954737480240638, -0.06891526597918896, 0.05764321606568634, 0.1842016981105612, 0.3107601801554365, 0.4373186622003109, 0.5638771442451862, 0.6904356262900615, 0.8169941083349359, 0.9435525903798112, 1.0701110724246865, 1.1966695544695618, 1.3232280365144362, 1.4497865185593115, 1.5763450006041868, 1.7029034826490612, 1.8294619646939365, 1.9560204467388118, 2.0825789287836862, 2.2091374108285615, 2.335695892873437, 2.4622543749183112, 2.5888128569631865, 2.715371339008062, 2.8419298210529362, 2.9684883030978115, 3.095046785142687, 3.2216052671875612, 3.3481637492324365, 3.474722231277312, 3.601280713322187, 3.7278391953670615, 3.854397677411937, 3.980956159456812, 4.1075146415016865, 4.234073123546562, 4.360631605591436, 4.487190087636312, 4.613748569681187, 4.740307051726061, 4.8668655337709374, 4.993424015815812, 5.119982497860686, 5.2465409799055625, 5.373099461950437, 5.499657943995311, 5.6262164260401875, 5.752774908085062, 5.879333390129936, 6.0058918721748125, 6.132450354219687, 6.259008836264563, 6.3855673183094375, 6.512125800354312, 6.638684282399188, 6.7652427644440625, 6.891801246488937, 7.018359728533813, 7.1449182105786875, 7.271476692623562, 7.398035174668438, 7.5245936567133125, 7.651152138758187, 7.777710620803063, 7.9042691028479375, 8.030827584892812, 8.157386066937688, 8.283944548982562, 8.410503031027437, 8.537061513072313, 8.663619995117188]
contour2.PointMergeMethod = 'Uniform Binning'

# create a new 'Slice'
slice3 = Slice(registrationName='Slice3', Input=steadyfoam)
slice3.SliceType = 'Plane'
slice3.HyperTreeGridSlicer = 'Plane'
slice3.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice3.SliceType.Origin = [-0.3, 0.0, 0.0]

# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice3.HyperTreeGridSlicer.Origin = [1.280000001192093, 0.0, 0.0]

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from slice2
slice2Display = Show(slice2, renderView1, 'GeometryRepresentation')

# get 2D transfer function for 'U'
uTF2D = GetTransferFunction2D('U')

# get color transfer function/color map for 'U'
uLUT = GetColorTransferFunction('U')
uLUT.TransferFunction2D = uTF2D
uLUT.RGBPoints = [9.622541256248951e-06, 0.231373, 0.298039, 0.752941, 11.581112821508796, 0.865003, 0.865003, 0.865003, 23.162216020476336, 0.705882, 0.0156863, 0.14902]
uLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
slice2Display.Representation = 'Surface With Edges'
slice2Display.ColorArrayName = ['POINTS', 'U']
slice2Display.LookupTable = uLUT
slice2Display.SelectTCoordArray = 'None'
slice2Display.SelectNormalArray = 'None'
slice2Display.SelectTangentArray = 'None'
slice2Display.OSPRayScaleArray = 'p'
slice2Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice2Display.SelectOrientationVectors = 'U'
slice2Display.ScaleFactor = 0.12000000476837158
slice2Display.SelectScaleArray = 'p'
slice2Display.GlyphType = 'Arrow'
slice2Display.GlyphTableIndexArray = 'p'
slice2Display.GaussianRadius = 0.006000000238418579
slice2Display.SetScaleArray = ['POINTS', 'p']
slice2Display.ScaleTransferFunction = 'PiecewiseFunction'
slice2Display.OpacityArray = ['POINTS', 'p']
slice2Display.OpacityTransferFunction = 'PiecewiseFunction'
slice2Display.DataAxesGrid = 'GridAxesRepresentation'
slice2Display.PolarAxes = 'PolarAxesRepresentation'
slice2Display.SelectInputVectors = ['POINTS', 'U']
slice2Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
slice2Display.ScaleTransferFunction.Points = [-99.52783203125, 0.0, 0.5, 0.0, 22.63670539855957, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
slice2Display.OpacityTransferFunction.Points = [-99.52783203125, 0.0, 0.5, 0.0, 22.63670539855957, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for uLUT in view renderView1
uLUTColorBar = GetScalarBar(uLUT, renderView1)
uLUTColorBar.Title = 'U'
uLUTColorBar.ComponentTitle = 'Magnitude'

# set color bar visibility
uLUTColorBar.Visibility = 1

# show color legend
slice2Display.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'U'
uPWF = GetOpacityTransferFunction('U')
uPWF.Points = [9.622541256248951e-06, 0.0, 0.5, 0.0, 23.162216020476336, 1.0, 0.5, 0.0]
uPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# restore active source
SetActiveSource(openFOAMReader6)
# ----------------------------------------------------------------


if __name__ == '__main__':
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory='extracts')