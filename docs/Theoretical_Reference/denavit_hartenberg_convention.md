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

## The the D–H referentials

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

There are 4 parameters to transform from the frame $$\mathcal{F}_{DH(i-1)}$$ to the next frame $$\mathcal{F}_{DHi}$$. This is for $$i=1,...,n$$, totaling $$4n$$ parameters.

The parameters are:

- $$\theta_i$$: the rotation that must be done on the current $$z$$ axis to align the current $$x$$ axis with the next $$x$$ axis.
- $$d_i$$: the displacement to be made on the current $$z$$ axis so that the center of the current frame goes to point $$i,i+1$$.
- $$\alpha_i$$: the rotation that must be done on the current $$x$$ axis to align the current $$x$$ axis with the next $$x$$ axis.
- $$a_i$$: the translation that must be done on the current $$x$$ axis so that the two reference frames finally coincide.

The way in which the DH axes are created guarantees the existence of these parameters, that is, that there are numbers $$\theta_i,d_i,\alpha_i,a_i$$ in which these transformations parameterized by them transform one referential into the next.

**Very important**: if the $$i$$-th joint is revolute, $$\theta_i$$ is variable and depends on the current **configuration** of joint $$i$$,$$q_i$$. If it is linear, it is $$d_i$$ which is variable, and depends on the current **configuration** of joint $$i$$,$$q_i$$.

All three remaining parameters from one reference frame to the other are structural constants of the robot, decided at the time of its design. Note that transformations always use the current frame of reference, not the starting frame.

### Demonstration 4

In the animation bellow, the four D–H parameters are deduced for each link of a robot manipulator.

<iframe frameBorder="0" scrolling="no" src="/assets/dh4.html" style="width:800px;height:650px;"></iframe>

### Demonstration 5

In the animation bellow, the four D–H parameters are deduced for each link of a robot manipulator.

<iframe frameBorder="0" scrolling="no" src="/assets/dh5.html" style="width:800px;height:650px;"></iframe>

Note that in the two previous examples, the robot was the same, but in different configurations. The structural parameters (in white) were the same, but the variables (in yellow) changed. 

### Demonstration 6

In the animation bellow, the four D–H parameters are deduced for each link of a robot manipulator.

<iframe frameBorder="0" scrolling="no" src="/assets/dh6.html" style="width:800px;height:650px;"></iframe>

## Solving the forward kinematics problem with the D–H convention

In possession of the parameters, it is easy to calculate the transformation of the reference frame $$\mathcal{F}_{DH(i-1)}$$ to $$\mathcal{F}_{DHi}$$, for $$i=1,2,...,n$$.

The transformation goes as follows:

$$H_{DH(i-1)}^{DHi}(q_i) = R_z(\theta_i)D_z(d_i)R_x(\alpha_i)D_x(a_i).$$

Note that the transformation must be read from left to right, as we use the current reference frame, not the initial one, to interpret the transformations! So first is the $$z$$ rotation, then the $$z$$ displacement, then the $$x$$ rotation, and finally the $$x$$ displacement.

The HTM $$H_{DH0}^{DHn}(q)$$ between the first reference frame (fixed) and the one that is attached to the last link (effector) is:

$$H_{DH0}^{DHn}(q) = H_{DH0}^{DH1}(q_1)H_{DH1}^{DH2}(q_2)...H_{DH(n-1)}^{DHn}(q_n).$$

Depended on the **configuration** $$q$$ of the robot.
