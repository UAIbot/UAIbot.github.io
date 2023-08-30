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

## Demonstration 1

To know the complete movement, we would need to know, at every instant of time $$t$$, the homogeneous transformation  matrix $$H(t)$$.

In the animation bellow, the matrix $$H(t)$$ is provided at all instants of time. This way, it is possible to continuously track the movement of the object.

<iframe frameBorder="0" scrolling="no" src="/assets/Homogenou.html" style="width:800px;height:650px;"></iframe>
