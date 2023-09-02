---
layout: home
title: Calculating robot foward kinematics
parent: UAIbotPy Examples
grand_parent: Cookbook
---

# Calculating robot foward kinematics

The forward kinematics can be calculated with the `.fkm` method. All HTMs are calculated with respect to the scenario reference frame.

```python
import numpy as np
import uaibot as ub

#only configures how the matrices will be displayed
np.set_printoptions(precision=4, suppress=True)

robot = ub.Robot.create_kuka_kr5()

#With no parameters, calculates for the current configuration (robot.q) and the effector
print(robot.fkm())

#We can specify the configuration
print(robot.fkm(q=[0,1,2,3,4,5]))

#We can choose if we want to calculate the MTH for the effector (default) or if
# for DH references. In the latter case, we have a list with n matrices
# (for the first frame, FDH0, is not calculated, as it is fixed)

#Calculate for the effector
print(robot.fkm(q=robot.q, axis='eef'))
#Calculates for DH references
htm_dh = robot.fkm(q=[0,1,2,3,4,5], axis='dh')
for i in range(len(htm_dh)):
    print(htm_dh[i])
```