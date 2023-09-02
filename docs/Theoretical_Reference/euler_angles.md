---
layout: default
title: Euler Angles
nav_order: 2
parent: Theoretical Reference
---

# Euler Angles

To understand this section a basic knowledge of linear algebra is required.

## Definition

In this context we have the following definition:

> Euler angles are a set of three angles that describe the orientation of a rigid body in a reference frame in the form of a sequence of three elemental rotations in form:
$$Q = R_z(\alpha)R_y(\beta)R_x(\gamma)$$

the angles $$\alpha$$, $$\beta$$ and $$\gamma$$ are called the Euler angles of rotation.

There are other Euler angle conventions (e.g. $$Q = R_x(\alpha)R_y(\beta)R_z(\gamma)$$), but this is the most common.

### Example 1

In UAIBot, Euler angles can be calculated using the Utils.euler_angles function in Python.

```python
import uaibot as ub
import numpy as np

Q = np.array([[0,0,1],[1,0,0],[0,1,0]])
alpha, beta, gamma = ub.Utils.euler_angles(Q)
print([alpha, beta, gamma])
```

### Demonstration 1

The following interactive demonstration shows the rotation of a box by the Euler angles $$\alpha$$, $$\beta$$ and $$\gamma$$. This demonstration is made using the UAIbotJS library. You can play around with the code by clicking the "Edit in JSFiddle" button.

<iframe width="100%" height="600px" src="//jsfiddle.net/UAIbot/tycnm73b/24/embedded/result/" allowfullscreen="allowfullscreen" allowpaymentrequest frameborder="0"></iframe>