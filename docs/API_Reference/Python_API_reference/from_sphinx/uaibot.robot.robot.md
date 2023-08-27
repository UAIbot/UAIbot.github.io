--- 
layout: default
title: uaibot.robot.robot
parent: uaibot.robot
grand_parent: Python API reference
--- 

# uaibot.robot.robot module

<a id="module-uaibot.robot.robot"></a>

### *class* uaibot.robot.robot.Robot(name, links, list_base_3d_obj=None, htm=array([[1., 0., 0., 0.], [0., 1., 0., 0.], [0., 0., 1., 0.], [0., 0., 0., 1.]]), htm_base_0=array([[1., 0., 0., 0.], [0., 1., 0., 0.], [0., 0., 1., 0.], [0., 0., 0., 1.]]), htm_n_eef=array([[1., 0., 0., 0.], [0., 1., 0., 0.], [0., 0., 1., 0.], [0., 0., 0., 1.]]), q0=None, eef_frame_visible=True, joint_limits=None)

Bases: `object`

A class that contains a robot object in uaibot.

## Parameters

name
: The robot name.
  (default: ‘genRobot’).

htm_base_0
: The robot base’s configuration.
  (default: 4x4 identity matrix).

list_base_3d_obj
: The list of 3d models of the base of the robot.
  If set to None, there is no base 3d object.
  (default: None).

links
: The list of link objects.

q0
: The robot initial configuration.
  (default: zero vector).

eef_frame_visible
: Set if the end-effector frame is visible.
  (default: True).

joint_limit
: A n x 2 numpy array containing the joint limits, either in rad or meters.
  If set to ‘None’, use very large joint limits.
  (default: None).

#### add_ani_frame(time, q=None, htm=None, enforce_joint_limits=False)

Add a single configuration to the object’s animation queue.

### Parameters

time: positive float
: The timestamp of the animation frame, in seconds.

q
: The manipulator’s joint configuration.

htm
: The robot base’s configuration.
  (default: the same as the current HTM).

enforce_joint_limits: boolean
: If True and some q violates the joint limits (seen in the attribute ‘joint_limit’), the
  respective q is clamped. Note that it DOES NOT issue any warning for this. So, be aware.
  (default: False).

### Returns

None

#### add_col_object(sim)

Add the objects that compose the collision model to a simulation.

### Parameters

sim
: ‘Simulation’ object.

#### attach_object(obj)

Attach an object to the end-effector.
The list of the type of objects that can be grouped can be seen in ‘Utils.IS_GROUPABLE’.

### Parameters

obj
: Object to be attached.

#### *property* attached_objects

Data structures containing the objects attached into the robot.

#### check_free_configuration(q=None, htm=None, obstacles=[], check_joint=True, check_auto=True, tol=0.0005, dist_tol=0.005, no_iter_max=20)

Check if the joint configuration q is in the free configuration space, considering
joint limits, collision with obstacles and auto collision. It also outputs a message about a
possible violation.

For efficiency purposes, the program halts in the first violation it finds (if there is any).
So, the message, if any, is only about one of the possible violations. There can be more.

### Parameters

q
: The manipulator’s joint configuration.
  (default: the current joint configuration (robot.q) for the manipulator).

obstacles
: A list of obstacles as simple objects (see Utils.IS_SIMPLE)
  (default: empty list).

htm
: The robot base’s configuration.
  (default: the same as the current htm).

check_joint: boolean
: If joint limits should be considered or not.
  (default: True).

check_auto: boolean
: If auto collision should be considered or not.
  (default: True).

tol
: Tolerance for convergence in the iterative algorithm, in meters.
  (default: 0.0005 m).

dist_tol
: The tolerance to consider that two links are colliding.
  (default: 0.005 m).

no_iter_max
: The maximum number of iterations for the distance computing algorithm.
  (default: 20 iterations).

### Returns

is_free
: If the configuration is free or not.

message: string
: A message about what is colliding (is otherwise just ‘Ok!’).

