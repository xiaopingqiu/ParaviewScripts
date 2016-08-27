try: paraview.simple
except: from paraview.simple import *
paraview.simple._DisableFirstRenderCameraReset()

pM_foam = OpenFOAMReader( FileName='E:\\OF_tutorials\\mapped\\pitzDailyMapped\\pM.foam' )

AnimationScene1 = GetAnimationScene()
AnimationScene1.EndTime = 0.1
AnimationScene1.PlayMode = 'Snap To TimeSteps'

pM_foam.CellArrays = ['U', 'UMean', 'UPrime2Mean', 'U_0', 'k', 'k_0', 'nuSgs', 'nuTilda', 'p', 'pMean', 'pPrime2Mean']
pM_foam.MeshRegions = ['internalMesh']

RenderView1 = GetRenderView()
RenderView1.CenterOfRotation = [0.10999999567866325, 0.0, 0.0]

RenderView1.Background = (81.0/255.0, 87.0/255.0, 110.0/255.0)
RenderView1.ViewSize = [1086,642]
RenderView1.CameraViewAngle = 30
RenderView1.CenterAxesVisibility=0

DataRepresentation1 = Show()
#DataRepresentation1.ConstantRadius = 0.28999999165534973
DataRepresentation1.EdgeColor = [0.0, 0.0, 0.5000076295109483]
#DataRepresentation1.PointSpriteDefaultsInitialized = 1
DataRepresentation1.SelectionPointFieldDataArrayName = 'p'
DataRepresentation1.SelectionCellFieldDataArrayName = 'p'
DataRepresentation1.ColorArrayName = ('POINT_DATA', 'p')
DataRepresentation1.ScalarOpacityUnitDistance = 0.015162935987203615
DataRepresentation1.Texture = []
DataRepresentation1.ExtractedBlockIndex = 1
#DataRepresentation1.RadiusRange = [-0.07000000029802322, 0.28999999165534973]
DataRepresentation1.ScaleFactor = 0.0359999991953373

a1_p_PVLookupTable = GetLookupTableForArray( "p", 1, RGBPoints=[0.0, 0.0, 0.0, 1.0, 1e-16, 1.0, 0.0, 0.0], VectorMode='Magnitude', NanColor=[0.498039, 0.498039, 0.498039], ColorSpace='HSV', ScalarRangeInitialized=1.0 )

a1_p_PiecewiseFunction = CreatePiecewiseFunction( Points=[0.0, 0.0, 0.5, 0.0, 1e-16, 1.0, 0.5, 0.0] )

DataRepresentation1.ScalarOpacityFunction = a1_p_PiecewiseFunction
DataRepresentation1.LookupTable = a1_p_PVLookupTable
#DataRepresentation1.RadiusRange = [-0.07, 0.29]

a1_p_PVLookupTable.ScalarOpacityFunction = a1_p_PiecewiseFunction

RenderView1.CameraPosition = [0.10999999567866325, 0.0, 0.7023592915690968]
RenderView1.CameraFocalPoint = [0.10999999567866325, 0.0, 0.0]
RenderView1.CameraClippingRange = [0.6943406986061459, 0.7141471810021238]
RenderView1.CameraParallelScale = 0.18178396116279658


######### generate a slice ################
Slice1 = Slice( SliceType="Plane" )

Slice1.SliceOffsetValues = [0.0]
Slice1.SliceType.Origin = [0.11, 0.0, 0.0]
Slice1.SliceType = "Plane"

# toggle the 3D widget visibility.
#active_objects.source.SMProxy.InvokeEvent('UserEvent', 'ShowWidget')
#RenderView1.CameraClippingRange = [0.4287074803602159, 1.0485246743217493]

# toggle the 3D widget visibility.
active_objects.source.SMProxy.InvokeEvent('UserEvent', 'HideWidget')
RenderView1.CameraClippingRange = [0.6943406986061459, 0.7141471810021238]

Slice1.SliceType.Normal = [0.0, 0.0, 1.0]

