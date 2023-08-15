---
layout: default
title: UAIbotJS quickstart
nav_order: 1
parent: User Guide
---

# UAIbotJS quickstart
## Overview
The goal of this section is to give a brief introduction to UAIbotJS. UAIbotJS is a JavaScript library for creating robotic simulations in the browser. This guide will walk you through the process of creating your first simulation. 

UaibotJS is a version of the UAIbot simulator entirelly written in JavaScript. If you want to take a look at the Python version of UAIbot see UAIbotPy.

To follow this tutorial a basic understnding of HTML, CSS and JavaScript is needed.

## Creating a simulation
For this tutorial we will create a simple simulation inside an HTML file. Let`s start with the smallest possible simulation, just an empty scene.

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

Now let`s take some time to analyse the code inside the script tag. First we import UAIbot as an ES6 module through a CDN. Then we instantiate the simulation using the UAIbot.Simulation() class. Finally, we set the animation loop. The animation loop is responsible for continuously rendering the simulation frames. It makes the scene able to change with time acording to preprogramed animations or user interaction. If you put the presented code in and HTML file and open it with a browser you would see the scene below.

<iframe frameBorder="0" scrolling="no" src="/assets/creating_a_simulation.html" style="width:100%;height:300px;"></iframe>

Note that even with an empty cenario you can already click and drag the simulation to move in space or zoom with the scroll wheel.

## Adding objects to the scene
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
      import * as math from 'https://cdn.jsdelivr.net/npm/mathjs@11.6.0/+esm'

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

As default, objects apear at the center of the scene. If you want to move them you need to use homogenous transformation matrices. 