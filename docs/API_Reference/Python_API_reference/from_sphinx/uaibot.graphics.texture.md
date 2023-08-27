--- 
layout: default
title: uaibot.graphics.texture
parent: uaibot.graphics
grand_parent: Python API reference
--- 

# uaibot.graphics.texture module

<a id="module-uaibot.graphics.texture"></a>

### *class* uaibot.graphics.texture.Texture(url, mapping='UVMapping', wrap_s='ClampToEdgeWrapping', wrap_t='ClampToEdgeWrapping', mag_filter='LinearFilter', min_filter='LinearMipmapLinearFilter', offset=[0, 0], repeat=[1, 1], rotation=0, center=[0, 0])

Bases: `object`

Texture to be applied in a Mesh Material.
It is essentially a wrapper of threejs’ ‘Texture’ class.
See ‘[https://threejs.org/docs/#api/en/textures/Texture](https://threejs.org/docs/#api/en/textures/Texture)’ for more details.

## Parameters

url
: The url that contains the texture.
  It must have one of the following formats: ‘png’, ‘bmp’, ‘jpg’, ‘jpeg’.

mapping
: Mirrors ‘Texture.mapping’ in threejs.
  How the image is applied to the object.
  A string  ‘UVMapping’ is the default, where the U,V coordinates are used to apply the map.
  It can be ‘UVMapping’, ‘CubeReflectionMapping’, ‘CubeRefractionMapping’,
  ‘EquirectangularReflectionMapping’, ‘EquirectangularRefractionMapping’,
  ‘CubeUVReflectionMapping’ or ‘CubeUVRefractionMapping’.
  (default: ‘UVMapping’).

wrap_s
: Mirrors ‘Texture.wrapS’ in threejs.
  This defines how the texture is wrapped horizontally and corresponds to U in UV mapping.
  The default is ‘ClampToEdgeWrapping’, where the edge is clamped to the outer edge texels.
  It can be ‘RepeatWrapping’, ‘ClampToEdgeWrapping’ or ‘MirroredRepeatWrapping’.
  (default: ‘ClampToEdgeWrapping’).

wrap_t
: Mirrors ‘Texture.wrapT’ in threejs.
  This defines how the texture is wrapped vertically and corresponds to V in UV mapping.
  The default is ‘ClampToEdgeWrapping’, where the edge is clamped to the outer edge texels.
  It can be ‘RepeatWrapping’, ‘ClampToEdgeWrapping’ or ‘MirroredRepeatWrapping’.
  (default: ‘ClampToEdgeWrapping’).

mag_filter
: Mirrors ‘Texture.magFilter’ in threejs.
  How the texture is sampled when a texel covers more than one pixel.
  The default is ‘LinearFilter’, which takes the four closest texels and bilinearly interpolates among them.
  It can be ‘NearestFilter’ or ‘LinearFilter’.
  (default: ‘LinearFilter’).

min_filter
: Mirrors ‘Texture.minFilter’ in threejs.
  How the texture is sampled when a texel covers less than one pixel.
  The default is ‘LinearMipmapLinearFilter’, which uses mipmapping and a trilinear filter.
  It can be ‘NearestFilter’, ‘NearestMipmapNearestFilter’, ‘NearestMipmapLinearFilter’, ‘LinearFilter’,
  ‘LinearMipmapNearestFilter’ or  ‘LinearMipmapLinearFilter’.
  (default: ‘LinearMipmapLinearFilter’).

offset
: Mirrors ‘Texture.offset’ in threejs.
  How much a single repetition of the texture is offset from the beginning, in each direction U and V.
  Typical range is 0.0 to 1.0.
  (default: [0,0]).

repeat
: Mirrors ‘Texture.repeat’ in threejs.
  How many times the texture is repeated across the surface, in each direction U and V.
  If repeat is set greater than 1 in either direction, the corresponding Wrap parameter should also be set to
  ‘RepeatWrapping’ or ‘MirroredRepeatWrapping’ to achieve the desired tiling effect.
  Setting different repeat values for textures is restricted in the same way like .offset.
  (default: [1,1]).

rotation
: How much the texture is rotated around the center point, in radians. Positive values are counter-clockwise.
  (default: 0).

center
: The point around which rotation occurs. A value of (0.5, 0.5) corresponds to the center of the texture.
  Default is [0, 0], the lower left.
  (default: [0, 0]).

#### *property* center

The shifting for the texture center.

#### gen_code(name)

#### *property* mag_filter

The method for the magnification filter.

#### *property* mapping

The method for mapping of texture.

#### *property* min_filter

The method for the mignification filter.

#### *property* offset

The offset in the texture.

#### *property* repeat

The repeat pattern.

#### *property* rotation

The texture rotation.

#### *property* url

The address of the texture.

#### *property* wrap_s

The method for wrapping in the U coordinate.

#### *property* wrap_t

The method for wrapping in the V coordinate.
