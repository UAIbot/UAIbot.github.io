---
layout: default
title: uaibot.utils
parent: Python API reference
---

# uaibot.utils module

<a id="module-uaibot.utils"></a>

### *class* uaibot.utils.Utils

Bases: `object`

A library that contains some utilities for UAIbot. All of the functions are static.

#### IS_GROUPABLE *= ['uaibot.Ball', 'uaibot.Box', 'uaibot.SmoothBox', 'uaibot.Cylinder', 'uaibot.Frame', 'uaibot.RigidObject', 'uaibot.Group', 'uaibot.Robot', 'uaibot.PointLight', 'uaibot.Cone']*

#### IS_OBJ_SIM *= ['uaibot.Ball', 'uaibot.Box', 'uaibot.SmoothBox', 'uaibot.Cylinder', 'uaibot.Cone', 'uaibot.Robot', 'uaibot.PointLight', 'uaibot.Frame', 'uaibot.PointCloud', 'uaibot.Vector', 'uaibot.RigidObject', 'uaibot.Group', 'uaibot.HTMLDiv']*

#### IS_SIMPLE *= ['uaibot.Ball', 'uaibot.Box', 'uaibot.Cylinder', 'uaibot.SmoothBox', 'uaibot.Cone']*

#### *static* S(v)

Returns a 3x3 matrix that implements the cross product for a 3D vector  
as a matricial product, that is, a matrix S(v) such that for any other 
3D column  vector w, S(v)w = cross(v,w).

## Parameters

v
: The vector for which the S matrix will be created.

## Returns

S
: A matrix that implements the cross product with v.

#### UAIBOT_NAME_TYPES *= ['uaibot.', 'cylinder.', 'box.', 'smoothbox.', 'ball.', 'robot.', 'simulation.', 'meshmaterial.', 'texture.', 'pointlight.', 'frame.', 'model3d.', 'links.', 'pointcloud.', 'vector.', 'rigidobject.', '.group', '.htmldiv']*

#### *static* axis_angle(htm)

Given an homogeneous transformation matrix representing a rotation, 
return the rotation axis angle.

## Parameters

htm: 4X4 numpy array or nested list 
: Homogeneous transformation matrix of the rotation.

## Returns

axis
: The rotation axis.

angle
: The rotation angle, in radians.

#### *static* bissection(fun, t0, tf, eps)

#### *static* compute_aabbdist(obj1, obj2)

#### *static* compute_dist(obj_a, obj_b, p_a_init=None, tol=0.001, no_iter_max=20)

#### *static* cubicsolve(p, lam)

#### *static* dp_inv(mat, eps=0.001)

Compute the damped pseudoinverse of the matrix ‘mat’.

## Parameters

mat: nxm numpy array
: The matrix to compute the damped pseudoinverse.

eps: positive float
: The damping factor.
  (default: 0.001).

## Returns

pinvA: mxn numpy array
: The damped pseudoinverse of ‘mat’.

#### *static* euler_angles(htm)

Computer the Euler angles of a rotation matrix.
Find alpha, beta and gamma such that.

htm = Utils.rotz(alpha) \* Utils.roty(beta) \* Utils.rotx(gamma).

## Parameters

htm: 4X4 numpy array or nested list
: Homogeneous transformation matrix of the rotation.

## Returns

alpha
: Rotation in z, in radians.

beta
: Rotation in y, in radians.

gamma
: Rotation in x, in radians.

#### *static* fun_Cir(v, h, r)

#### *static* fun_Int(v, h, L)

#### *static* fun_Sph(v, h, r)

#### *static* generate_connectivity_info(mesh_triangle, h)

#### *static* get_data_from_model(path)

#### *static* get_uaibot_type(obj)

Return the UAIBot type of the object.
Return the empty string if it is not an UAIBot object.

## Parameters

obj: object
: Object to be verified.

## Returns

obj_type: string
: UAIBot type.

#### *static* hierarchical_solve(mat_a, mat_b, eps=0.001)

