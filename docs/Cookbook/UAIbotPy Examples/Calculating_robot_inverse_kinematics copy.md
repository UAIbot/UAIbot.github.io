---
layout: home
title: Calculating robot inverse kinematics
parent: UAIbotPy Examples
grand_parent: Cookbook
---

# Calculating robot inverse kinematics

The inverse kinematics can be calculated with the `.ikm` method.

```python
import numpy as np
import uaibot as ub

robot = ub.Robot.create_kuka_kr5()
sim = ub.Simulation([robot])

#Let's create a target mth for the end-effector that is the same as the initial one, but offset
#bit down
target =  ub.Utils.trn([0,0,-0.3]) * robot.fkm()

#Let's find out which configuration gives this mth to the effector:
q_ikm = robot.ikm(htm_target = target)

#Let's make a smooth animation of the robot going from initial setup to
# the target configuration
dt=0.01
tmax = 10
for i in range(round(tmax/dt)):
    t = i*dt
    q_c = (1-t/tmax) * robot.q0 + (t/tmax) * q_ikm
    robot.add_ani_frame(time=t, q=q_c)

sim.run()
```