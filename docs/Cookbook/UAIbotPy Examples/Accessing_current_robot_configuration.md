---
layout: home
title: Accessing current robot configuration
parent: UAIbotPy Examples
grand_parent: Cookbook
---

# Accessing current robot configuration

In UAIBot, we can access the current robot configuration as `robot.q`, where `robot` is the robot's variable name:

```python
import numpy as np
import uaibot as ub

robot = ub.Robot.create_kuka_kr5()
#Show current configuration
print(robot.q)
#Show initial (base) configuration
print(robot.q0)
```

Both are numpy arrays with shape(n,1) (n rows and 1 columns).