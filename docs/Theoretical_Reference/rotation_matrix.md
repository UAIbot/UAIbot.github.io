---
layout: default
title: Rotation Matrix
nav_order: 1
parent: Theoretical Reference
---

# Rotation Matrix

In this context we have the following definition:

> A rotation matrix is a matrix $$Q\in \mathbb{R}^{3 \times 3}$$ with two properties:
1. $$Q^TQ = QQ^T = I_{3 \times 3}$$
2. $$\det(Q) = +1$$

In which $$I_{3 \times 3}$$ is the identity matrix of size $$3 \times 3$$.

The first condition $$Q^TQ=I_{3 \times 3}$$ has a geometric interpretation. Supose it is written as:

$$ Q = \LARGE{\Big(}\normalsize{}\begin{array}{ccc}
                        Q_{xx} & Q_{xy} & Q_{xz} \\
                        Q_{yx} & Q_{yy} & Q_{yz} \\
                        Q_{zx} & Q_{zy} & Q_{zz}
                        \end{array}\LARGE{\Big)}\normalsize{} = \left(\begin{array}{ccc}
                        Q_{x} & Q_y & Q_z
                        \end{array}\right)$$

In which $$Q_x$$ , $$Q_y$$ , and $$Q_z$$ are the columns of $$Q$$.

So, reading the first condition in terms of the columns, we deduce that they are orthonormal, that is, they describe vectors that are orthogonal to each other and of unit size:

$$ Q_x^TQ_y = Q_x^TQ_z = Q_y^TQ_z = 0 $$

$$ Q_x^TQ_x = Q_y^TQ_y = Q_z^TQ_z = 1.$$

That is, if we choose a reference (set of three orthogonal unit vectors) $$\mathcal{F}_0$$ and consider each column of $$Q$$ as a vector written in this reference frame, we will have, when we finish drawing the three vectors corresponding to the three columns, another set of vectors orthogonal to each other and unitary, that is, another reference frame, $$\mathcal{F}_1$$.

The second condition, ($$\det(Q)=+1$$) implies that this new reference $$\mathcal{F}_1$$ is positively oriented according to the right-hand rule.

This means that if you place your thumb on the $$x$$ axis with your right hand and the index finger on the $$y$$ axis, then the axis $$z$$ will be in the palm of your hand.

This procedure (interpreting the columns of a rotation matrix $$Q$$ as vectors in a frame of reference $$\mathcal{F}_0$$ , draw them and get another reference) is very relevant and will be addressed shortly. 

We then have the first interpretation for a rotation matrix $$Q$$:

> A rotation matrix $$Q$$ is a matrix that describes a change of reference frame $$\mathcal{F}_0$$ to another reference frame $$\mathcal{F}_1$$

Note that the two reference frames have the same center!

Now let's move on to the second interpretation of a rotation matrix $$Q$$.

> A rotation matrix $$Q$$ implements rotation, around a specific axis written in a reference frame $$\mathcal{F}_0$$ - following the right-hand rule - and from a specific angle, from a point.

### Example 1

Consider the rotation matrix $$Q$$:

$$Q = \Large{\Bigg(}\normalsize{}\begin{array}{ccc}
                        \frac{\sqrt{2}}{2} & -\frac{\sqrt{2}}{2} & 0 \\
                        \frac{\sqrt{2}}{2} & \frac{\sqrt{2}}{2} & 0 \\
                        0 & 0 & 1
                        \end{array}\Large{\Bigg)}\normalsize{}.$$

Consider a referential $$\mathcal{F}_0$$, and a point that is written as a column vector $$p$$ in $$\mathcal{F}_0$$. So the vector $$p'=Qp$$ represents, also written in $$\mathcal{F}_0$$, the point $$p$$ rotated 45 degrees on axis $$z_0$$.        

So, if:

$$p = \Large{\Bigg(}\normalsize{}\begin{array}{c}
                        \frac{\sqrt{2}}{2} \\
                        \frac{\sqrt{2}}{2} \\
                        \frac{1}{2}
                        \end{array}\Large{\Bigg)}\normalsize{} \ \ \ , \ \ \ p' = Qp =
                        \Large{\Bigg(}\normalsize{}\begin{array}{c}
                        0 \\
                        1 \\
                        \frac{1}{2}
                        \end{array}\Large{\Bigg)}.$$

The point $$p'$$ is the point $$p$$ rotated 45 degrees on axis $$z_0$$.

### Example 2

In UAIBot it is possible to calculate the axis and angle (in radians) of a rotation matrix using the `Utils.axis_angle` function:

