--- 
layout: default
title: uaibot.simobjects.group
parent: uaibot.simobjects
grand_parent: Python API reference
--- 

# uaibot.simobjects.group module

<a id="module-uaibot.simobjects.group"></a>

### *class* uaibot.simobjects.group.Group(list_of_objects, name='', htm=array([[1., 0., 0., 0.], [0., 1., 0., 0.], [0., 0., 1., 0.], [0., 0., 0., 1.]]))

Bases: `object`

A group of other ‘simobject’ objects.

When the objects are grouped, it is assumed that the scenario frame is the parent frame of all objects.
This means that when the group is created, it stores the htm of each object at that moment, htm_base_object[i].
When the htm of the whole group is changed to ‘htm’, it changes the htm of each member i of the group to
htm @ htm_base_object[i]. Thus, be sure that, when the group is created, all the objects are in the correct pose.

To see which type of objects are groupable, see the constant ‘Utils.IS_GROUPABLE’.

## Parameters

htm
: The object’s configuration.
  (default: the same as the current HTM).

name
: The object’s name.
  (default: ‘genGroup’).

list_of_objects
: List of objects. Each must be an object of the type contained in the constant list ‘Utils.IS_GROUPABLE’.

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

Group pose. A 4x4 homogeneous transformation matrix written is scenario coordinates.

#### *property* htm_base_object

The pose of each object, written in scenario coordinates, when the group was created.

#### *property* list_of_objects

The list of objects contained in the group.

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