info: list
: Contains a list with information of the violation of free space (if there is any, otherwise
  it is empty). The first element is the violation type: either 0 (lower joint limit violated), 1 (upper joint
  limit violated) 2 (collision with obstacles) and 3 (collision between links). The last elements depends on
  the violation type.
  <br/>
  If lower joint limit or upper joint limit, contains which joint was violated.
  <br/>
  If collision with obstacles, contains the list [i,isub,j], containing the index of the link i
  i, the index of the collision object in the link isub and the obstacle index in the list, j.
  <br/>
  If collision, contains the list [i,isub,j,jsub], containing the index of the first link i,
  the index of the collision object in the first link isub, the index of the second link j and
  the index of the collision object in the second link jsub.

#### compute_dist(obj, q=None, htm=None, old_dist_struct=None, tol=0.0005, no_iter_max=20, max_dist=inf)

Compute the  distance structure from each one of the robot’s link to a
‘simple’ external object (see Utils.IS_SIMPLE), given a joint and base
configuration.

This function can be faster if some distance computations are avoided.
See the description of the parameter ‘max_dist’.

Use an iterative algorithm, based on projections
(Von Neumann’s cyclic projection algorithm).

### Parameters

obj
: The external object for which the distance structure is going to be 
  computed, for each robot link.

q
: The manipulator’s joint configuration.
  (default: the current  joint configuration (robot.q) for the manipulator).

htm
: The robot base’s configuration.
  (default: the same as the current htm).

old_dist_struct
: ‘DistStructRobotObj’ obtained previously for the same robot and external object.
  Can be used to enhance the algorithm speed using the previous closest
  point as an initial guess.
  (default: None).

tol
: Tolerance for convergence in the iterative algorithm, in meters.
  (default: 0.0005 m).

no_iter_max
: The maximum number of iterations for the algorithm.
  (default: 20 iterations).

max_dist: positive float
: The algorithm uses an axis aligned bounding box (aabb) to avoid some distance computations.
  The algorithm skips a more precise distance computation if the distance between the aabb
  of the primitive objects composing the link and ‘obj’ is less than ‘max_dist’ (in meters).
  (default: infinite).

### Returns

dist_struct
: Distance struct for each one of the m objects that compose the robot’s
  collision model. Contains a list of m ‘DistStructLinkObj’ objects.

#### compute_dist_auto(q=None, old_dist_struct=None, tol=0.0005, no_iter_max=20, max_dist=inf)

Compute the  distance structure from each one of the robot’s links to itself
(auto collision), given a joint and base configuration.

This function consider only non-sequential links, since the collision between
sequential links in the kinematic chain can be verified by checking joint limits.
This saves times. This verification should be done elsewhere (by checking if the
configuration is inside the joint limits).

This function can be faster if some distance computations are avoided.
See the description of the parameter ‘max_dist’.

Use an iterative algorithm, based on projections
(Von Neumann’s cyclic projection algorithm).

### Parameters

q
: The manipulator’s joint configuration.
  (default: the current  joint configuration (robot.q) for the manipulator).

old_dist_struct
: ‘DistStructRobotAuto’ obtained previously for the same robot.
  Can be used to enhance the algorithm speed using the previous closest
  point as an initial guess.
  (default: None).

tol
: Tolerance for convergence in the iterative algorithm, in meters.
  (default: 0.0005 m).

no_iter_max
: The maximum number of iterations for the algorithm.
  (default: 20 iterations).

max_dist: positive float
: The algorithm uses an axis aligned bounding box (aabb) to avoid some distance computations.
  The algorithm skips a more precise distance computation if the distance between the aabb
  of the primitive objects composing the link and ‘obj’ is less than ‘max_dist’ (in meters).
  (default: infinite).

### Returns

dist_struct
: Distance struct for each one of the m objects that compose the robot’s
  collision model. Contains a list of m ‘DistStructLinkLink’ objects.

