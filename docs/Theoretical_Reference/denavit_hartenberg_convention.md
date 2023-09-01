---
layout: default
title: Denavit–Hartenberg convention
nav_order: 5
parent: Theoretical Reference
---

# Denavit–Hartenberg (D-H) convention

To understand this section a basic knowledge of linear algebra is required.

The Denavit–Hartenberg convention is a powerfull tool to describe the kinematics of a robotic manipulator. But first, let's define some important concepts.

## Foward Kinematics and Configuration

The first important consept in this section is **forward kinematics**. 

Definition:

>The forward kinematics problem is to find the position and orientation of the end-effector, given the joint angles and link lengths of the robot arm. In other words, given the joint angles $$\theta$$, we want to find the homogeneous transformation matrix $$H$$ that relates the position of the end-effector to the position of the base of the robot, or som other reference frame.

In the study of robot kinematics another definition is very important: **configuration**.

Definition:

>The configuration of a robotic manipulator is the set of all joint angles $$\theta$$. The configuration space is the set of all possible configurations. The configuration space of a robot with $$n$$ joints is $$\mathbb{R}^n$$.

## Solving the forward kinematics problem with the D–H convention

The D–H convention is a systematic procedure for assigning coordinate frames to the links of a robot manipulator. The rocedure goes as follows:

Do the following for each link of the robot (in which the links are numbered as $$i=0,1,2,...,n$$):

- Identify line $$i$$, which is the infinite line aligned with joint $$i$$;
- Identify line $$i+1$$, which is the infinite line aligned with joint $$i+1$$;
- Identify point $$i,i+1$$, which is the point on line $$i$$ closest to line $$i+1$$;
- Identify point $$i+1,i$$, which is the point on line $$i+1$$ closest to line $$i$$;
- The center of $$\mathcal{F}_{DHi}$$ is the point point $$i+1,i$$;
- The axis $$z_{DHi}$$ is chosen to be in one of the two directions on line $$i+1$$;
- the axis $$x_{DHi}$$ is chosen as the vector that goes from point $$i,i+1$$ to point $$i+1,i$$, after normalization;
- Complete the referential $$\mathcal{F}_{DHi}$$ with the axis $$y_{DHi}$$, which is chosen by the right-hand rule.

The referential $$\mathcal{F}_{DHi}$$ is stuck on the i-th link, and link 0 is the base of the robot.

There are some cases where the rule is ill-defined, and the engineer is free to choose:

- For $$i=0$$, there is no joit $$0$$. So, for $$i=0$$ we simply choose the center  on line 1, and the axis $$x_{DH0}$$ arbitrarily, as long as it is orthogonal to the axis $$z_{DH0}$$.
- If the lines line $$i$$ and line $$i+1$$ are parallel, there are infinitely many possible choices for the pair of points point $$i,i+1$$ and point $$i+1,i$$. Choose one of these pairs arbitrarily.
- If point $$i,i+1$$ = point $$i+1,i$$, the rule for choosing $$x_{DHi}$$ is poorly defined. Pick any one of the two vectors that are mutually orthogonal to the lines line $$i$$ and line $$i+1$$.
- If $$i=n$$, there is no joint $$n+1$$. In this case, we choose the straight line $$n+1$$ arbitrarily. We usually use the previous line, Line $$n$$.

### Demonstration 1

In the animation bellow, the D–H convention is used to assign coordinate frames to the links of a robot manipulator.

<iframe frameBorder="0" scrolling="no" src="/assets/dh1.html" style="width:800px;height:650px;"></iframe>

### Demonstration 2

In the animation bellow, the D–H convention is used to assign coordinate frames to the links of a robot manipulator.

<iframe frameBorder="0" scrolling="no" src="/assets/dh2.html" style="width:800px;height:650px;"></iframe>

### Demonstration 3

In the animation bellow, the D–H convention is used to assign coordinate frames to the links of a robot manipulator.

<iframe frameBorder="0" scrolling="no" src="/assets/dh3.html" style="width:800px;height:650px;"></iframe>

## The D–H parameters

After sticking $$n+1$$ referentials in the robot (one of them in the fixed base), there is a systematic way to calculate the HTM $$H_{DH0}^{DHn}(q)$$, which is the last DH frame ($$i=n$$) written in the first DH reference frame ($$i=0$$).

Given the two interpretations for an HTM, we can also interpret $$H_{DH0}^{DHn}(q)$$ like the rigid transformation we have to make from the first frame of reference to the last one.

Anyway, for that we have to extract the Denavit-Hartenberg Parameters from the robot, which are $$4n$$ numbers that allow us to know how each of the references is at a given instant of time.

aula 3 slide 31