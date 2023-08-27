--- 
layout: default
title: uaibot.simobjects.vector
parent: uaibot.simobjects
grand_parent: Python API reference
--- 

# uaibot.simobjects.vector module

<a id="module-uaibot.simobjects.vector"></a>

### *class* uaibot.simobjects.vector.Vector(name='', color='black', thickness=1, origin=[0, 0, 0], vector=[0.5, 0.5, 0.5])

Bases: `object`

A vector object (arrow).

## Parameters

name
: The object’s name.
  (default: ‘genVector’).

color
: The object’s color, a HTML - compatible string.
  (default: “red”).

#### add_ani_frame(time, origin=None, vector=None)

#### *property* color

Color of the object

#### gen_code()

Generate code for injection.

#### *property* name

Name of the object.

#### *property* origin

The origin point of the vector, in scenario coordinates and in meters.

#### set_ani_frame(start_point=None, end_point=None)

#### *property* thickness

The thickness of the vetor.

#### *property* vector

The vector, in scenario coordinates and in meters.
