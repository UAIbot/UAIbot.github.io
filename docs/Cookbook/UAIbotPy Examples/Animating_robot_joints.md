---
layout: home
title: Animating robot joints
parent: UAIbotPy Examples
grand_parent: Cookbook
---

# Animating robot joints

We can specify what the configuration is at an instant of time $$t$$ with `.add_ani_frame`. When this method is called, we change the current robot configuration (`robot.q`).

```python
import numpy as np
import uaibot as ub

robot = ub.Robot.create_kuka_kr5()
sim = ub.Simulation([robot])

#Let's make the first joint range from 0 to 2*pi, while the others continue at
# zero. The time will vary from 0.01 in 0.01 seconds, up to 10 seconds.
dt=0.01
tmax=10
for i in range(round(tmax/dt)):
    t = i*dt
    robot.add_ani_frame(time = t, q = [ (2*np.pi)*t/tmax, 0, 0, 0, 0, 0])

sim.run()
```