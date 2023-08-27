--- 
layout: default
title: uaibot.simobjects.pointcloud
parent: uaibot.simobjects
grand_parent: Python API reference
--- 

# uaibot.simobjects.pointcloud module

<a id="module-uaibot.simobjects.pointcloud"></a>

### *class* uaibot.simobjects.pointcloud.PointCloud(name='', points=[], size=0.1, color='blue')

Bases: `object`

A cloud of points to draw in the simulator.

There is a fixed set of points (‘points’ attribute), and animation can be done by choosing, at each time,
an interval [initial_ind, final_ind] that determines the range of points that will be displayed.

## Parameters

name
: The object’s name.
  (default: ‘genPointCloud’).

size
: The size of each point in the point cloud.

color
: A HTML-compatible color.

points
: A matrix with 3 rows. The first row is the x coordinates, the second row the y coordinates, and the third row
  the z coordinates.

#### add_ani_frame(time, initial_ind, final_ind)

#### *property* color

Color of the object, a HTML-compatible string.

#### gen_code()

Generate code for injection.

#### *property* name

The object name.

#### *property* points

The points that compose the point cloud.

#### set_ani_frame(time, initial_ind, final_ind)

#### *property* size

The size of each point in the point cloud.
