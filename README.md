This repository contains several pieces of pvpython scripts. [pvpython](http://www.paraview.org/Wiki/ParaView/Python_Scripting) is a Paraview python clientused to access all kinds of features in Paraview through python scripts.

The two scripts have the same function, but `testScript4.py`is valid for Paraview-4.1.0, and `testScript5.py` for Paraview-5.1.0.

Functions are listed below:

1. Read a 'xxx.foam' with Paraview's OpenFOAMReader 
2. Make a slice, and then use 'Glyph' fliter on the slice 
3. Call 'Surface Vectors' filter on the slice to make a Surface Vector source named as 'SurfaceVector' 
4. Call 'Mask Points' filter on the 'SurfaceVector' to make a Mask Points source named as 'MaskPoint' 
5. Call the 'Stream Tracer With Custom Source' filter, with the 'SurfaceVector' as Input, and 'MaskPoint' as seed point. This will generate stream line on the slice made at step 2 
6. Make the stream line visible, and save a screenshot of the view. 
7. Make the slice and glyph visible, and save a 11 frame animation. The camera of the view circles around the y axis.  
