---
layout: default
title: uaibot.Box
parent: uaibot
grand_parent: JavaScript API reference
---

## Box ⇐ [<code>Objsim</code>](#Objsim)
Class representing a cuboid

**Kind**: global class  
**Extends**: [<code>Objsim</code>](#Objsim)  

* [Box](#Box) ⇐ [<code>Objsim</code>](#Objsim)
    * [new Box(_width, _height, _depth, _color)](#new_Box_new)
    * [.setHTM(m)](#Objsim+setHTM)

<a name="new_Box_new"></a>

### new Box(_width, _height, _depth, _color)
Creates a cuboid.


| Param | Type | Description |
| --- | --- | --- |
| _width | <code>number</code> | width of the cuboid in meters. |
| _height | <code>number</code> | height of the cuboid in meters. |
| _depth | <code>number</code> | depth of the cuboid in meters. |
| _color | <code>\*</code> | color of the cuboid in RGB/Hexadecimal/etc... |

<a name="Objsim+setHTM"></a>

### box.setHTM(m)
Sets the homogeneous transformation matrix that represents the position of the object as the position of the object.

**Kind**: instance method of [<code>Box</code>](#Box)  
**Overrides**: [<code>setHTM</code>](#Objsim+setHTM)  

| Param | Type | Description |
| --- | --- | --- |
| m | <code>object</code> | 4x4 math.js homogeneous transformation matrix that represents the position of the object. |