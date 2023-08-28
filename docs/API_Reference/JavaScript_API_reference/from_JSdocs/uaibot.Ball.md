---
layout: default
title: uaibot.Ball
parent: uaibot
grand_parent: JavaScript API reference
---

## Ball ⇐ [<code>Objsim</code>](#Objsim)
Class representing a sphere.

**Kind**: global class  
**Extends**: [<code>Objsim</code>](#Objsim)  

* [Ball](#Ball) ⇐ [<code>Objsim</code>](#Objsim)
    * [new Ball(_radius, _color)](#new_Ball_new)
    * [.setHTM(m)](#Objsim+setHTM)

<a name="new_Ball_new"></a>

### new Ball(_radius, _color)
Creates a sphere.


| Param | Type | Description |
| --- | --- | --- |
| _radius | <code>number</code> | radius of the sphere in meters. |
| _color | <code>\*</code> | color of the sphere in RGB/Hexadecimal/etc... |

<a name="Objsim+setHTM"></a>

### ball.setHTM(m)
Sets the homogeneous transformation matrix that represents the position of the object as the position of the object.

**Kind**: instance method of [<code>Ball</code>](#Ball)  
**Overrides**: [<code>setHTM</code>](#Objsim+setHTM)  

| Param | Type | Description |
| --- | --- | --- |
| m | <code>object</code> | 4x4 math.js homogeneous transformation matrix that represents the position of the object. |