Solve the lexicographical unconstrained quadratic optimization problem

lexmin_x ||mat_a[i]\*x - b[i]||² + eps\*||x||²

with lower indexes having higher priority than higher indexes.

## Parameters

mat_a: A list of matrices (double arrays or numpy matrices).
: The matrices mat_a[i]. All must have the same number of columns.

mat_b: A list of column vectors (double arrays or numpy matrices).
: The vectors mat_b[i]. The number of rows of mat_b[i] must be equal to the number
  of rows of mat_a[i].

eps: positive float
: Damping parameter.
  (default: 0.001).

## Returns

x: numpy column vector
: The solution x. For positive eps, the solution is always unique.

#### *static* htm_rand(trn=1, rot=1.5707963267948966)

Returns a random homogeneous transformation matrix.

## Parameters

trn: float
: Maximum parameter for random translation in x, y and z.
  (default: 1)

rot: float
: Maximum parameter for random rotation in x, y and z.
  (default: 1)

## Returns

htm
: A homogeneous transformation matrix.

#### *static* interpolate(points)

Create a function handle that generates an one-time differentiable interpolated data from ‘points’.

The simplest case in when ‘points’ is a list with m elements. In this case, it will output a function f.
When this function is evaluated at a scalar t, it will coincide with points[i] when t = i/m, that is,
f(i/m) = points[i]. This function is once differentiable and periodic with period 1, so f(t+k)=f(t) for
an integer k.

The function can also use a n x m numpy array or lists as ‘points’. In this case, f(t) is a n dimensional
column vector in which its i-th entry is the same as computing f_i = interpolate(points[i]) and then
computing f_i(t).

Finally, t can be a list of k elements instead of just a scalar. In this case, f(t) is a n x k numpy matrix
in which the element at row i and column j is the same as computing f_i = interpolate(points[i]) and then
computing f_i(t[k]).

## Parameters

points: a n x m numpy array or lists
: Points to be interpolated.

## Returns

f: function handle
: The function handle that implements the interpolation.

#### *static* inv_htm(htm)

Given a homogeneous transformation matrix, compute its inverse.
It is faster than using numpy.linalg.inv in the case of HTMs.

## Parameters

htm: 4X4 numpy array or nested list 
: Homogeneous transformation matrix of the rotation.

## Returns

inv_htm: 4X4 numpy array
: The inverse of the transformation matrix.

#### *static* is_a_color(obj)

Check if the argument is a HTML-compatible string that represents a color.

## Parameters

obj: object
: Object to be verified.

## Returns

is_type: boolean
: If the object is of the type.

#### *static* is_a_groupable_object(obj)

Check if the argument is a groupable object.
Check the constant ‘Utils.IS_GROUPABLE’ for a list of groupable objects.

## Parameters

obj: object
: Object to be verified.

## Returns

is_type: boolean
: If the object is of the type.

#### *static* is_a_matrix(obj, n=None, m=None)

Check if the argument is a nxm matrix of floats.

## Parameters

obj: object
: Object to be verified.

n: positive int
: Number of rows
  (default: it does not matter).

m: positive int
: Number of columns
  (default: it does not matter).

## Returns

is_type: boolean
: If the object is of the type.

#### *static* is_a_name(string)

Check if the argument is a valid name for uaibot objects.
Only characters [a-z], [A-z], [0-9] and ‘_’ are allowed.
However, variables should not begin with numbers.

## Parameters

string: string
: Name to be verified.

## Returns

is_name: boolean
: If the name is a valid name.

#### *static* is_a_natural_number(obj)

Check if the argument is a natural number (integer and >=0)

## Parameters

obj: object
: Object to be verified.

## Returns

is_type: boolean
: If the object is of the type.

#### *static* is_a_number(obj)

Check if the argument is a float or int number

## Parameters

obj: object
: Object to be verified.

## Returns

is_type: boolean
: If the object is of the type.

#### *static* is_a_obj_sim(obj)

