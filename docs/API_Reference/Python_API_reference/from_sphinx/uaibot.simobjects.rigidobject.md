--- 
layout: default
title: uaibot.simobjects.rigidobject
parent: uaibot.simobjects
grand_parent: Python API reference
--- 

# uaibot.simobjects.rigidobject module

<a id="module-uaibot.simobjects.rigidobject"></a>

### *class* uaibot.simobjects.rigidobject.RigidObject(list_model_3d, name='', htm=array([[1., 0., 0., 0.], [0., 1., 0., 0.], [0., 0., 1., 0.], [0., 0., 0., 1.]]))

Bases: `object`

A rigid object.

## Parameters

name
: The object’s name.
  (default: ‘genRigidObject’).

list_model_3d
: The 3d model that compose the object.

htm
: The object’s configuration.
  (default: the same as the current HTM).

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

#### gen_code()

Generate code for injection.

#### *property* htm

Object pose. A 4x4 homogeneous transformation matrix written is scenario coordinates.

#### *property* list_model_3d

The list of 3d models of the object.

#### *property* name

Name of the object.

#### set_ani_frame(htm=None)

Reset object’s animation queue and add a single configuration to the
object’s animation queue.

### Parameters

htm
: The object’s configuration
  (default: the same as the current HTM).

### Returns

None
