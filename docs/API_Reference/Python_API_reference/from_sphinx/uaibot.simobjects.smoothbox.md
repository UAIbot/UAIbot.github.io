--- 
layout: default
title: uaibot.simobjects.smoothbox
parent: uaibot.simobjects
grand_parent: Python API reference
--- 

# uaibot.simobjects.smoothbox module

<a id="module-uaibot.simobjects.smoothbox"></a>

### *class* uaibot.simobjects.smoothbox.SmoothBox(htm=array([[1., 0., 0., 0.], [0., 1., 0., 0.], [0., 0., 1., 0.], [0., 0., 0., 1.]]), name='', width=1, height=1, depth=1, mass=1, color='red', opacity=1, mesh_material=None)

Bases: `object`

A smooth box object. Smooth boxes satisfy the parametric equation (in their own aligned axis)

(x/width)^4+(y/depth)^4+(z/height)^4 = 1

## Parameters

htm
: The object’s configuration
  (default: the same as the current HTM).

name
: The object’s name.
  (default: ‘genBox’).

width
: The object’s width, in meters.
  (default: 1).

depth
: The object’s depth, in meters.
  (default: 1).

height
: The object’s height, in meters.
  (default: 1).

mass
: The object’s mass, in kg.
  (default: 1).

color
: The object’s color, a HTML - compatible string.
  (default: “red”).

opacity
: The opacity. 1 = fully opaque, and 0 = transparent.

mesh_material: ‘MeshMaterial’ object
: The object mesh material. If set to ‘None’, the default is used.
  (default: None).

#### aabb()

Compute the width, depth and height of an axis aligned bounding box (aabb) that
covers the object. It also considers the current orientation.

### Returns

> width
> : The width of the box, in meters.

> depth
> : The depth of the box, in meters.

> height
> : The depth of the box, in meters.

#### add_ani_frame(time, htm=None)

Add a single configuration to the object’s animation queue.

### Parameters

time: positive float
: The timestamp of the animation frame, in seconds.

htm
: The object’s configuration
  (default: the same as the current HTM).

### Returns

None

#### *property* color

Color of the object

#### copy()

Return a deep copy of the object, without copying the animation frames.

#### *property* depth

The box depth, in meters.

#### gen_code()

Generate code for injection.

#### *property* height

The box height, in meters.

#### *property* htm

Object pose. A 4x4 homogeneous transformation matrix written is scenario coordinates.

#### inertia_matrix(htm=None)

The 3D inertia matrix of the object, written in the world frame.
Assume that the transformation between the word frame and the object frame is ‘htm’.

### Parameters

htm
: The object’s configuration for which the inertia matrix will be computed
  (default: the same as the current HTM).

### Returns

> inertia_matrix
> : The 3D inertia matrix.

#### *property* mass

Mass of the object, in kg.

#### *property* mesh_material

Mesh properties of the object

#### *property* name

The object name.

#### projection(point, htm=None)

The projection of a point in the object, that is, the
closest point in the object to a point ‘point’.

### Parameters

point
: The point for which the projection will be computed.

htm
: The object’s configuration
  (default: the same as the current HTM).

### Returns

> proj_point
> : The projection of the point ‘point’ in the object.

> d
> : The distance between the object and ‘point’.

#### set_ani_frame(htm=None)

Reset object’s animation queue and add a single configuration to the
object’s animation queue.

### Parameters

htm
: The object’s configuration
  (default: the same as the current HTM).

### Returns

None

#### *property* volume

The volume of the object, in m³.

#### *property* width

The box width, in meters.