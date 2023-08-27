--- 
layout: default
title: uaibot.demo.demo
parent: uaibot.demo
grand_parent: Python API reference
--- 

# uaibot.demo.demo module

<a id="module-uaibot.demo.demo"></a>

### *class* uaibot.demo.demo.Demo

Bases: `object`

A class that contains demonstrations in robotics.

#### *static* control_demo_1()

Show a robotic manipulator drawing a circle in a drawboard.
The task demands that the manipulator keep a constant pose while
drawing.

#### *static* control_demo_2()

Show two robotic manipulators cooperating to transport an object between
two plates. Note that the relative pose between the two end-effectors must
be kept.

The control uses task priority framework using the null space of the task
Jacobian. The task of keeping the relative pose is prioritized over the
task of moving the plate.

#### *static* control_demo_3()

Show a robot manipulator that must achieve a pose inside a hole. Collision must be avoided.

Perform second order kinematic control with constraints that enforce
collision avoidance.

#### *static* lesson_demo_3(robot_creator=None, width=800, height=600)

Show a robot manipulator that must achieve a pose inside a hole. Collision must be avoided.

Perform second order kinematic control with constraints that enforce
collision avoidance.
