---
layout: default
title: UAIbotPy quickstart
parent: User Guide
nav_order: 1
---

# UAIbotPy quickstart

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1i3sxpV_DvVr_WH3vPFoN-ZPSP0ktpFlx?usp=sharing)

## Overview

The goal of this section is to give a brief introduction to UAIbotPy. UAIbotPy is a Python library for creating robotics simulations. It is a beginner-friendly web-based simulator for interactive robotics learning and research. This guide will walk you through the process of creating your first simulation.

This tutorial will cover how to use UAIbotPy inside an IDE. If you want to use UAIbotPy within Jupyter Notebook see [this](https://colab.research.google.com/drive/1i3sxpV_DvVr_WH3vPFoN-ZPSP0ktpFlx?usp=sharing) quickstart guide.

A basic understanding of Python is needed to follow this tutorial

## Creating a simulation

For this tutorial, we will create a simple simulation using an IDE. You can easily install UAIbot using pip.

```console
pip install uaibot
```

Let's start with the smallest possible simulation, just an empty scene.

```python
import uaibot as ub  # Import UAIbot as a Python package

sim = ub.Simulation()  # Instantiate simulation

sim.save("/your/folder/path", "example")  # Run the simulation

```
If you execute de Python code above you should see the simulation below after you open the "example.html" file at "/your/folder/path"

<iframe frameBorder="0" scrolling="no" src="/assets/Python_examples/creating_a_simulation.html" style="width:800px;height:650px;"></iframe>

Note that even with an empty scenario you can already click and drag the simulation to move in space or zoom with the scroll wheel.

Now let's take some time to analyze the code above. First, we import UAIbot as a Python package. Then, we instantiate the simulation using the `UAIbot.Simulation()` class. Finally, we run de simulation with the `UAIbot.Simulation.run()` method.

## Adding objects to the simulation

To add objects to the scene is very simple, you first instantiate them using their respective class and then add them to the simulation using the `Simulation.add()` method or passing them as arguments to the constructor of the `UAIbot.Simulation()` class, as seen in the example code below.

```python
import uaibot as ub #Import UAIbot as a Python package

cube_position = ub.Utils.trn([0.06, -0.525, 0.05]) #Create HTM for positioning the cube
cube = ub.Box(htm=cube_position, width=0.1, depth=0.1, height=0.1, color="red") #Instantiate cube

robot = ub.Robot.create_epson_t6(color="gray") #Instantiate robot

sim = ub.Simulation([cube, robot]) #Instantiate simulation

sim.save("/your/folder/path", "example")  # Run the simulation

```

If you execute de Python code above you should see the simulation below after you open the "example.html" file at "/your/folder/path"

<iframe frameBorder="0" scrolling="no" src="/assets/Python_examples/adding_objects_to_the_simulation.html" style="width:800px;height:650px;"></iframe>

As default, objects appear at the center of the scene. If you want to move them you need to use a homogenous transformation matrix (HTM). Homogenous transformation matrices (HTMs) are used to express the position and orientation of objects in UAIbot because of their ubiquity in robotics literature. Thankfully, there is a utility library that can be used to abstract HTMs and express the position of an object by its x, y, and z coordinates as seen in the use of the function `ub.Utils.trn()`.

## Moving simulation elements

Now, that we have created a scene and populated it with objects, we can move those objects and develop a true simulation. For this simulation, the robot is going to move toward the box, catch it, and move it to the opposite side. Let's assume that we know when the robot will be in the right pose at the right time. If you want more information about how to properly position robotic manipulators in specific poses the study of inverse kinematics techniques is encouraged. The code to perform the aforementioned task is shown below.

```python
import uaibot as ub #Import UAIbot as a Python package
import numpy as np

cube_position = ub.Utils.trn([0.12, -0.525, 0.05]) #Create HTM for positioning the cube
cube = ub.Box(htm=cube_position, width=0.1, depth=0.1, height=0.1, color="red") #Instantiate cube

robot = ub.Robot.create_epson_t6(color="gray") #Instantiate robot

sim = ub.Simulation([cube, robot]) #Instantiate simulation

for i in range(392):
  robot.add_ani_frame(time = i*0.02, q = [ np.cos(i/50), np.cos(i/50), 0.04*np.cos(i/25)+0.06])
  if i == 157:
    robot.attach_object(cube) #Catch cube

  if i == 314:
    robot.detach_object(cube) #Release cube

sim.save("/your/folder/path", "example")  # Run the simulation

```

If you execute de Python code above you should see the simulation below after you open the "example.html" file at "/your/folder/path"

<iframe frameBorder="0" scrolling="no" src="/assets/Python_examples/moving_simulation_elements.html" style="width:800px;height:650px;"></iframe>

If you gently hoover the cursor over the lower part of the simulation canvas a simplified media player interface will appear. Through this interface, you can play, pause, and replay the simulation as you wish.

That's all for this quickstart guide. If you want to learn more we suggest that you browse through the project's API documentation or take a look at the cookbook section. In case of any doubts or suggestions do not hesitate to open an issue on GitHub.