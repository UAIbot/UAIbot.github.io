---
layout: default
title: uaibot.Robot
parent: uaibot
grand_parent: JavaScript API reference
---

## Robot
Class representing a generic open chain robotic manipulator.

**Kind**: global class  

* [Robot](#Robot)
    * [new Robot(_linkInfo)](#new_Robot_new)
    * [.config(c)](#Robot+config)
    * [.catch(object)](#Robot+catch)
    * [.release(object)](#Robot+release)
    * [.fkm(n, q)](#Robot+fkm) ⇒
    * [._jac_geo(axis)](#Robot+_jac_geo) ⇒
    * [.create_kuka_kr5()](#Robot+create_kuka_kr5) ⇒
    * [.create_epson_t6()](#Robot+create_epson_t6) ⇒

<a name="new_Robot_new"></a>

### new Robot(_linkInfo)
Creates a generic open chain robotic manipulator.


| Param | Type | Description |
| --- | --- | --- |
| _linkInfo | <code>object</code> | 5xN matrix representing the DH parameters that describe the robot. |

<a name="Robot+config"></a>

### robot.config(c)
Sets robot configuration.

**Kind**: instance method of [<code>Robot</code>](#Robot)  

| Param | Type | Description |
| --- | --- | --- |
| c | <code>object</code> | math.js column matrix representing the robot configuration. |

<a name="Robot+catch"></a>

### robot.catch(object)
Makes robot catch a scene object.

**Kind**: instance method of [<code>Robot</code>](#Robot)  

| Param | Type | Description |
| --- | --- | --- |
| object | <code>object</code> | Scene object to be catched. |

<a name="Robot+release"></a>

### robot.release(object)
Makes robot release a scene object.

**Kind**: instance method of [<code>Robot</code>](#Robot)  

| Param | Type | Description |
| --- | --- | --- |
| object | <code>object</code> | Scene object to be released. |

<a name="Robot+fkm"></a>

### robot.fkm(n, q) ⇒
Calculates the forward kinematics of the robot.

**Kind**: instance method of [<code>Robot</code>](#Robot)  
**Returns**: 4x4 math.js homogeneous transformation matrix representing the forward kinematics.  

| Param | Type | Description |
| --- | --- | --- |
| n | <code>number</code> | DH referential for which the forward kinematics will be calculated. |
| q | <code>object</code> | Configuration of the robot for the calculation of the forward kinematics. |

<a name="Robot+_jac_geo"></a>

### robot.\_jac\_geo(axis) ⇒
Calculates the geometric jacobian.

**Kind**: instance method of [<code>Robot</code>](#Robot)  
**Returns**: 6xN math.js matrix representing the geometric jacobian.  

| Param | Type | Description |
| --- | --- | --- |
| axis | <code>number</code> | DH referential for which the geometric jacobian will be calculated. |

<a name="Robot+create_kuka_kr5"></a>

### robot.create\_kuka\_kr5() ⇒
Creates a KUKA KR5.

**Kind**: instance method of [<code>Robot</code>](#Robot)  
**Returns**: Robot object configured as a KUKA KR5.  
<a name="Robot+create_epson_t6"></a>

### robot.create\_epson\_t6() ⇒
Creates an Epson T6.