#### const_control(htm_des, q=None, htm=None, obstacles=[], dict_old_dist_struct=None, eta_obs=0.5, eta_joint=0.5, eta_auto=0.5, dist_safe_obs=0.01, dist_safe_auto=0.01, max_dist_obs=inf, max_dist_auto=inf, task_rate_fun=0.5, eps=0.001)

Computes the constrained joint velocity aiming a target pose (htm_des).
Consider three kind of constraints: collision with obstacles, joint limits and
auto collision.

The obstacles should be simple objects (see Utils.IS_SIMPLE for the list).

### Parameters

htm_des :4x4 numpy array or 4x4 nested list
: The desired pose for the end-effector of the robot.

q
: The joint configuration in which we want to compute the control action.
  (default: the current joint configuration for the robot).

htm
: The robot base’s configuration.
  (default: the same as the current HTM).

obstacles
: A list of obstacles as simple objects (see Utils.IS_SIMPLE)
  (default: empty list).

dict_old_dist_struct: a dictionary that maps each obstacle to a ‘DistStructRobotObj’
: Used to speed up computation using data from a previous run. The output
  ‘dict_dist_struct’ of this function can be fed as this parameter in a next
  call. If None is provided, this speed up is ignored.
  (default: None)

eta_obs
: Parameter that controls obstacle avoidance, measured in s^(-1)
  (inverse seconds). The rule is that the rate of approximation
  to each obstacle, in meters per seconds, should be at most:
  <br/>
  eta_obs \* (distance-safe_distance).
  <br/>
  So, the higher is this value, the less the robot
  is “afraid” of obstacles. Not that if this value is too high
  there can be collisions. If this value is np.inf, obstacle avoidance
  is skipped.
  (default: 0.5 s^(-1)).

eta_joint
: Parameter that controls joint limits avoidance, measured in s^(-1)
  (inverse seconds). The rule is that the rate of approximation
  to each joint limit, in meters per seconds, should be at most:
  <br/>
  eta_joint \* (distance to joint limit).
  <br/>
  So, the higher is this value, the less the robot
  is “afraid” of joint limits. Not that if this value is too high
  there can be collisions. If this value is np.inf, joint limits
  are skipped.
  (default: 0.5 s^(-1)).

eta_joint
: Parameter that controls joint limits avoidance, measured in s^(-1)
  (inverse seconds). The rule is that the rate of approximation
  to each joint limit, in meters per seconds, should be at most:
  <br/>
  eta_joint \* (distance to joint limit -safe_distance).
  <br/>
  So, the higher is this value, the less the robot
  is “afraid” of joint limits. Not that if this value is too high
  there can be collisions. If this value is np.inf, joint limits
  are skipped.
  (default: 0.5 s^(-1)).

eta_auto
: Parameter that controls auto collision avoidance, measured in s^(-1)
  (inverse seconds). The rule is that the rate of approximation
  between each non-sequential link, in meters per seconds, should be at most:
  <br/>
  eta_auto \* (distance -safe_distance).
  <br/>
  So, the higher is this value, the less the robot
  is “afraid” of auto collision. Not that if this value is too high
  there can be collisions. If this value is np.inf, auto collision is
  skipped.
  (default: 0.5 s^(-1)).

dist_safe_obs
: Parameter that controls a safety margin to collision to obstacles,
  in meters.
  (default: 0.01 meter).

dist_safe_auto
: Parameter that controls a safety margin to auto collision,
  in meters.
  (default: 0.01 meter).

max_dist_obs
: Controls the maximum distance considered to skip collision between the object
  and obstacles. See the parameter ‘max_dist’ in the function ‘compute_dist’ of
  the robot.
  (default: np.inf).

max_dist_auto
: Controls the maximum distance considered when skipping collision between the object
  and itself (auto collision). See the parameter ‘max_dist’ in the function ‘compute_dist’ of
  the robot.
  (default: np.inf).

