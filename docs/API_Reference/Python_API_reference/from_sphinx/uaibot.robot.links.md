--- 
layout: default
title: uaibot.robot.links
parent: uaibot.robot
grand_parent: Python API reference
--- 

# uaibot.robot.links module

<a id="module-uaibot.robot.links"></a>

### *class* uaibot.robot.links.Link(joint_number, theta, d, alpha, a, joint_type, list_model_3d, mass=1, com_coordinates=[0, 0, 0], inertia_matrix=array([[1., 0., 0.], [0., 1., 0.], [0., 0., 1.]]), show_frame=False)

Bases: `object`

A class that contains the information of the links of the robot.

## Parameters

joint_number
: The joint number in the kinematic chain (0 is the first joint).

theta
: The ‘theta’ parameter in the Denavit-Hartenberg convention (rotation in z), in rad.

d
: The ‘d’ parameter in the Denavit-Hartenberg convention (displacement in z), in meters.

alpha
: The ‘alpha’ parameter in the Denavit-Hartenberg convention (rotation x), in rad.

a
: The ‘a’ parameter in the Denavit-Hartenberg convention (displacement in x), in meters.

joint_type
: The joint type. “0” is rotative and “1” is prismatic.

list_model_3d
: The 3d models that compose the links.

mass
: The link mass, in kg.
  (default: 1 kg).

com_coordinates
: The coordinates of the center of mass of the object, written in its Denavit-Hartenberg frame and
  in meters.
  (default: [0,0,0]).

inertia_matrix
: The link’s inertia matrix, in kg m². Its is calculated with respect to the attached Denavit-Hartenberg frame, and thus
  is a constant along the motion.
  (default: np.identity(3)).

#### *property* a

The ‘a’ parameter of the Denavit-Hartenberg convention (in meters)

#### *property* alpha

The ‘alpha’ parameter of the Denavit-Hartenberg convention (in rad)

#### attach_col_object(obj, htm)

Attach an object (ball, box or cylinder) into the link as a collision
object.

### Parameters

obj: object
: Object to be added.

htm
: The transformation between the link’s HTM and the object’s HTM

#### *property* col_objects

Collection of objects that compose the collision model of the link.

#### *property* com_coordinates

The coordinates, written in the link’s Denavit-Hartenberg frame and in meters, of the center-of-mass
point of the link.

#### *property* d

The ‘d’ parameter of the Denavit-Hartenberg convention (in meters)

#### gen_code(name)

Generate code for injection.

#### *property* inertia_matrix

The link’s inertia matrix, in kg m². Its is calculated with respect to the attached Denavit-Hartenberg frame, and thus
is a constant along the motion.

#### *property* joint_number

The joint number in the kinematic chain.

#### *property* joint_type

The joint type (0=revolute, 1=prismatic).

#### *property* list_model_3d

The list of 3d models of the object.

#### *property* mass

The link’s mass, in kg.

#### *property* show_frame

If the Denavit-Hartenberg frame of the link is displayed in simulation.

#### *property* theta

The ‘theta’ parameter of the Denavit-Hartenberg convention (in rad)