DataRepresentation2 = Show()
#DataRepresentation2.ConstantRadius = 0.28999999165534973
DataRepresentation2.EdgeColor = [0.0, 0.0, 0.5000076295109483]
#DataRepresentation2.PointSpriteDefaultsInitialized = 1
DataRepresentation2.SelectionPointFieldDataArrayName = 'p'
DataRepresentation2.SelectionCellFieldDataArrayName = 'p'
DataRepresentation2.ColorArrayName = ('POINT_DATA', 'p')
DataRepresentation2.Texture = []
DataRepresentation2.LookupTable = a1_p_PVLookupTable
#DataRepresentation2.RadiusRange = [-0.07000000029802322, 0.28999999165534973]
DataRepresentation2.ScaleFactor = 0.0359999991953373

DataRepresentation1.Visibility = 0

RenderView1.CameraClippingRange = [0.6953356986534058, 0.7128946809426333]

#DataRepresentation2.RadiusRange = [-0.07, 0.29]
DataRepresentation2.ColorArrayName = ('POINT_DATA', 'U')

a3_U_PVLookupTable = GetLookupTableForArray( "U", 3, RGBPoints=[0.0, 0.0, 0.0, 1.0, 16.0, 1.0, 0.0, 0.0], VectorMode='Magnitude', NanColor=[0.498039, 0.498039, 0.498039], ColorSpace='HSV', ScalarRangeInitialized=1.0, LockScalarRange=1 )

a3_U_PiecewiseFunction = CreatePiecewiseFunction( Points=[0.0, 0.0, 0.5, 0.0, 16.0, 1.0, 0.5, 0.0] )

AnimationScene1.AnimationTime = 0.1

ScalarBarWidgetRepresentation1 = CreateScalarBar( ComponentTitle='Magnitude', Title='U', Enabled=1, LabelFontSize=12, LookupTable=a3_U_PVLookupTable, TitleFontSize=12 )
GetRenderView().Representations.append(ScalarBarWidgetRepresentation1)


###### generate a glyph #################
Glyph1 = Glyph( GlyphType="Arrow", GlyphTransform="Transform2" )

DataRepresentation2.LookupTable = a3_U_PVLookupTable

a3_U_PVLookupTable.ScalarOpacityFunction = a3_U_PiecewiseFunction

Glyph1.Scalars = ['POINTS', 'p']
Glyph1.SetScaleFactor = 0.0359999991953373
Glyph1.Vectors = ['POINTS', 'U']
Glyph1.GlyphTransform = "Transform2"
Glyph1.GlyphType = "Arrow"

Glyph1.SetScaleFactor = 0.01
Glyph1.ScaleMode = 'off'
Glyph1.MaximumNumberofPoints = 1000

DataRepresentation3 = Show()
#DataRepresentation3.ConstantRadius = 0.2999996840953827
DataRepresentation3.EdgeColor = [0.0, 0.0, 0.5000076295109483]
#DataRepresentation3.PointSpriteDefaultsInitialized = 1
DataRepresentation3.SelectionPointFieldDataArrayName = 'p'
DataRepresentation3.SelectionCellFieldDataArrayName = 'p'
DataRepresentation3.ColorArrayName = ('POINT_DATA', 'U')
DataRepresentation3.Texture = []
#DataRepresentation3.RadiusRange = [-0.07000353187322617, 0.2999996840953827]
DataRepresentation3.ScaleFactor = 0.03700032159686089

#DataRepresentation3.ColorArrayName = ('POINT_DATA', '')

RenderView1.CameraClippingRange = [0.6936123081169067, 0.7150640745576737]

#DataRepresentation3.RadiusRange = [-0.0700035, 0.3]
DataRepresentation3.ColorArrayName = ('POINT_DATA', 'p')
DataRepresentation3.LookupTable = a1_p_PVLookupTable

DataRepresentation2.Texture = []
DataRepresentation2.Visibility = 0

ScalarBarWidgetRepresentation1.Enabled = 0
ScalarBarWidgetRepresentation1.Visibility = 0

a1_p_PVLookupTable.RGBPoints = [-96.12127685546875, 0.0, 0.0, 1.0, 61.768226623535156, 1.0, 0.0, 0.0]

a1_p_PiecewiseFunction.Points = [-96.12127685546875, 0.0, 0.5, 0.0, 61.768226623535156, 1.0, 0.5, 0.0]


###### generate a surface vector ###################
SetActiveSource(Slice1)
SurfaceVectors1 = SurfaceVectors()

SurfaceVectors1.SelectInputVectors = ['POINTS', 'U']

