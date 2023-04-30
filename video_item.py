# trace generated using paraview version 5.11.0
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 11

#### import the simple module from the paraview
import os
import re
import sys
from paraview.simple import *
import time

dir_in = sys.argv[1]
dir_out = sys.argv[2]
fn = sys.argv[3]
angle = float(sys.argv[4])

#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'Legacy VTK Reader'
step_full_046500vtk = LegacyVTKReader(registrationName=fn, FileNames=[dir_in + fn])

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

renderView1.OrientationAxesVisibility = 0

# show data in view
step_full_046500vtkDisplay = Show(step_full_046500vtk, renderView1, 'UnstructuredGridRepresentation')

text = Text()
text.Text = re.match(r'.*_(\d+)\..*', fn).group(1)
textDisplay = Show(text, renderView1)
# textDisplay.Position = [0,0]

# trace defaults for the display properties.
step_full_046500vtkDisplay.Representation = 'Surface'
step_full_046500vtkDisplay.ColorArrayName = [None, '']
step_full_046500vtkDisplay.SelectTCoordArray = 'None'
step_full_046500vtkDisplay.SelectNormalArray = 'None'
step_full_046500vtkDisplay.SelectTangentArray = 'None'
step_full_046500vtkDisplay.OSPRayScaleArray = 'activity'
step_full_046500vtkDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
step_full_046500vtkDisplay.SelectOrientationVectors = 'None'
step_full_046500vtkDisplay.ScaleFactor = 18.6560299104
step_full_046500vtkDisplay.SelectScaleArray = 'None'
step_full_046500vtkDisplay.GlyphType = 'Arrow'
step_full_046500vtkDisplay.GlyphTableIndexArray = 'None'
step_full_046500vtkDisplay.GaussianRadius = 0.93280149552
step_full_046500vtkDisplay.SetScaleArray = ['POINTS', 'activity']
step_full_046500vtkDisplay.ScaleTransferFunction = 'PiecewiseFunction'
step_full_046500vtkDisplay.OpacityArray = ['POINTS', 'activity']
step_full_046500vtkDisplay.OpacityTransferFunction = 'PiecewiseFunction'
step_full_046500vtkDisplay.DataAxesGrid = 'GridAxesRepresentation'
step_full_046500vtkDisplay.PolarAxes = 'PolarAxesRepresentation'
step_full_046500vtkDisplay.ScalarOpacityUnitDistance = 282.77611863233534
step_full_046500vtkDisplay.OpacityArrayName = ['POINTS', 'activity']
step_full_046500vtkDisplay.SelectInputVectors = [None, '']
step_full_046500vtkDisplay.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
step_full_046500vtkDisplay.ScaleTransferFunction.Points = [-72.2939, 0.0, 0.5, 0.0, 26.9816, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
step_full_046500vtkDisplay.OpacityTransferFunction.Points = [-72.2939, 0.0, 0.5, 0.0, 26.9816, 1.0, 0.5, 0.0]

# reset view to fit data
renderView1.ResetCamera(False)

# get the material library
materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(step_full_046500vtkDisplay, ('POINTS', 'connected_dendrites'))

# rescale color and/or opacity maps used to include current data range
step_full_046500vtkDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
step_full_046500vtkDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'connected_dendrites'
connected_dendritesLUT = GetColorTransferFunction('connected_dendrites')

# get opacity transfer function/opacity map for 'connected_dendrites'
connected_dendritesPWF = GetOpacityTransferFunction('connected_dendrites')

# get 2D transfer function for 'connected_dendrites'
connected_dendritesTF2D = GetTransferFunction2D('connected_dendrites')

# change representation type
step_full_046500vtkDisplay.SetRepresentationType('Point Gaussian')

# hide data in view
Hide(step_full_046500vtk, renderView1)

# create a new 'Glyph'
glyph1 = Glyph(registrationName='Glyph1', Input=step_full_046500vtk,
    GlyphType='Arrow')
glyph1.OrientationArray = ['POINTS', 'No orientation array']
glyph1.ScaleArray = ['POINTS', 'No scale array']
glyph1.ScaleFactor = 18.6560299104
glyph1.GlyphTransform = 'Transform2'

# set active source
SetActiveSource(glyph1)

# show data in view
glyph1Display = Show(glyph1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
glyph1Display.Representation = 'Surface'
glyph1Display.ColorArrayName = ['POINTS', 'connected_dendrites']
glyph1Display.LookupTable = connected_dendritesLUT
glyph1Display.SelectTCoordArray = 'None'
glyph1Display.SelectNormalArray = 'None'
glyph1Display.SelectTangentArray = 'None'
glyph1Display.OSPRayScaleArray = 'activity'
glyph1Display.OSPRayScaleFunction = 'PiecewiseFunction'
glyph1Display.SelectOrientationVectors = 'None'
glyph1Display.ScaleFactor = 20.40607510209084
glyph1Display.SelectScaleArray = 'None'
glyph1Display.GlyphType = 'Arrow'
glyph1Display.GlyphTableIndexArray = 'None'
glyph1Display.GaussianRadius = 1.0203037551045417
glyph1Display.SetScaleArray = ['POINTS', 'activity']
glyph1Display.ScaleTransferFunction = 'PiecewiseFunction'
glyph1Display.OpacityArray = ['POINTS', 'activity']
glyph1Display.OpacityTransferFunction = 'PiecewiseFunction'
glyph1Display.DataAxesGrid = 'GridAxesRepresentation'
glyph1Display.PolarAxes = 'PolarAxesRepresentation'
glyph1Display.SelectInputVectors = [None, '']
glyph1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
glyph1Display.ScaleTransferFunction.Points = [-72.006, 0.0, 0.5, 0.0, 26.9816, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
glyph1Display.OpacityTransferFunction.Points = [-72.006, 0.0, 0.5, 0.0, 26.9816, 1.0, 0.5, 0.0]

# show color bar/color legend
glyph1Display.SetScalarBarVisibility(renderView1, True)

# reset view to fit data
renderView1.ResetCamera(False)

# Properties modified on glyph1
glyph1.GlyphType = 'Sphere'

# show data in view
glyph1Display = Show(glyph1, renderView1, 'GeometryRepresentation')

# reset view to fit data
renderView1.ResetCamera(False)

# show color bar/color legend
glyph1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# change representation type
glyph1Display.SetRepresentationType('Point Gaussian')

# Rescale transfer function
connected_dendritesLUT.RescaleTransferFunction(0.0, 15.0)

# Rescale transfer function
connected_dendritesPWF.RescaleTransferFunction(0.0, 15.0)

# Rescale 2D transfer function
connected_dendritesTF2D.RescaleTransferFunction(0.0, 15.0, 0.0, 15.0)

# create a new 'Clip'
clip1 = Clip(registrationName='Clip1', Input=glyph1)
clip1.ClipType = 'Plane'
clip1.HyperTreeGridClipper = 'Plane'
clip1.Scalars = ['POINTS', 'activity']
clip1.Value = -22.5122

# init the 'Plane' selected for 'ClipType'
clip1.ClipType.Origin = [93.21967506408691, 73.76142978668213, 77.15091228485107]

# init the 'Plane' selected for 'HyperTreeGridClipper'
clip1.HyperTreeGridClipper.Origin = [93.21967506408691, 73.76142978668213, 77.15091228485107]

# Properties modified on clip1.ClipType
clip1.ClipType.Origin = [93.21369557844596, 74.00192589884854, 77.13879152971688]
clip1.ClipType.Normal = [0.059885186432594426, 0.9965755328504619, -0.05701729360248291]

# show data in view
clip1Display = Show(clip1, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
clip1Display.Representation = 'Surface'
clip1Display.ColorArrayName = ['POINTS', 'connected_dendrites']
clip1Display.LookupTable = connected_dendritesLUT
clip1Display.SelectTCoordArray = 'None'
clip1Display.SelectNormalArray = 'Normals'
clip1Display.SelectTangentArray = 'None'
clip1Display.OSPRayScaleArray = 'Normals'
clip1Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip1Display.SelectOrientationVectors = 'None'
clip1Display.ScaleFactor = 22.074069023132324
clip1Display.SelectScaleArray = 'None'
clip1Display.GlyphType = 'Arrow'
clip1Display.GlyphTableIndexArray = 'None'
clip1Display.GaussianRadius = 1.1037034511566162
clip1Display.SetScaleArray = ['POINTS', 'Normals']
clip1Display.ScaleTransferFunction = 'PiecewiseFunction'
clip1Display.OpacityArray = ['POINTS', 'Normals']
clip1Display.OpacityTransferFunction = 'PiecewiseFunction'
clip1Display.DataAxesGrid = 'GridAxesRepresentation'
clip1Display.PolarAxes = 'PolarAxesRepresentation'
clip1Display.ScalarOpacityFunction = connected_dendritesPWF
clip1Display.ScalarOpacityUnitDistance = 7.748923730368715
clip1Display.OpacityArrayName = ['POINTS', 'Normals']
clip1Display.SelectInputVectors = ['POINTS', 'Normals']
clip1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
clip1Display.ScaleTransferFunction.Points = [-0.9749279022216797, 0.0, 0.5, 0.0, 0.9749279022216797, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
clip1Display.OpacityTransferFunction.Points = [-0.9749279022216797, 0.0, 0.5, 0.0, 0.9749279022216797, 1.0, 0.5, 0.0]

# show color bar/color legend
clip1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# hide data in view
Hide(clip1, renderView1)

# set active source
SetActiveSource(clip1)

# show data in view
clip1Display = Show(clip1, renderView1, 'UnstructuredGridRepresentation')

# show color bar/color legend
clip1Display.SetScalarBarVisibility(renderView1, True)

# change representation type
clip1Display.SetRepresentationType('Point Gaussian')

# hide data in view
Hide(glyph1, renderView1)

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

# get layout
layout1 = GetLayout()

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1810, 1544)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [-318.5979225828467, -408.94669018063547, 278.3799133766025]
renderView1.CameraFocalPoint = [93.45354652404774, 73.76142978668206, 77.15091228485102]
renderView1.CameraViewUp = [0.20528001779217242, 0.2221186909017186, 0.9531649392667316]
renderView1.CameraParallelScale = 172.3211396844726
renderView1.GetActiveCamera().Azimuth(-angle)

Render()
print(fn.replace('.vtk', '.png'))
WriteImage(dir_out + fn.replace('.vtk', '.png'))

Delete(layout1)
Delete(clip1Display)
Delete(clip1)
Delete(glyph1Display)
Delete(glyph1)
Delete(connected_dendritesTF2D)
Delete(connected_dendritesPWF)
Delete(connected_dendritesLUT)
Delete(materialLibrary1)
Delete(step_full_046500vtkDisplay)
Delete(renderView1)
# Delete(transformFilter)
Delete(text)
Delete(step_full_046500vtk)

time.sleep(10)