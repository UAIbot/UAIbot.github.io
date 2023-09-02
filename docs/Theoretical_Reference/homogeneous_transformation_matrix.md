---
layout: default
title: Homogeneous Transformation Matrix
nav_order: 4
parent: Theoretical Reference
---

# Homogeneous Transformation Matrix

To understand this section a basic knowledge of linear algebra is required.

## Definition

We can define a homogeneous transformation matrix as follows:

> A homogeneous transformation matrix (HTM) is a matrix assembled as follows:
>
> $$H = \left(\begin{array}{cc} Q & s \\ 0_{1 \times 3} & 1 \end{array}\right)$$
>
> where $$Q$$ is a $$3 \times 3$$ rotation matrix, $$s$$ is a $$3 \times 1$$ translation vector, and $$0_{1 \times 3}$$ is a $$1 \times 3$$ zero vector.

A homogeneous transformation matrix represents a rigid transformation. We can describe the motion of a rigid body by giving, at any instant in time, the rigid transformation $$T_t$$ that relates the position of a group of particles in times 0 and $$t$$. Therefore, we can describe the motion of a rigid body by giving, at any instant in time, the homogeneous transformation matrix $$H_t$$ that relates the position of a group of particles in times 0 and $$t$$.

### Demonstration 1

To know the complete movement, we would need to know, at every instant of time $$t$$, the homogeneous transformation  matrix $$H(t)$$.

In the animation bellow, the matrix $$H(t)$$ is provided at all instants of time. This way, it is possible to continuously track the movement of the object.

<iframe frameBorder="0" scrolling="no" src="/assets/Homogenou.html" style="width:800px;height:550px;"></iframe>


## Basic Homogeneous Transformation Matrices

We have 4 basic HTMs, representing rotations in $$x$$, $$y$$ and $$z$$ and a translation of a vector $$s \in \mathbb{R}^{3 \times 1}$$.

$$\tilde{R}_x(\theta) = \left(\begin{array}{cc} R_x(\theta) & 0_{3 \times 1} \\ 0_{1 \times 3} &
                        1 \end{array}\right) \ , \
                        \tilde{R}_y(\theta) = \left(\begin{array}{cc} R_y(\theta) & 0_{3 \times 1} \\ 0_{1 \times 3} & 1
                        \end{array}\right), $$

$$\tilde{R}_z(\theta) = \left(\begin{array}{cc} R_z(\theta) & 0_{3 \times 1} \\ 0_{1 \times 3} &
                        1 \end{array}\right) \ , \
                        \tilde{D}(s) = \left(\begin{array}{cc} I_{3 \times 3} & s \\ 0_{1 \times 3} & 1
                        \end{array}\right). $$

In which $$R_x(\theta), R_y(\theta)$$, and  $$R_z(\theta)$$ are 3x3 rotation matrices.

### Example 1

In UAIBot, these four matrices are implemented with functions Utils.rotx, Utils.roty, Utils.rotz, Utils.trn

```python
import numpy as np
import uaibot as ub

theta=3.14/2
s = [1,2,3]

Rx = ub.Utils.rotx(theta)
Ry = ub.Utils.roty(theta)
Rz = ub.Utils.rotz(theta)
D = ub.Utils.trn(s)
```

In Python, and:

```javascript
import * as Utils from "https://cdn.jsdelivr.net/gh/UAIbot/UAIbotJS@main/UAIbotJS/Utils.js";

let theta = 3.14/2;
let s = math.matrix([
  [1],
  [2],
  [3]
]);

let Rx = Utils.rotx(theta);
let Ry = Utils.roty(theta);
let Rz = Utils.rotz(theta);
let D = Utils.trn(s);
```

In JavaScript.

## Homogeneous Transformation Matrix composition

HTMs have several uses when representing rigid transformations. For example, the composition of rigid transforms is also a rigid transformation. If $$T_1(p) = Q_1p+s_1$$ and $$T_2(p) = Q_2p+s_2$$ are two rigid transformations, then:

$$T_2(T_1(p)) = (Q_2Q_1)p + (Q_2s_1+s_2).$$

Note that, as with rotations, transformations do not necessarily commute: $$(T_2T_1 \not= T_1T_2)$$.

Let the respective MTH of the transformations be $$T_1$$ and $$T_2$$, and the MTH of the composition be $$T_3$$ ($$T_3 = T_2T_1$$). Then:

$$H_1 = \left(\begin{array}{cc} Q_1 & s_1 \\ 0_{1 \times 3} & 1 \end{array}\right) \ , \ H_2 =
                        \left(\begin{array}{cc} Q_2 & s_2 \\ 0_{1 \times 3} & 1 \end{array}\right),$$

$$H_3 = \left(\begin{array}{cc} Q_2Q_1 & Q_2s_1+s_2 \\ 0_{1 \times 3} & 1
                        \end{array}\right).$$

It's not hard to see that $$H_3 = H_2H_1$$, that is, if we represent rigid transformations by MTH, the composition of two transformations is the matrix product (in the correct order) of the respective MTHs!

From now on, we will use the symbols $$R_x(\theta), R_y(\theta), R_z(\theta), D_x(d),
                        D_y(d), D_z(d)$$ to represent the MTHs of the respective transformations in $$\theta, d \in
                        \mathbb{R}$$

Consider a referential $$\mathcal{F}_0$$. We apply the transformations represented by the MTHs $$H_1, H_2, H_3$$ and $$H_4$$, in that order.

We will then have a final HTM $$H_{F} = H_4 H_3 H_2 H_1$$, where the most recent transformations multiply from the left.

Note that all transformations are interpreted in the same referential $$\mathcal{F}_0$$. So if $$H_2$$ is a shift in the $$z$$ axis of 5 units, we will apply a displacement of 5 units in the $$z_0$$ axis.

### Demonstration 2

Consider the following sequence of transformations:

$$H = R_x(\pi/4) D_y(-0.25) R_z(\pi/2) D_x(1).$$

Note the order ($$D_x(1)$$ first, $$R_z(\pi/2)$$ later, etc...). We read from right to left!

See the demonstration bellow with the sequence of transformations. Note that all transformations are done with respect to the reference frame $$\mathcal{F}_0$$.

<iframe frameBorder="0" scrolling="no" src="/assets/anim2.html" style="width:800px;height:550px;"></iframe>


**There is another way to interpret the same transformation!**

We will arrive at the same final frame of reference $$H$$ if we read from left to right, but considering that the transformations are interpreted in the current reference frame instead of the original reference frame $$\mathcal{F}_0$$!

See the demonstration bellow with the sequence of transformations. Note that the final reference is the same! Only the intermediate frames change.

<iframe frameBorder="0" scrolling="no" src="/assets/Homogenou3.html" style="width:800px;height:550px;"></iframe>

Thus, when making a composition of transformations, we can multiply the matrix left or right:

- On the left: we make the transformation using the initial reference frame ($$\mathcal{F}_0$$).
- On the right: we do the transformation using the current reference frame.

Both applications are useful. In robotics, however, it is more common to apply to the right (in the current reference frame).

