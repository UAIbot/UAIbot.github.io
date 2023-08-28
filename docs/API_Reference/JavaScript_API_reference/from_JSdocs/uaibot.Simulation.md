---
layout: default
title: uaibot.Simulation
parent: uaibot
grand_parent: JavaScript API reference
---

## Simulation
Represents a new simulation environment.

**Kind**: global class  

* [Simulation](#Simulation)
    * [new Simulation()](#new_Simulation_new)
    * [.render()](#Simulation+render)
    * [.setAnimationLoop(loop_code)](#Simulation+setAnimationLoop)
    * [.fitWindow()](#Simulation+fitWindow)
    * [.add(object_sim)](#Simulation+add)

<a name="new_Simulation_new"></a>

### new Simulation()
Creates a new simulation environment.

<a name="Simulation+render"></a>

### simulation.render()
Renders each frame.

**Kind**: instance method of [<code>Simulation</code>](#Simulation)  
<a name="Simulation+setAnimationLoop"></a>

### simulation.setAnimationLoop(loop_code)
Creates the animation loop.

**Kind**: instance method of [<code>Simulation</code>](#Simulation)  

| Param | Type | Description |
| --- | --- | --- |
| loop_code | <code>undefined</code> | code to be excecuted every loop. |

<a name="Simulation+fitWindow"></a>

### simulation.fitWindow()
Makes scene fit browser window.

**Kind**: instance method of [<code>Simulation</code>](#Simulation)  
<a name="Simulation+add"></a>

### simulation.add(object_sim)
Adds object to the scene.

**Kind**: instance method of [<code>Simulation</code>](#Simulation)  

| Param | Type | Description |
| --- | --- | --- |
| object_sim | <code>object</code> | Object to be added. |