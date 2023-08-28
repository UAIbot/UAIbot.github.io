---
layout: default
title: utils.s(v)
parent: utils
grand_parent: JavaScript API reference
---

## s(v) ⇒ <code>object</code>
Returns a 3x3 matrix that implements the cross product for a 3D vector
as a matricial product, that is, a matrix S(v) such that for any other
3D column  vector w, S(v)w = cross(v,w).

**Kind**: global function  
**Returns**: <code>object</code> - 4x4 math.js matrix that implements the cross product with v.  

| Param | Type | Description |
| --- | --- | --- |
| v | <code>object</code> | 3x1 math.js matrix representing a 3D vector. |