task_rate_fun
: const_fun should be either a function handle that receives a 6x1 numpy column vector and
  outputs a 6x1 numpy column vector or a positive float.
  <br/>
  If task_rate_fun is a function f(r), it controls the target task function decrease. So we
  aim to have the task function decrease dr/dt as -f(r). In order to be suitable function, there
  should exist a positive definite function V(r) such that grad -V(r).T \* f(r) <=0. This is
  not checked and is a responability of the user.
  <br/>
  If task_rate_fun is a positive float, is the same result as using the function handle
  lambda r : task_rate_fun\*r. In this case V(r) = ||r||² is suitable.
  (default: 0.5).

eps
: Damping factor. Control inputs generated by this procedure can be quite noisy/discontinuous. The
  higher is this value, the less is this behaviour. However, this can generate steady state errors
  in the controller.
  (default: 0.001).

### Returns

qdot, failure, r, dict_dist_struct

qdot
: The joint velocity that can be used to control.

failure: boolean
: The controller is computed using a quadratic program. If the problem is unfeasible,
  then this variable returns ‘false. This typically happens when the configuration
  ‘q’ violates one of the constraints (collision to obstacle, joint limits or
  auto collision).

r
: The task vector.

dict_dist_struct
: Used to speed up computation using data from a previous run. This output can be
  fed as the parameter ‘dict_old_dist_struct’ in a next call.

#### const_control_mod(htm_des, q=None, htm=None, obstacles=[], dict_old_dist_struct=None, eta_obs=0.5, eta_joint=0.5, eta_auto=0.5, dist_safe_obs=0.01, dist_safe_auto=0.01, max_dist_obs=inf, max_dist_auto=inf, task_rate_fun=0.5, eps=0.001)

#### *static* coop_task_function(robot_a, robot_b, htm_a_des, htm_a_b_des, q_a=None, q_b=None)

Computes the 12-dimensional task function for end-effector pose control
of two robots ‘robot_a’, ‘robot_b’ given their respective configurations
q_a and q_b.

The first three components are relative position error.

The second three components are relative orientation error.

The third three components are position error for ‘robot_a’.

The third three components are orientation error for ‘robot_a’.

Everything is written in scenario coordinates.

Also returns the Jacobian of this function.

### Parameters

robot_a :robot object
: The first robot.

robot_b :robot object
: The second robot.

htm_a_des :4x4 numpy array or 4x4 nested list
: The desired pose for the end-effector of ‘robot_a’.

htm_a_b_des :4x4 numpy array or 4x4 nested list
: The desired relative pose between the end-effector of ‘robot_a’ and
  ‘robot_b’. That is, inv(htmA) \* htmB.

q_a
: ‘robot_a’’ joint configuration
  (default: the current  joint configuration (robot.q) for ‘robot_a’).

q_b
: ‘robot_b’’ joint configuration
  (default: the current  joint configuration (robot.q) for ‘robot_b’).

### Returns

r
: The task vector.

jac_r
: The respective task Jacobian.

#### *static* create_abb_crb(htm=array([[1., 0., 0., 0.], [0., 1., 0., 0.], [0., 0., 1., 0.], [0., 0., 0., 1.]]), name='abbcrb', color='white', opacity=1, eef_frame_visible=True)

