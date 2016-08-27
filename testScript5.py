#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'OpenFOAMReader'
pMfoam = OpenFOAMReader(FileName='E:\\OF_tutorials\\mapped\\pitzDailyMapped\\pM.foam')
pMfoam.MeshRegions = ['internalMesh']
pMfoam.CellArrays = ['U', 'UMean', 'UPrime2Mean', 'U_0', 'k', 'k_0', 'nuSgs', 'nuTilda', 'p', 'pMean', 'pPrime2Mean']

# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1097, 641]

# get color transfer function/color map for 'p'
pLUT = GetColorTransferFunction('p')

# show data in view
pMfoamDisplay = Show(pMfoam, renderView1)
# trace defaults for the display properties.
pMfoamDisplay.ColorArrayName = ['POINTS', 'p']
pMfoamDisplay.LookupTable = pLUT
pMfoamDisplay.OSPRayScaleArray = 'p'
pMfoamDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
pMfoamDisplay.GlyphType = 'Arrow'
pMfoamDisplay.ScalarOpacityUnitDistance = 0.015162935987203615
pMfoamDisplay.SetScaleArray = ['POINTS', 'p']
pMfoamDisplay.ScaleTransferFunction = 'PiecewiseFunction'
pMfoamDisplay.OpacityArray = ['POINTS', 'p']
pMfoamDisplay.OpacityTransferFunction = 'PiecewiseFunction'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
pMfoamDisplay.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 16.606517301670138, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
pMfoamDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 16.606517301670138, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
pMfoamDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 16.606517301670138, 1.0, 0.5, 0.0]

# reset view to fit data
renderView1.ResetCamera()

# show color bar/color legend
pMfoamDisplay.SetScalarBarVisibility(renderView1, True)

# get opacity transfer function/opacity map for 'p'
pPWF = GetOpacityTransferFunction('p')

animationScene1.GoToLast()

# create a new 'Slice'
slice1 = Slice(Input=pMfoam)
slice1.SliceType = 'Plane'
slice1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Origin = [0.10999999567866325, 0.0, 0.0]

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.109999995678663, 0.0, 0.0]
slice1.SliceType.Normal = [0.0, 0.0, 1.0]

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.109999995678663, 0.0, 0.0]
slice1.SliceType.Normal = [0.0, 0.0, 1.0]

# show data in view
slice1Display = Show(slice1, renderView1)
# trace defaults for the display properties.
slice1Display.ColorArrayName = ['POINTS', 'p']
slice1Display.LookupTable = pLUT
slice1Display.OSPRayScaleArray = 'p'
slice1Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice1Display.GlyphType = 'Arrow'
slice1Display.SetScaleArray = ['POINTS', 'p']
slice1Display.ScaleTransferFunction = 'PiecewiseFunction'
slice1Display.OpacityArray = ['POINTS', 'p']
slice1Display.OpacityTransferFunction = 'PiecewiseFunction'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
slice1Display.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 16.606517301670138, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
slice1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 16.606517301670138, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
slice1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 16.606517301670138, 1.0, 0.5, 0.0]

# hide data in view
Hide(pMfoam, renderView1)

# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=slice1.SliceType)

# set scalar coloring
ColorBy(slice1Display, ('POINTS', 'U'))

# rescale color and/or opacity maps used to include current data range
slice1Display.RescaleTransferFunctionToDataRange(True)

# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'U'
uLUT = GetColorTransferFunction('U')

# get opacity transfer function/opacity map for 'U'
uPWF = GetOpacityTransferFunction('U')

# Rescale transfer function
uLUT.RescaleTransferFunction(0.0, 16.0)

# Rescale transfer function
uPWF.RescaleTransferFunction(0.0, 16.0)

# create a new 'Glyph'
glyph1 = Glyph(Input=slice1,
    GlyphType='Arrow')
glyph1.Scalars = ['POINTS', 'p']
glyph1.Vectors = ['POINTS', 'U']
glyph1.ScaleFactor = 0.0359999991953373
glyph1.GlyphTransform = 'Transform2'

# show data in view
glyph1Display = Show(glyph1, renderView1)
# trace defaults for the display properties.
glyph1Display.ColorArrayName = ['POINTS', 'p']
glyph1Display.LookupTable = pLUT
glyph1Display.OSPRayScaleArray = 'p'
glyph1Display.OSPRayScaleFunction = 'PiecewiseFunction'
glyph1Display.GlyphType = 'Arrow'
glyph1Display.SetScaleArray = ['POINTS', 'p']
glyph1Display.ScaleTransferFunction = 'PiecewiseFunction'
glyph1Display.OpacityArray = ['POINTS', 'p']
glyph1Display.OpacityTransferFunction = 'PiecewiseFunction'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
glyph1Display.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 16.606517301670138, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
glyph1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 16.606517301670138, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
glyph1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 16.606517301670138, 1.0, 0.5, 0.0]

# show color bar/color legend
glyph1Display.SetScalarBarVisibility(renderView1, True)