```python
import numpy as np
import uaibot as ub

Q = np.array([[0,-1,0],[1,0,0],[0,0,1]])
axis, angle = ub.Utils.axis_angle(Q)

print(axis) #prints [0. 0. 1.]
print(angle) #prints 1.570 rad
```

Note that the axis is written in a generic reference frame $$\mathcal{F}_0$$. The axis is contextualized when we apply the rotation matrix to a point $$p$$ written in a specific reference.

## COMPOSITION OF ROTATION MATRIXES

Two rotations in a row represented by matrices $$Q_1$$ and $$Q_2$$ (in that order!) in a frame of reference $$\mathcal{F}_0$$ form another rotation in the reference frame $$\mathcal{F}_0$$, represented by a rotation matrix $$Q_3=Q_2Q_1$$ (the product of matrices).

*Note the order!* The second spin comes first on the product! More recent rotations come on the left!

Also note that the axes of rotation are always written in the reference frame $$\mathcal{F}_0$$, which is fixed along the rotations.

*Attention!* rotations do not commute, in general:

$$Q_2Q_1 \not= Q_1Q_2.$$

### Example 3

Consider the rotation matrix $$Q_1$$ and $$Q_2$$:

$$Q_1 = \large{\Bigg(}\normalsize{}\begin{array}{ccc}
                        1 & 0 & 0 \\
                        0 & 0 & -1 \\
                        0 & 1 & 0
                        \end{array}\large{\Bigg)}\normalsize{} \ \ , \ \ Q_2 =
                        \large{\Bigg(}\normalsize{}\begin{array}{ccc}
                        0 & 0 & 1 \\
                        0 & 1 & 0 \\
                        -1 & 0 & 0
                        \end{array}\large{\Bigg)}\normalsize{}.$$

The first matrix represents a 90 degree rotation of $$x$$, and the second 90 degrees of $$y$$.

so:

$$Q_1Q_2 = \large{\Bigg(}\normalsize{}\begin{array}{ccc}
                        0 & 0 & 1 \\
                        1 & 0 & 0 \\
                        0 & 1 & 0
                        \end{array} \large{\Bigg)}\normalsize{}\ \ , \ \ Q_2Q_1 =
                        \large{\Bigg(}\normalsize{}\begin{array}{ccc}
                        0 & 1 & 0 \\
                        0 & 0 & -1 \\
                        -1 & 0 & 0
                        \end{array} \large{\Bigg)}\normalsize{}.$$

The first matrix is a rotation on the axis $$r=( \frac{\sqrt{3}}{3} \ \frac{\sqrt{3}}{3} \
                        \frac{\sqrt{3}}{3} )^T$$ by an angle of 2.09 radians.

The second matrix is a rotation on the axis $$r=( \frac{\sqrt{3}}{3} \ \frac{\sqrt{3}}{3} \
                        -\frac{\sqrt{3}}{3} )^T$$ by an angle of 2.09 radians.

## ELEMENTARY ROTATIONS

$$R_x(\theta) = \Large{\Bigg(}\normalsize{}\begin{array}{ccc}
                        1 & 0 & 0 \\
                        0 & \cos(\theta) & -\sin(\theta) \\
                        0 & \sin(\theta) & \ \ \cos(\theta)
                        \end{array}\Large{\Bigg)}\normalsize{}.$$

$$R_y(\theta) = \Large{\Bigg(}\normalsize{}\begin{array}{ccc}
                        \ \cos(\theta) & 0 & \sin(\theta) \\
                        0 & 1 & 0 \\
                        -\sin(\theta) & 0 & \cos(\theta)
                        \end{array}\Large{\Bigg)}\normalsize{}.

$$R_z(\theta) = \Large{\Bigg(}\normalsize{}\begin{array}{ccc}
                        \cos(\theta) & -\sin(\theta) & 0 \\
                        \sin(\theta) & \ \ \cos(\theta) & 0 \\
                        0 & 0 & 1
                        \end{array}\Large{\Bigg)}\normalsize{}.$$


### Example 4

In UAIBot, elementary rotations are implemented by:

```python
import uaibot as ub

theta=3.14/2
Rx = ub.Utils.rotx(theta)
Ry = ub.Utils.roty(theta)
Rz = ub.Utils.rotz(theta)
```

In this case the matrices will be 4x4 instead of 3x3, but you can recover the rotation matrices by discarding the last row and the last column. Why these matrices are embedded in the 4x4 matrix will become clear shortly.

