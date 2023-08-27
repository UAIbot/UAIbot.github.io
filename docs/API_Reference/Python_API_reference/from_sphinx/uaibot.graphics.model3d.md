--- 
layout: default
title: uaibot.graphics.model3d
parent: uaibot.graphics
grand_parent: Python API reference
--- 

# uaibot.graphics.model3d module

<a id="module-uaibot.graphics.model3d"></a>

### *class* uaibot.graphics.model3d.Model3D(url='', scale=1, htm=array([[1., 0., 0., 0.], [0., 1., 0., 0.], [0., 0., 1., 0.], [0., 0., 0., 1.]]), mesh_material=None)

Bases: `object`

A class that represents a 3d model of an object.

## Parameters

url
: The url that contains the 3d object.
  It must have one of the following formats: ‘obj’, ‘stl’, ‘dae’.

scale
: The scaling parameter of the object.
  (default: 1).

htm
: The htm of the 3d models. This is used to tune the ‘default’ htm for the object in the uaibot simulator.
  This is necessary because the 3d model can have a different ‘default’ pose than the desired one.
  (default: np.identity(4)).

mesh_material
: The mesh_material to be applied into the 3d model.
  (default: None).

#### gen_code(name)

Generate code for injection.

#### *property* htm

Object pose. A 4x4 homogeneous transformation matrix written is scenario coordinates.

#### *property* mesh_material

The model mesh material.

#### *property* scale

The object scale.

#### *property* url

The 3d model url.