DataRepresentation4 = Show()
#DataRepresentation4.ConstantRadius = 0.28999999165534973
DataRepresentation4.EdgeColor = [0.0, 0.0, 0.5000076295109483]
#DataRepresentation4.PointSpriteDefaultsInitialized = 1
DataRepresentation4.SelectionPointFieldDataArrayName = 'p'
DataRepresentation4.SelectionCellFieldDataArrayName = 'p'
DataRepresentation4.ColorArrayName = ('POINT_DATA', 'U')
DataRepresentation4.Texture = []
DataRepresentation4.LookupTable = a3_U_PVLookupTable
#DataRepresentation4.RadiusRange = [-0.07000000029802322, 0.28999999165534973]
DataRepresentation4.ScaleFactor = 0.0359999991953373

#DataRepresentation4.RadiusRange = [-0.07, 0.29]

DataRepresentation3.Visibility = 0

RenderView1.CameraClippingRange = [0.6953356986534058, 0.7128946809426333]

DataRepresentation2.Texture = []

DataRepresentation2.Visibility = 0

#DataRepresentation4.Texture = []
#DataRepresentation4.Visibility = 0

RenderView1.CameraClippingRange = [0.002996152353161611, 2.9961523531616105]

DataRepresentation4.Visibility = 1

ScalarBarWidgetRepresentation1.Enabled = 1
ScalarBarWidgetRepresentation1.Visibility = 1

RenderView1.CameraPosition = [0.10999999567866325, 0.0, 0.702356634767752]
RenderView1.CameraClippingRange = [0.6953330684200745, 0.7128919842892683]
RenderView1.CameraParallelScale = 0.1817832735320095

#DataRepresentation2.Texture = []

DataRepresentation4.Texture = []


#####  generate a maskpoint ##########################
MaskPoints1 = MaskPoints()

MaskPoints1.GenerateVertices = 1
MaskPoints1.RandomSampling = 1
MaskPoints1.RandomSamplingMode = 'Spatially Stratified Random Sampling'
MaskPoints1.MaximumNumberofPoints = 1000

DataRepresentation5 = Show()
#DataRepresentation5.ConstantRadius = 0.28999999165534973
DataRepresentation5.EdgeColor = [0.0, 0.0, 0.5000076295109483]
#DataRepresentation5.PointSpriteDefaultsInitialized = 1
DataRepresentation5.SelectionPointFieldDataArrayName = 'p'
DataRepresentation5.SelectionCellFieldDataArrayName = 'p'
DataRepresentation5.ColorArrayName = ('POINT_DATA', 'U')
DataRepresentation5.Texture = []
DataRepresentation5.LookupTable = a3_U_PVLookupTable
#DataRepresentation5.RadiusRange = [-0.07000000029802322, 0.28999999165534973]
DataRepresentation5.ScaleFactor = 0.0359999991953373

DataRepresentation4.Visibility = 0

#DataRepresentation5.RadiusRange = [-0.07, 0.29]


####### generate stream line on a surface #########################
SetActiveSource(SurfaceVectors1)
StreamTracerWithCustomSource1 = StreamTracerWithCustomSource( SeedSource=MaskPoints1 )

StreamTracerWithCustomSource1.Vectors = ['POINTS', 'U']
StreamTracerWithCustomSource1.MaximumStreamlineLength = 0.35999999195337296

StreamTracerWithCustomSource1.MaximumError = 1e-06
StreamTracerWithCustomSource1.TerminalSpeed = 1e-12

DataRepresentation6 = Show()
#DataRepresentation6.ConstantRadius = 0.28999999165534973
DataRepresentation6.EdgeColor = [0.0, 0.0, 0.5000076295109483]
#DataRepresentation6.PointSpriteDefaultsInitialized = 1
DataRepresentation6.SelectionPointFieldDataArrayName = 'p'
DataRepresentation6.SelectionCellFieldDataArrayName = 'ReasonForTermination'
DataRepresentation6.ColorArrayName = ('POINT_DATA', 'U')
DataRepresentation6.Texture = []
DataRepresentation6.LookupTable = a3_U_PVLookupTable
#DataRepresentation6.RadiusRange = [-0.07000000029802322, 0.28999999165534973]
DataRepresentation6.ScaleFactor = 0.0359999991953373

DataRepresentation5.Visibility = 0

#DataRepresentation6.RadiusRange = [-0.07, 0.29]
DataRepresentation6.ColorArrayName = ('POINT_DATA', '')

