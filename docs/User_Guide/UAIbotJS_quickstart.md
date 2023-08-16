---
layout: default
title: UAIbotJS quickstart
nav_order: 1
parent: User Guide
---

# UAIbotJS quickstart
## Overview
The goal of this section is to give a brief introduction to UAIbotJS. UAIbotJS is a JavaScript library for creating robotic simulations in the browser. This guide will walk you through the process of creating your first simulation.

UaibotJS is a version of the UAIbot simulator entirely written in JavaScript. If you want to look at the Python version of UAIbot see UAIbotPy.

A basic understanding of HTML, CSS, and JavaScript is needed to follow this tutorial.


## Creating a simulation

For this tutorial, we will create a simple simulation inside an HTML file. Let`s start with the smallest possible simulation, just an empty scene.

```html
<!DOCTYPE html>
<html>
  <body>

    <!--The canvas element below is where the simulation will be displayed-->
    <canvas id="scene" style='width:100%; height:100%; position:absolute'></canvas>

    <script type="module"> 
      import * as UAIbot from "https://cdn.jsdelivr.net/gh/UAIbot/UAIbotJS@v1.0.1/UAIbotJS/UAIbot.js";

      let sim = new UAIbot.Simulation();

      sim.setAnimationLoop(() => {
        sim.render();
      });
      
    </script>
  </body>
</html>
```

Now let`s take some time to analyze the code inside the script tag. First, we import UAIbot as an ES6 module through a CDN. Then we instantiate the simulation using the UAIbot.Simulation() class. Finally, we set the animation loop. The animation loop is responsible for continuously rendering the simulation frames. It makes the scene able to change with time according to preprogrammed animations or user interaction. If you put the presented code in an HTML file and open it with a browser you would see the scene below.

<iframe frameBorder="0" scrolling="no" src="/assets/creating_a_simulation.html" style="width:100%;height:300px;"></iframe>

Note that even with an empty scenario you can already click and drag the simulation to move in space or zoom with the scroll wheel.

## Adding objects to the simulation
To add objects to the scene is very simple, you first instantiate them using their respective class and then add them to the simulation using the Simulation.add() method, as seen in the example code below.

```html
<!DOCTYPE html>
<html>
  <body>

    <!--The canvas element below is where the simulation will be displayed-->
    <canvas id="scene" style='width:100%; height:100%; position:absolute'></canvas>

    <script type="module"> 
      import * as UAIbot from "https://cdn.jsdelivr.net/gh/UAIbot/UAIbotJS@v1.0.1/UAIbotJS/UAIbot.js";
      import * as Utils from "https://cdn.jsdelivr.net/gh/UAIbot/UAIbotJS@main/UAIbotJS/Utils.js";
      import * as math from 'https://cdn.jsdelivr.net/npm/mathjs@11.6.0/+esm';

      let sim = new UAIbot.Simulation(); //instantiate simulation
      let bot = new UAIbot.Robot().create_epson_t6(); //instantiate robot
      let box = new UAIbot.Box(0.1, 0.1, 0.1, "red"); //instantiate cube

      sim.add(box);//Add box
      sim.add(bot);//Add cube
      
      let position_vector = math.matrix([[0.05],
                                         [-0.525],
                                         [0.05]]);//Create position vector for positioning the cube
      let box_position = Utils.trn(position_vector); //Create HTM for positioning the cube
      box.setHTM(box_position)//Change cube position

      sim.setAnimationLoop(() => {
        sim.render();
      });
      
    </script>
  </body>
</html>
```

As default, objects appear at the center of the scene. If you want to move them you need to use a homogenous transformation matrix (HTM). Homogenous transformation matrices (HTMs) are used to express the position and orientation of objects in UAIbot because of their ubiquity in robotics literature. Thankfully, there is a utility library that can be used to abstract HTMs and express the position of an object by its x, y, and z coordinates. In the example above, the utility library and the Math.js library are imported through CDNs. Then, a position vector is declared and passed to the Utils.trn() method in order to be converted into a HTM. Finally, The created HTM is passed to the Box object with the Box.setHTM() method. If you put the code above in an HTML file and open it with a browser you would see the scene below.

<iframe frameBorder="0" scrolling="no" src="/assets/adding_objects_to_the_scene.html" style="width:100%;height:300px;"></iframe>

If you don't see the red box, don't worry. It is right behind the robot, just click and drag the scenario to see it.

## Moving simulation elements

Now, that we have created a scene and populated it with objects, we can move those objects and develop a true simulation. For this simulation, the robot is going to move toward the box, catch it, and move it to the opposite side. Let`s assume that we know when the robot will be in the right pose at the right time. If you want more information about how to properly position robotic manipulators in specific poses the study of inverse kinematics techniques is encouraged. The code to perform the aforementioned task is shown below.

```html
<!DOCTYPE html>
<html>
  <body>

    <!--The canvas element below is where the simulation will be displayed-->
    <canvas id="scene" style='width:100%; height:100%; position:absolute'></canvas>

    <script type="module"> 
      import * as UAIbot from "https://cdn.jsdelivr.net/gh/UAIbot/UAIbotJS@v1.0.1/UAIbotJS/UAIbot.js";
      import * as Utils from "https://cdn.jsdelivr.net/gh/UAIbot/UAIbotJS@main/UAIbotJS/Utils.js";
      import * as math from 'https://cdn.jsdelivr.net/npm/mathjs@11.6.0/+esm';

      let sim = new UAIbot.Simulation(); //instantiate simulation
      let bot = new UAIbot.Robot().create_epson_t6(); //instantiate robot
      let box = new UAIbot.Box(0.1, 0.1, 0.1, "red"); //instantiate cube

      sim.add(box);//Add box
      sim.add(bot);//Add cube
      
      let position_vector = math.matrix([[0.05],
                                         [-0.525],
                                         [0.05]]);//Create position vector for positioning the cube
      let box_position = Utils.trn(position_vector); //Create HTM for positioning the cube
      box.setHTM(box_position)//Change cube position

      let i = 0;//Variable for registering frame number
      sim.setAnimationLoop(() => {

        if(i < 392){
          let q = math.matrix([[math.cos(i/50)],
                               [math.cos(i/50)],
                               [-0.04*math.cos(i/25) - 0.05]]);//Create configuration vector
          if(i == 157){
            bot.catch(box);//Catch box
          }
          if(i == 314){
            bot.release(box);//Realease box
          }
          bot.config(q);//Put robot in specified configuration
        }
        i++;//Go to next frame

        sim.render();
      });
      
    </script>
  </body>
</html>
```

The first noteworthy thing is that now we created a new variable `i` in order to have some reference of which frame we are on. Based on this variable `i` we can calculate all the poses of all objects one frame after the other. The first calculation made is of a configuration vector for the robot. Configuration vectors are column vectors used to express the position of each robot link at a certain pose. The robot receives this vector through the Robot.config() method. 

As previously stated, we know that the robot will be in the right pose to catch the box at frame number 157. So, in frame 157 the box is caught with the method Robot.catch(). After this method is called the pose of the box is updated in relation to the robot end effector in a way that gives the visual impression that the robot is holding the box. An analogous thing happens at frame 314, but at this time the robot releases the box. If you put the code above in an HTML file and open it with a browser you would see the scene below.

<iframe frameBorder="0" scrolling="no" src="/assets/moving_scene_elements.html" style="width:100%;height:300px;"></iframe>

If the animation above is over, reload the page and everything will start all over again.

That’s all for this quickstart guide. If you want to learn more we suggest that you browse through the project’s API documentation or take a look at the cookbook section. In case of any doubts or suggestions do not hesitate to open an issue on GitHub.