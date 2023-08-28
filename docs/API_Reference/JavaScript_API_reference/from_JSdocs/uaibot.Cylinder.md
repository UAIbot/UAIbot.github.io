---
layout: default
title: uaibot.Cylinder
parent: uaibot
grand_parent: JavaScript API reference
---

## Cylinder ⇐ [<code>Objsim</code>](#Objsim)
Class representing a cylinder.

**Kind**: global class  
**Extends**: [<code>Objsim</code>](#Objsim)  

* [Cylinder](#Cylinder) ⇐ [<code>Objsim</code>](#Objsim)
    * [new Cylinder(_radius, _height, _color)](#new_Cylinder_new)
    * [.setHTM(m)](#Objsim+setHTM)

<a name="new_Cylinder_new"></a>

### new Cylinder(_radius, _height, _color)
Creates a cylinder.


| Param | Type | Description |
| --- | --- | --- |
| _radius | <code>number</code> | radius of the cylinder in meters. |
| _height | <code>number</code> | height of the cylinder in meters. |
| _color | <code>\*</code> | color of the cylinder in RGB/Hexadecimal/etc... |

<a name="Objsim+setHTM"></a>

### cylinder.setHTM(m)
Sets the homogeneous transformation matrix that represents the position of the object as the position of the object.

**Kind**: instance method of [<code>Cylinder</code>](#Cylinder)  
**Overrides**: [<code>setHTM</code>](#Objsim+setHTM)  

| Param | Type | Description |
| --- | --- | --- |
| m | <code>object</code> | 4x4 math.js homogeneous transformation matrix that represents the position of the object. |