ScalarBarWidgetRepresentation1.Enabled = 0
ScalarBarWidgetRepresentation1.Visibility = 0

#DataRepresentation5.Texture = []

MaskPoints1.MaximumNumberofPoints = 200

DataRepresentation6.Texture = []

DataRepresentation6.Opacity = 0.7
DataRepresentation6.DiffuseColor = [0.0, 0.0, 0.0]

DataRepresentation4.Texture = []

DataRepresentation4.Visibility = 1

#DataRepresentation6.Texture = []

#DataRepresentation5.Texture = []

#DataRepresentation4.Texture = []

RenderView1.CameraPosition = [0.10999999567866325, 0.0, 0.4797190320113051]
RenderView1.CameraClippingRange = [0.47492184169119206, 0.4869148174914747]

DataRepresentation2.Texture = []

DataRepresentation2.Visibility = 0

DataRepresentation4.Texture = []

WriteImage('E:/OF_tutorials/mapped/pitzDailyMapped/testscreen.png', Magnification=2)


DataRepresentation6.Visibility = 0

DataRepresentation4.Visibility = 0

RenderView1.CameraClippingRange = [0.0026043054963398975, 2.6043054963398973]

DataRepresentation3.Texture = []

DataRepresentation3.Visibility = 1

RenderView1.CameraPosition = [0.11499807611107826, 0.00038802623748779297, 0.725254404116244]
RenderView1.CameraFocalPoint = [0.11499807611107826, 0.00038802623748779297, 0.0]
RenderView1.CameraClippingRange = [0.7162784695385823, 0.7383026137930281]
RenderView1.CenterOfRotation = [0.11499807611107826, 0.00038802623748779297, 0.0]
RenderView1.CameraParallelScale = 0.18770965232976394

DataRepresentation2.Texture = []

DataRepresentation2.Visibility = 1

DataRepresentation3.Texture = []

DataRepresentation3.ColorArrayName = ('POINT_DATA', '')
DataRepresentation3.DiffuseColor = [0.0, 0.0, 0.0]

RenderView1.CameraPosition = [0.11499807611107826, 0.00038802623748779297, 0.599383805054747]
RenderView1.CameraClippingRange = [0.5916665764677003, 0.6105439557456087]

AnimationScene1.AnimationTime = 0.0
AnimationScene1.PlayMode = 'Sequence'
AnimationScene1.NumberOfFrames = 11

CameraAnimationCue1 = GetCameraTrack()
CameraAnimationCue1.AnimatedProxy = RenderView1
CameraAnimationCue1.Mode = 'Path-based'

TimeAnimationCue1 = GetTimeTrack()

KeyFrame5047 = CameraKeyFrame( FocalPathPoints=[0.114998, 0.000388026, 0.0], FocalPoint=[0.11499807611107826, 0.00038802623748779297, 0.0], PositionPathPoints=[0.0, 0.0, 0.5, 0.43120039439853625, 0.0, 0.40403042680054746, 0.6279812289875636, 0.0, 0.008529172380306538, 0.4444572181383874, 0.0, -0.39329526260513553, 0.016685579000083814, 0.0, -0.5035466293017314, -0.3382012405958345, 0.0, -0.24048906072285084, -0.35710462563060374, 0.0, 0.20085728982710624], ClosedPositionPath=1, ParallelScale=0.18770965232976394, Position=[0.11499807611107826, 0.00038802623748779297, 0.725254404116244] )

KeyFrame5048 = CameraKeyFrame( ParallelScale=0.18770965232976394, Position=[0.11499807611107826, 0.00038802623748779297, 0.725254404116244], KeyTime=1.0, FocalPoint=[0.11499807611107826, 0.00038802623748779297, 0.0] )

CameraAnimationCue1.KeyFrames = [ KeyFrame5047, KeyFrame5048 ]

RenderView1.CameraFocalPoint = [0.10459624231466369, 0.000388026, -0.002392362660596616]
RenderView1.CameraClippingRange = [0.5303500129360129, 0.7361458699228238]
RenderView1.CameraPosition = [-0.03455133768533633, -8.148545999999996e-05, 0.6026076373394033]

WriteAnimation('E:/OF_tutorials/mapped/pitzDailyMapped/ani/rotateTest.png', Magnification=2, Quality=2, FrameRate=15.000000)


Render()