# Properties modified on glyph1
glyph1.ScaleFactor = 0.01
glyph1.MaximumNumberOfSamplePoints = 1000

# turn off scalar coloring
ColorBy(glyph1Display, None)

# change solid color
glyph1Display.DiffuseColor = [0.0, 0.0, 0.0]

# hide data in view
Hide(glyph1, renderView1)

# set active source
SetActiveSource(slice1)

# create a new 'Surface Vectors'
surfaceVectors1 = SurfaceVectors(Input=slice1)
surfaceVectors1.SelectInputVectors = ['POINTS', 'U']

# show data in view
surfaceVectors1Display = Show(surfaceVectors1, renderView1)
# trace defaults for the display properties.
surfaceVectors1Display.ColorArrayName = ['POINTS', 'p']
surfaceVectors1Display.LookupTable = pLUT
surfaceVectors1Display.OSPRayScaleArray = 'p'
surfaceVectors1Display.OSPRayScaleFunction = 'PiecewiseFunction'
surfaceVectors1Display.GlyphType = 'Arrow'
surfaceVectors1Display.SetScaleArray = ['POINTS', 'p']
surfaceVectors1Display.ScaleTransferFunction = 'PiecewiseFunction'
surfaceVectors1Display.OpacityArray = ['POINTS', 'p']
surfaceVectors1Display.OpacityTransferFunction = 'PiecewiseFunction'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
surfaceVectors1Display.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 16.606517301670138, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
surfaceVectors1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 16.606517301670138, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
surfaceVectors1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 16.606517301670138, 1.0, 0.5, 0.0]

# hide data in view
Hide(slice1, renderView1)

# show color bar/color legend
surfaceVectors1Display.SetScalarBarVisibility(renderView1, True)

# set scalar coloring
ColorBy(surfaceVectors1Display, ('POINTS', 'U'))

# rescale color and/or opacity maps used to include current data range
surfaceVectors1Display.RescaleTransferFunctionToDataRange(True)

# show color bar/color legend
surfaceVectors1Display.SetScalarBarVisibility(renderView1, True)

# Rescale transfer function
uLUT.RescaleTransferFunction(0.0, 16.0)

# Rescale transfer function
uPWF.RescaleTransferFunction(0.0, 16.0)

# create a new 'Mask Points'
maskPoints1 = MaskPoints(Input=surfaceVectors1)

# Properties modified on maskPoints1
maskPoints1.MaximumNumberofPoints = 200

# show data in view
maskPoints1Display = Show(maskPoints1, renderView1)
# trace defaults for the display properties.
maskPoints1Display.ColorArrayName = ['POINTS', 'p']
maskPoints1Display.LookupTable = pLUT
maskPoints1Display.OSPRayScaleArray = 'p'
maskPoints1Display.OSPRayScaleFunction = 'PiecewiseFunction'
maskPoints1Display.GlyphType = 'Arrow'
maskPoints1Display.SetScaleArray = ['POINTS', 'p']
maskPoints1Display.ScaleTransferFunction = 'PiecewiseFunction'
maskPoints1Display.OpacityArray = ['POINTS', 'p']
maskPoints1Display.OpacityTransferFunction = 'PiecewiseFunction'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
maskPoints1Display.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 16.606517301670138, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
maskPoints1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 16.606517301670138, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
maskPoints1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 16.606517301670138, 1.0, 0.5, 0.0]

# hide data in view
Hide(surfaceVectors1, renderView1)

# show color bar/color legend
maskPoints1Display.SetScalarBarVisibility(renderView1, True)

# Properties modified on maskPoints1
maskPoints1.RandomSampling = 1
maskPoints1.RandomSamplingMode = 'Spatially Stratified Random Sampling'
maskPoints1.GenerateVertices = 1

# create a new 'Stream Tracer With Custom Source'
streamTracerWithCustomSource1 = StreamTracerWithCustomSource(Input=surfaceVectors1,
    SeedSource=maskPoints1)
streamTracerWithCustomSource1.Vectors = ['POINTS', 'U']
streamTracerWithCustomSource1.MaximumStreamlineLength = 0.35999999195337296

# show data in view
streamTracerWithCustomSource1Display = Show(streamTracerWithCustomSource1, renderView1)
# trace defaults for the display properties.
streamTracerWithCustomSource1Display.ColorArrayName = ['POINTS', 'p']
streamTracerWithCustomSource1Display.LookupTable = pLUT
streamTracerWithCustomSource1Display.OSPRayScaleArray = 'p'
streamTracerWithCustomSource1Display.OSPRayScaleFunction = 'PiecewiseFunction'
streamTracerWithCustomSource1Display.GlyphType = 'Arrow'
streamTracerWithCustomSource1Display.SetScaleArray = ['POINTS', 'p']
streamTracerWithCustomSource1Display.ScaleTransferFunction = 'PiecewiseFunction'
streamTracerWithCustomSource1Display.OpacityArray = ['POINTS', 'p']
streamTracerWithCustomSource1Display.OpacityTransferFunction = 'PiecewiseFunction'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
streamTracerWithCustomSource1Display.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 16.606517301670138, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
streamTracerWithCustomSource1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 16.606517301670138, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
streamTracerWithCustomSource1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 16.606517301670138, 1.0, 0.5, 0.0]