Create a ABB CRB 15000, a six degree of freedom manipulator.
Model taken from the ROS github repository ([https://github.com/ros-industrial/abb_experimental](https://github.com/ros-industrial/abb_experimental)).

### Parameters

htm
: The initial base configuration for the robot.
  (default: np.identity(4))

name
: The robot name.
  (default: ‘abbcrb’).

htm
: A HTML-compatible string representing the object color.
  (default: ‘white’)’.

opacity
: The opacity of the robot. 1 = fully opaque and 0 = transparent.
  (default: 1)

### Returns

robot
: The robot.

#### *static* create_darwin_mini(htm=array([[1., 0., 0., 0.], [0., 1., 0., 0.], [0., 0., 1., 0.], [0., 0., 0., 1.]]), name='darwin_mini', color='#3e3f42', opacity=1, eef_frame_visible=True)

Create an (oversized) Darwin Mini, a humanoid robot.
Thanks to Alexandre Le Falher for the 3D model ([https://grabcad.com/library/darwin-mini-1](https://grabcad.com/library/darwin-mini-1)).

### Parameters

htm
: The initial base configuration for the robot.
  (default: np.identity(4))

name
: The robot name.
  (default: ‘darwin_mini’).

htm
: A HTML-compatible string representing the object color.
  (default: ‘#3e3f42’).

opacity
: The opacity of the robot. 1 = fully opaque and 0 = transparent.
  (default: 1)

### Returns

robot
: The robot. It is composed of a group of six objects: the two arms and legs (members of ‘Robot’ class)
  and the chest and head (both ‘RigidObject’ class)

#### *static* create_epson_t6(htm=array([[1., 0., 0., 0.], [0., 1., 0., 0.], [0., 0., 1., 0.], [0., 0., 0., 1.]]), name='epsont6', color='white', opacity=1, eef_frame_visible=True)

Create an Epson T6, a SCARA manipulator.
Thanks KUA for the 3d model (see [https://grabcad.com/library/epson-t6-scara-robot-1](https://grabcad.com/library/epson-t6-scara-robot-1)).

### Parameters

htm
: The initial base configuration for the robot.
  (default: np.identity(4))

name
: The robot name.
  (default: ‘epsont6’).

htm
: A HTML-compatible string representing the object color.
  (default: ‘white’)’.

opacity
: The opacity of the robot. 1 = fully opaque and 0 = transparent.
  (default: 1)

### Returns

robot
: The robot.

#### *static* create_franka_ermika_3(htm=array([[1., 0., 0., 0.], [0., 1., 0., 0.], [0., 0., 1., 0.], [0., 0., 0., 1.]]), name='frankaermika', color='silver', opacity=1, eef_frame_visible=True)

Create a Franka Ermika 3, a seven degree of freedom manipulator.
Model taken from the ROS github repository ([https://github.com/BolunDai0216/FR3Env/tree/d5218531471cadafd395428f8c2033f6feeb3555/FR3Env/robots/meshes/visual](https://github.com/BolunDai0216/FR3Env/tree/d5218531471cadafd395428f8c2033f6feeb3555/FR3Env/robots/meshes/visual)).

### Parameters

htm
: The initial base configuration for the robot.
  (default: np.identity(4))

name
: The robot name.
  (default: ‘frankaermika’).

htm
: A HTML-compatible string representing the object color.
  (default: ‘silver’)’.

opacity
: The opacity of the robot. 1 = fully opaque and 0 = transparent.
  (default: 1)

### Returns

robot
: The robot.

#### *static* create_kuka_kr5(htm=array([[1., 0., 0., 0.], [0., 1., 0., 0.], [0., 0., 1., 0.], [0., 0., 0., 1.]]), name='kukakr5', color='#df6c25', opacity=1, eef_frame_visible=True)

Create a Kuka KR5 R850, a six-degree of freedom manipulator.
Thanks Sugi-Tjiu for the 3d model (see [https://grabcad.com/library/kuka-kr-5-r850](https://grabcad.com/library/kuka-kr-5-r850)).

### Parameters

htm
: The initial base configuration for the robot.
  (default: np.identity(4))

name
: The robot name.
  (default: ‘kukakr5’).

htm
: A HTML-compatible string representing the object color.
  (default: ‘#df6c25’)’.

opacity
: The opacity of the robot. 1 = fully opaque and 0 = transparent.
  (default: 1)

### Returns

robot
: The robot.

#### *static* create_kuka_kr5_per(htm=array([[1., 0., 0., 0.], [0., 1., 0., 0.], [0., 0., 1., 0.], [0., 0., 0., 1.]]), name='kukakr5', color='#df6c25', opacity=1, eef_frame_visible=True, per=0.05)

Create a Kuka KR5 R850, a six-degree of freedom manipulator.
Thanks Sugi-Tjiu for the 3d model (see [https://grabcad.com/library/kuka-kr-5-r850](https://grabcad.com/library/kuka-kr-5-r850)).

### Parameters

htm
: The initial base configuration for the robot.
  (default: np.identity(4))

name
: The robot name.
  (default: ‘kukakr5’).

htm
: A HTML-compatible string representing the object color.
  (default: ‘#df6c25’)’.

opacity
: The opacity of the robot. 1 = fully opaque and 0 = transparent.
  (default: 1)

### Returns

robot
: The robot.

#### *static* create_kuka_lbr_iiwa(htm=array([[1., 0., 0., 0.], [0., 1., 0., 0.], [0., 0., 1., 0.], [0., 0., 0., 1.]]), name='kukalbriiwa', color='silver', opacity=1, eef_frame_visible=True)

Create a Kuka LBR IIWA 14 R820, a seven degree of freedom manipulator.
Model taken from the ROS github repository ([https://github.com/ros-industrial/kuka_experimental](https://github.com/ros-industrial/kuka_experimental)).

### Parameters

htm
: The initial base configuration for the robot.
  (default: np.identity(4))

name
: The robot name.
  (default: ‘kukalbriiwa’).

htm
: A HTML-compatible string representing the object color.
  (default: ‘silver’)’.

opacity
: The opacity of the robot. 1 = fully opaque and 0 = transparent.
  (default: 1)

### Returns

robot
: The robot.

#### *static* create_staubli_tx60(htm=array([[1., 0., 0., 0.], [0., 1., 0., 0.], [0., 0., 1., 0.], [0., 0., 0., 1.]]), name='staublitx60', color='#ff9b00', opacity=1, eef_frame_visible=True)

Create a Staubli TX60, a six degree of freedom manipulator.
Model taken from the ROS github repository ([https://github.com/ros-industrial/staubli](https://github.com/ros-industrial/staubli)).

### Parameters

htm
: The initial base configuration for the robot.
  (default: np.identity(4))

name
: The robot name.
  (default: ‘staublitx60’).

htm
: A HTML-compatible string representing the object color.
  (default: ‘#ff9b00’)’.

opacity
: The opacity of the robot. 1 = fully opaque and 0 = transparent.
  (default: 1)

### Returns

robot
: The robot.

#### detach_object(obj)

Detach an object (ball, box or cylinder) to the end-effector.

### Parameters

obj
: Object to be detached.

#### dyn_model(q, qdot)

Compute the three robot’s dynamic model terms, in a given joint configuration ‘q’
and joint speed ‘qdot’.

### Parameters

q
: The manipulator’s joint configuration.

qdot
: The manipulator’s joint configuration speed.

### Returns

dyn_m
: The generalized inertia matrix at the joint configuration q.

dyn_c
: The generalized Coriolis-Centrifugal torques at the joint
  configuration q and joint configuration speed qdot.

dyn_g
: The generalized gravity torques at the joint configuration q.

#### *property* eef_frame_visible

If the frame attached to the end effector is visible

#### fkm(q=None, axis='eef', htm=None)

Compute the forward kinematics for an axis at a given joint and base
configuration. Everything is written in the scenario coordinates.

### Parameters

q
: The manipulator’s joint configuration.
  (default: the current  joint configuration (robot.q) for the manipulator).

axis
: For which axis you want to compute the FK:
  ‘eef’: for the end-effector;
  ‘dh’: for all Denavit-Hartenberg axis;
  ‘com’: for all center-of-mass axis.
  (default: ‘eef’).

htm
: The robot base’s configuration.
  (default: the same as the current HTM).

### Returns

htm_fk
: For axis=’eef’, returns a single htm. For the other cases, return
  n htms as a nx4x4 numpy matrix.

#### gen_code()

Generate code for injection.

#### *property* htm

The current base configuration in scenario coordinates.
A 4x4 homogeneous matrix written is scenario coordinates.

#### *property* htm_base_0

The constant homogeneous transformation between the HTM of the base and
the HTM of the first Denavit-Hartenberg frame.

#### *property* htm_n_eef

The constant homogeneous transformation between the HTM of the last
Denavit-Hartenberg frame and the end-effector

#### ikm(htm_target, q0=None, p_tol=0.005, a_tol=5, no_iter_max=2000, ignore_orientation=False)

Try to solve the inverse kinematic problem for the end-effector, given a
desired homogeneous transformation matrix. It returns the manipulator
configuration.

Important: it disregards the current htm of the base of the robot. That is,
it assumes that robot.htm = np.identity(4). You can easily consider other
cases by transforming htm_target as Utils.inv_htm(robot.htm) \* htm_target.

Uses an iterative algorithm.

The algorithm can fail, throwing an Exception when it happens.

### Parameters

htm_target
: The target end-effector HTM, written in scenario coordinates.

q0
: Initial guess for the algorithm for the joint configuration.
  (default: a random joint configuration).

p_tol
: The accepted error for the end-effector position, in meters.
  (default: 0.005 m).

a_tol
: The accepted error for the end-effector orientation, in degrees.
  (default: 5 degrees).

no_iter_max
: The maximum number of iterations for the algorithm.
  (default: 2000 iterations).

ignore_orientation: boolean
: If True, the orientation part of the HTM is ignored. Task is position-only.
  (default: False)

### Returns

q
: The configuration that solves the IK problem.

#### jac_ana(q=None, htm=None)

Compute the analytic Jacobian for the end-effector. The Euler angle
convention is zyx. Also returns the end-effector htm and Euler angles
as a by-product.

### Parameters

q
: The manipulator’s joint configuration
  (default: the current  joint configuration (robot.q) for the manipulator).

htm
: The robot base’s configuration.
  (default: the same as the current htm).

### Returns

jac_ana
: The analytic Jacobian.

htm_eef
: The end-effector htm.

phi
: The euler angles in the z (alpha), y (beta) and x (gamma) convention,
  as a column vector.

#### jac_geo(q=None, axis='eef', htm=None)

Compute the geometric Jacobian for an axis at a given joint and base
configuration. Also returns the forward kinematics as a by-product.
Everything is written in the scenario coordinates.

### Parameters

q
: The manipulator’s joint configuration 
  (default: the current  joint configuration (robot.q) for the manipulator).

axis
: For which axis you want to compute the FK:
  ‘eef’: for the end-effector;
  ‘dh’: for all Denavit-Hartenberg axis;
  ‘com’: for all center-of-mass axis.
  (default: ‘eef’).

htm
: The robot base’s configuration.
  (default: the same as the current htm).

### Returns

jac_geo
: For axis=’eef’, returns a single 6xn Jacobian. For the other cases, 
  return n Jacobians as a nx6xn numpy matrix.

htm_out
: For axis=’eef’, returns a single htm. For the other cases, return
  n htms as a n x 4 x 4 numpy matrix.

#### jac_jac_geo(q=None, axis='eef', htm=None)

Compute the Jacobians of the columns of the geometric Jacobian in the joint variable ‘q’.
This can be either to the end-effector frames (axis=’eef’), to the Denavit-Hartenberg (DH) frames
(axis=’dh’) or to the center-of-mass (COM) frames (axis=’com’).

If axis =’dh’ or ‘com’:

If the robot has n links, jj_geo = robot.jac_jac_geo(q, htm) is a list of lists, in which
jj_geo[i][j] is a 6 x n matrix that represents the Jacobian of the j-th column of the geometric
Jacobian matrix of the i-th DH or COM frame.

jj_geo[i][j] for j>i is not computed, because the j-th column of the geometric Jacobian matrix of the
i-th DH or COM frame is always the 6 x n zero matrix, regardless of the ‘q’ and ‘htm’ chosen.

jj_geo[i][j] could be alternatively computed numerically. For example, for axis=’dh’, by defining the function of q
f = lambda q_var: np.matrix(robot.jac_geo(q = q_var, htm = htm, axis = ‘dh’)[0][i][j])
and then computing the numerical Jacobian as Utils.jac(f,q).
However, this function  is faster and has greater numerical accuracy, since it is computed analytically
instead of numerically.

If axis=’eef’, this is the same as computing axis=’dh’ but throwing away all but the last list away.

### Parameters

q
: The manipulator’s joint configuration
  (default: the current  joint configuration (robot.q) for the manipulator).

axis
: For which axis you want to compute the FK:
  ‘eef’: for the end-effector;
  ‘dh’: for all Denavit-Hartenberg axis;
  ‘com’: for all center-of-mass axis.
  (default: ‘eef’).

htm
: The robot base’s configuration.
  (default: the same as the current htm).

### Returns

jj_geo
: The Jacobian of the j-th column of the geometric Jacobian matrix of the i-th Denavit-Hartenberg frame.

#### *property* joint_limit

A n x 2 numpy array containing the joint limits, either in rad or meters

#### *property* links

Data structures containing the links of the robot.

#### *property* list_object_3d_base

The list of 3d objects that form the base.

#### *property* name

Name of the object.

#### *property* q

The current joint configuration.

#### *property* q0

The default joint configuration.

#### set_ani_frame(q=None, htm=None, enforce_joint_limits=False)

Reset object’s animation queue and add a single configuration to the 
object’s animation queue.

### Parameters

q
: The manipulator’s joint configuration .
  (default: the current  joint configuration (robot.q) for the manipulator, q0).

htm
: The robot base’s configuration.
  (default: the same as the current HTM).

enforce_joint_limits: boolean
: If True and some q violates the joint limits (seen in the attribute ‘joint_limit’), the
  respective q is clamped. Note that it DOES NOT issue any warning for this. So, be aware.
  (default: False).

### Returns

None

#### set_htm_to_eef(htm)

#### task_function(htm_des, q=None, htm=None)

Computes the 6-dimensional task function for end-effector pose control,  
given a joint configuration, a base configuration and the desired pose 
‘htm_des’.

The first three entries are position error, and the three last entries are
orientation error.

Everything is written in scenario coordinates.

Also returns the Jacobian of this function.

### Parameters

htm_des
: The desired end-effector pose.

q
: The manipulator’s joint configuration.
  (default: the current  joint configuration (robot.q) for the manipulator).

htm
: The robot base’s configuration.
  (default: the same as the current htm).

### Returns

r
: The task function.

jac_r
: The respective task Jacobian.

#### update_col_object(time)

Update internally the objects that compose the collision model to the
current configuration of the robot.

#### *static* vector_field(curve, alpha=1, const_vel=1)

Computes a handle to a vector field function fun(p). Uses the vector field
presented in

“Adriano M. C. Rezende; Vinicius M. Goncalves; Luciano C. A. Pimenta: 
Constructive Time-Varying Vector Fields for Robot Navigation 
IEEE Transactions on Robotics (2021)”.

The vector field has constant velocity and use the function 
G(u) = (2/pi)\*atan(alpha\*u).

### Parameters

curve
: Curve, described as sampled points. Each one of the n rows should 
  contain a m-dimensional float vector that is the n-th m-dimensional
  sampled point of the curve.

alpha
: Controls the vector field behaviour. Greater alpha’s imply more 
  robustness to the vector field, but increased velocity and acceleration
  behaviours. Used in G(u) = (2/pi)\*atan(alpha\*u)
  (default: 1).

const_vel
: The constant velocity of the vector field. The signal of this number 
  controls the direction of rotation 
  (default: 1).

### Returns

fun: a function handle that you can call as f(p), returning a numpy column vector. ‘p’ should be a
: m-dimensional vector.
