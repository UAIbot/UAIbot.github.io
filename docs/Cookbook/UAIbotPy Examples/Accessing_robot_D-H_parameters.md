---
layout: home
title: Accessing robot's D-H parameters
parent: UAIbotPy Examples
grand_parent: Cookbook
---

# Accessing robot's D-H parameters

In UAIBot we can access the robot's DH parameters as:

```python
import numpy as np
import uaibot as ub

robot = ub.Robot.create_kuka_kr5()

#Joints go from i=0 to i=n-1
for i in range(len(robot.links)):
    #Type: 0 (revolute), 1 (prismatic)
    print("Type"+str(i+1)+": "+str(robot.links[i].joint_type))
    print("theta"+str(i+1)+": "+str(robot.links[i].theta)+" rad")
    print("d"+str(i+1)+": "+str(robot.links[i].d)+" m")
    print("alpha"+str(i+1)+": "+str(robot.links[i].alpha)+" rad")
    print("a"+str(i+1)+": "+str(robot.links[i].a)+" m")
    print("\n")
```