# hide data in view
Hide(surfaceVectors1, renderView1)

# hide data in view
Hide(maskPoints1, renderView1)

# show color bar/color legend
streamTracerWithCustomSource1Display.SetScalarBarVisibility(renderView1, True)

# turn off scalar coloring
ColorBy(streamTracerWithCustomSource1Display, None)

# change solid color
streamTracerWithCustomSource1Display.DiffuseColor = [0.0, 0.0, 0.0]

# reset view to fit data
renderView1.ResetCamera()

# set active source
SetActiveSource(slice1)

# show data in view
slice1Display = Show(slice1, renderView1)

# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# Properties modified on slice1Display
slice1Display.Opacity = 0.9

# Properties modified on slice1Display
slice1Display.Opacity = 0.8

# Properties modified on slice1Display
slice1Display.Opacity = 0.81

# Properties modified on slice1Display
slice1Display.Opacity = 1.0

# set active source
SetActiveSource(streamTracerWithCustomSource1)

# Properties modified on streamTracerWithCustomSource1Display
streamTracerWithCustomSource1Display.Opacity = 0.9

# Properties modified on streamTracerWithCustomSource1Display
streamTracerWithCustomSource1Display.Opacity = 0.8

# Properties modified on streamTracerWithCustomSource1Display
streamTracerWithCustomSource1Display.Opacity = 0.7

# Properties modified on streamTracerWithCustomSource1Display
streamTracerWithCustomSource1Display.Opacity = 0.6

# current camera placement for renderView1
renderView1.CameraPosition = [0.10997183993458748, -1.6307458281517029e-06, 0.7022380229427176]
renderView1.CameraFocalPoint = [0.10997183993458748, -1.6307458281517029e-06, 0.0]
renderView1.CameraParallelScale = 0.18175257453271623

# save screenshot
SaveScreenshot('E:/OF_tutorials/mapped/pitzDailyMapped/testscreen5.png', magnification=1, quality=100, view=renderView1)

# hide data in view
Hide(streamTracerWithCustomSource1, renderView1)

# set active source
SetActiveSource(glyph1)

# show data in view
glyph1Display = Show(glyph1, renderView1)

# Properties modified on animationScene1
animationScene1.PlayMode = 'Sequence'

# Properties modified on animationScene1
animationScene1.NumberOfFrames = 11

# get camera animation track for the view
cameraAnimationCue1 = GetCameraTrack(view=renderView1)

# create keyframes for this animation track

# create a key frame
keyFrame6294 = CameraKeyFrame()
keyFrame6294.Position = [0.10997183993458748, -1.6307458281517029e-06, 0.7022380229427176]
keyFrame6294.FocalPoint = [0.10997183993458748, -1.6307458281517029e-06, 0.0]
keyFrame6294.ParallelScale = 0.18175257453271623
keyFrame6294.PositionPathPoints = [0.0, 0.0, 0.5, 0.4313853635234024, 0.0, 0.4044182226353145, 0.6285839769212815, 0.0, 0.009017268033072706, 0.4454008303939574, 0.0, -0.3930687213457655, 0.01764043818344739, 0.0, -0.5037495908866263, -0.3375730898923284, 0.0, -0.24097105771016905, -0.3568989304714977, 0.0, 0.20045359034691326]
keyFrame6294.FocalPathPoints = [0.115497, 0.000493787, 0.0]
keyFrame6294.ClosedPositionPath = 1

# create a key frame
keyFrame6295 = CameraKeyFrame()
keyFrame6295.KeyTime = 1.0
keyFrame6295.Position = [0.10997183993458748, -1.6307458281517029e-06, 0.7022380229427176]
keyFrame6295.FocalPoint = [0.10997183993458748, -1.6307458281517029e-06, 0.0]
keyFrame6295.ParallelScale = 0.18175257453271623

# initialize the animation track
cameraAnimationCue1.Mode = 'Path-based'
cameraAnimationCue1.KeyFrames = [keyFrame6294, keyFrame6295]

# current camera placement for renderView1
renderView1.CameraPosition = [0.10997183993458748, -1.6307458281517029e-06, 0.7022380229427176]
renderView1.CameraFocalPoint = [0.10997183993458748, -1.6307458281517029e-06, 0.0]
renderView1.CameraParallelScale = 0.18175257453271623

# current camera placement for renderView1
renderView1.CameraPosition = [0.10997183993458748, -1.6307458281517029e-06, 0.7022380229427176]
renderView1.CameraFocalPoint = [0.10997183993458748, -1.6307458281517029e-06, 0.0]
renderView1.CameraParallelScale = 0.18175257453271623

# save animation images/movie
WriteAnimation('E:/OF_tutorials/mapped/pitzDailyMapped/ani/rotateTest5.png', Magnification=1, FrameRate=15.0, Compression=True)