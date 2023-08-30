---
layout: default
title: Rigid Bodies
nav_order: 3
parent: Theoretical Reference
---

# Rigid Bodies

To understand this section a basic knowledge of linear algebra is required.

## Definition

From the point of view of Physics, a rigid body is an idealized object that cannot suffer deformations, contractions, expansions or breaks due to the forces that act on it.

It is obviously an approximation, and whether the object is a rigid body or not depends on the forces we are considering. For reasonable forces, we can say that a steel cylinder is a rigid body, while a beach ball is not.

From the point of view of Mathematics, rigid body is a set in which, for any two particles $$P_1$$ and $$P_2$$, the distance between them remains constant throughout the movement.

that is, if $$p_1(t)$$ and $$p_2(t)$$ are the positions of two particles $$P_1$$ and $$P_2$$ over time, written with respect to a reference $$R$$, so for all time $$t$$ we have:

$$\|p_1(t_A)-p_2(t_A)\| = \|p_1(t_B)-p_2(t_B)\|$$

In which $$\| \cdot \|$$ is the Euclidean norm of the vector.

## Describing the movement of a rigid body

We now want to make a mathematical description of the motion of a rigid body. Therefore, it is understood to describe the trajectory of all the particles that form a rigid body. 

Note that this would be extremely difficult for a generic object like a beach ball. After all, the beach ball can translate, rotate, contract, distort, etc... in infinite, extremely complex ways. 

Fortunately, for a rigid body, particle motion is severely limited, which allows for a concise description of motion.

Before understanding how we can do this, we need to understand what a *rigid transformation* is.

## Rigid transformation

>A rigid transformation is a function $$T: \mathbb{R}^3 \mapsto \mathbb{R}^3$$ with the following property: for any two points $$p_1$$ and $$p_2$$:
1. $$\|T(p_1)-T(p_2)\|=\|p_1-p_2\|.$$

In other words, a rigid transformation preserves the distance between points.

There is a teorem that states:

>For every rigid transformation $$T$$, there is a rotation matrix $$Q$$ and a vector $$s$$ such that $$T(p) = \pm(Qp+s)$$, in which $$\pm$$ represents an arbitrary sign change in each element of the vector $$p'=Qp+s$$.

The interpretation of this theorem is that every rigid transformation is composed of three sub-operations:
- A *rotation* by a matrix $$Q$$...
- ...followed by a *translation* by a vector $$s$$...
- ...followed by a *reflection* around the main axes.

Note that, in all this, there is an implicit reference frame $$F_0$$.

We will work, for now, with proper rigid transformations, without reflection:

$$T(p) = Qp+s$$

that is, a *rotation* and a *translation*.

## Describing the movement of a rigid body with rigid transformations

Obviously, there is a connection between *motion of rigid bodies* and *rigid transformations*.

If $$\mathcal{P}(t_A), \mathcal{P}(t_B) \subseteq \mathbb{R}^3$$ are sets that represent the positions of the particles of the same rigid body $$P$$ at two different times, $$t = t_A$$ and $$t = t_B$$. Then there is a unique rigid transformation $$T_{AB}$$ such that every point of $$\mathcal{P}(t_B)$$ can be obtained from a point of $$\mathcal{P}(t_A)$$ through the application of $$T_{AB}$$.

In other words, the set at a time $$t_B$$ can be obtained from the set at a time $$t_A$$ by applying to all points of a rigid transformation $$T_{AB}$$.

This observation, that the set at different times is related to a single rigid transformation that depends on the two times, allows us to make a very important observation:

>We can describe the motion of a rigid body by giving, at any instant in time, the rigid transformation $$T_t$$ that relates the sets in times 0 and $$t$$.

In fact: if we know how the object is doing in time $$t=0$$ and the transformation $$T_t$$ (where a referencial $$\mathcal{F}_0$$ is implied), we are able to unambiguously describe the movement of all the particles that make up the body over time $$t$$, and therefore of the body as a whole.

A rigid transformation $$T(p) = Qp+s$$ is specified by a rotation matrix $$Q \in \mathbb{R}^{3 \times 3}$$ and a vector $$s \in \mathbb{R}^3$$. So, to specify $$T_t(p)$$ we need to specify the matrix $$Q(t)$$ and the displacement vector $$s(t)$$ at all times. We can provide both of these pieces of information using just one matrix, the *Homogeneous Transformation Matrix*. For more information, see the Homogeneous Transformation Matrix section.