Check if the argument is an object that can be put into the simulator.
Check the constant ‘Utils.IS_OBJ_SIM’ for a list of objects that can be put in the simulator.

## Parameters

obj: object
: Object to be verified.

## Returns

is_type: boolean
: If the object is of the type.

#### *static* is_a_pd_matrix(obj, n=None)

Check if the argument is a symmetric nxn positive (semi)-definite matrix.

## Parameters

obj: object
: Object to be verified.

n: positive int
: Dimension of the square matrix
  (default: it does not matter).

## Returns

is_type: boolean
: If the object is of the type.

#### *static* is_a_simple_object(obj)

Check if the argument is a simple object.
Check the constant ‘Utils.IS_SIMPLE’ for a list of simple objects.

## Parameters

obj: object
: Object to be verified.

## Returns

is_type: boolean
: If the object is of the type.

#### *static* is_a_vector(obj, n=None)

Check if the argument is a n vector of floats.

## Parameters

obj: object
: Object to be verified.

n: positive int
: Number of elements
  (default: it does not matter).

## Returns

is_type: boolean
: If the object is of the type.

#### *static* is_url_available(url, types)

Try to access the content of the url ‘url’. Also verifies if the content is one of the extensions contained in
‘types’ (e.g, types = [‘png’, ‘bmp’, ‘jpg’, ‘jpeg’] for images).

Never throws an Exception, always returning a string with a message. Returns ‘ok!’ if and only if the
url was succesfully acessed and has the correct file type.

## Parameters

url: string
: The url string.

types: list of string
: The desired content extensions.

## Returns

message: string
: Message.

#### *static* jac(f, x, delta=0.0001)

Compute the numerical Jacobian of a function f at the point x.
Uses centralized finite difference to compute the derivatives.

## Parameters

f: function handle
: The function handle. It should accept a single ‘m’ dimensional numpy array/matrix
  which is a *column* matrix and return a single ‘n’ dimensional numpy/array/matrix
  which is a *column* matrix.

x: m dimensional numpy *columsn* array/matrix
: Point in which the Jacobian will be computed. This object should be of the same nature of the input of
  f, so f(x) is well-defined.

delta: float
: Variation used in the numerical differentiation
  (default: 0.0001)

## Returns

jac: n x m numpy array
: The numerical Jacobian of f at point x. It is a n x m numpy array.
  If f_i(x) is the i-th entry of f(x) (1<=i<=n) and x_j the j-th variable (1<=j<=m), then
  the entry in the i-th row and j-th column is partial f_i/partial x_j evaluated at x.

#### *static* plot(xv, yv, title='', xname='x', yname='y', labels='')

#### *static* rot(axis, angle)

Homogeneous transformation matrix that represents the rotation of an
angle in an axis.

## Parameters

axis
: The axis of rotation.

angle: float
: The angle of rotation, in radians.

## Returns

htm
: The homogeneous transformation matrix.

#### *static* rotx(angle)

Homogeneous transformation matrix that represents the rotation of an
angle in the ‘x’ axis.

## Parameters

angle: float
: The angle of rotation, in radians.

## Returns

htm
: The homogeneous transformation matrix.

#### *static* roty(angle)

Homogeneous transformation matrix that represents the rotation of an
angle in the ‘y’ axis.

## Parameters

angle: float
: The angle of rotation, in radians.

## Returns

htm
: The homogeneous transformation matrix.

#### *static* rotz(angle)

Homogeneous transformation matrix that represents the rotation of an
angle in the ‘z’ axis.

## Parameters

angle: float
: The angle of rotation, in radians.

## Returns

htm
: The homogeneous transformation matrix.

#### *static* softmax(x, h)

#### *static* softmin(x, h)

#### *static* softselectmax(x, y, h)

#### *static* softselectmin(x, y, h)

#### *static* trn(vector)

Homogeneous transformation matrix that represents the displacement
of a vector

## Parameters

vector
: The displacement vector.

## Returns

htm
: The homogeneous transformation matrix.
