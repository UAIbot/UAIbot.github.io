--- 
layout: default
title: uaibot.simobjects.pointlight
parent: uaibot.simobjects
grand_parent: Python API reference
--- 

# uaibot.simobjects.pointlight module

<a id="module-uaibot.simobjects.pointlight"></a>

### *class* uaibot.simobjects.pointlight.PointLight(htm=array([[1., 0., 0., 0.], [0., 1., 0., 0.], [0., 0., 1., 0.], [0., 0., 0., 1.]]), name='', color='white', intensity=1, max_distance=0)

Bases: `object`

> A point light.

> name
> : The object’s name.
>   (default: ‘genLight’).

> color
> : A HTML-compatible color.
>   (default: ‘white’).

> intensity
> : The light intensity.
>   (default: 1).
htm
: > The object’s configuration.
  > (default: the same as the current HTM).
  max_distance
  : The maximum distance in which the light can act, in meters.
    If set to 0, this distance is infinite.
    (default: 0).

#### add_ani_frame(time, htm=None, color=None, intensity=None, max_distance=None)

Add a single configuration to the object’s animation queue.

## Parameters

time: positive float
: The timestamp of the animation frame, in seconds.

htm
: The object’s configuration
  (default: the same as the current HTM).

color
: A HTML-compatible color.
  (default: the same as the current color).

intensity
: The light intensity.
  (default: the same as the current intensity).

max_distance
: The maximum distance in which the light can act, in meters.
  If set to 0, this distance is infinite.
  (default: the same as the current max_distance).

## Returns

None

#### *property* color

The light color.

#### gen_code()

Generate code for injection.

#### *property* htm

Object pose. A 4x4 homogeneous transformation matrix written is scenario coordinates.

#### *property* intensity

The light intensity

#### *property* max_distance

The light maximum distance (meters).

#### *property* name

The object name.

#### set_ani_frame(htm=None, color=None, intensity=None, max_distance=None)

Reset object’s animation queue and add a single configuration to the
object’s animation queue.

## Parameters

htm
: The object’s configuration
  (default: the same as the current HTM).

color
: A HTML-compatible color.
  (default: the same as the current color).

intensity
: The light intensity.
  (default: the same as the current intensity).

max_distance
: The maximum distance in which the light can act, in meters.
  If set to 0, this distance is infinite.
  (default: the same as the current max_distance).

## Returns

None
