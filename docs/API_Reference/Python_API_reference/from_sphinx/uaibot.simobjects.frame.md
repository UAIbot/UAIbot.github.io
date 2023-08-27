--- 
layout: default
title: uaibot.simobjects.frame
parent: uaibot.simobjects
grand_parent: Python API reference
--- 

# uaibot.simobjects.frame module

<a id="module-uaibot.simobjects.frame"></a>

### *class* uaibot.simobjects.frame.Frame(htm=array([[1., 0., 0., 0.], [0., 1., 0., 0.], [0., 0., 1., 0.], [0., 0., 0., 1.]]), name='', size=0.3, axis_color=['red', 'lime', 'blue'], axis_names=['x', 'y', 'z'])

Bases: `object`

A frame object.

## Parameters

htm
: The object’s configuration.
  (default: the same as the current HTM).

name
: The object’s name.
  (default: ‘genFrame’).

size
: The axis sizes, in meters.
  (default: 0.3).

axis_color
: A list of 3 HTML-compatible strings, one for each axis.
  (default: [‘red’, ‘lime’, ‘blue’]).

axis_names
: The axis names.
  (default: [‘x’, ‘y’, ‘z’]).

#### add_ani_frame(time, htm=None)

Add a single configuration to the object’s animation queue.

### Parameters

time: positive float
: The timestamp of the animation frame, in seconds.

htm
: The object’s configuration.
  (default: the same as the current HTM).

### Returns

None

#### *property* axis_color

The axis colors. It is a list of 3 HTML-compatible colors.

#### *property* axis_name

The axis names. It is a list of 3 strings.

#### gen_code()

Generate code for injection.

#### *property* htm

Object pose. A 4x4 homogeneous transformation matrix written is scenario coordinates.

#### *property* name

Name of the object.

#### set_ani_frame(htm=None)

Reset object’s animation queue and add a single configuration to the
object’s animation queue.

### Parameters

htm
: The object’s configuration.
  (default: the same as the current HTM).

### Returns

None

#### *property* size

The axis size, in meters.
