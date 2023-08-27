--- 
layout: default
title: uaibot.graphics.meshmaterial
parent: uaibot.graphics
grand_parent: Python API reference
--- 

# uaibot.graphics.meshmaterial module

<a id="module-uaibot.graphics.meshmaterial"></a>

### *class* uaibot.graphics.meshmaterial.MeshMaterial(opacity=1, shadow_side='null', side='null', alpha_map='', ao_map='', ao_map_intensity=1, bump_map='', bump_map_scale=1, color='white', emissive='black', emissive_map='', emissive_intensity=1, env_map='', env_map_intensity=1, flat_shading=False, light_map='', light_map_itensity=1, texture_map='', metalness=0, metalness_map='', normal_map='', normal_scale=[1, 1], refraction_ratio=0.98, roughness=1, roughness_map='', clearcoat=0, clearcoat_map='', clearcoat_normal_map='', clearcoat_normal_scale=[1, 1], clearcoat_roughness=0, clearcoat_roughness_map='', ior=1.5, reflectivity=0.5, sheen=0, sheen_roughness=1, sheen_roughness_map='', sheen_color='white', sheen_color_map='', specular_intensity=0, specular_intensity_map='', specular_color='white', specular_color_map='', transmission=0, transmission_map='')

Bases: `object`

A class that contains a Mesh Material for applying into objects.
It is essentially a wrapper of threejs’ ‘MeshPhysicalMaterial’ class.
See [https://threejs.org/docs/#api/en/materials/MeshPhysicalMaterial](https://threejs.org/docs/#api/en/materials/MeshPhysicalMaterial) for
more details.

## Parameters

opacity
: Mirrors ‘Material.opacity’ in threejs.
  Float in the range of 0.0 - 1.0 indicating how transparent the material is.
  A value of 0.0 indicates fully transparent, 1.0 is fully opaque.
  The attribute ‘transparent’ is set to true automatically if opacity<1.
  (default: 1).

shadow_side
: Mirrors ‘Material.shadowSide’ in threejs.
  Defines which side of faces cast shadows. When set, can be
  ‘’FrontSide’, ‘BackSide’, or ‘DoubleSide’ or ‘null’.
  (default: ‘null’).

side
: Mirrors ‘Material.side’ in threejs.
  Defines which side of faces will be rendered - front, back or both.
  Default is ‘FrontSide’. Other options are ‘BackSide’ and ‘DoubleSide’.
  (default: ‘FrontSide’).

alpha_map
: Mirrors ‘MeshStandardMaterial.alphaMap’ in threejs.
  The alpha map is a grayscale texture that controls the opacity across the surface
  (black: fully transparent; white: fully opaque).
  If it is a string, a default texture is created from it.
  If it is the empty string, it is ignored.
  (default: empty string).

ao_map
: Mirrors ‘MeshStandardMaterial.aoMap’ in threejs.
  The red channel of this texture is used as the ambient occlusion map.
  The aoMap requires a second set of UVs.
  If it is a string, a default texture is created from it.
  If it is the empty string, it is ignored.
  (default: empty string).

ao_map_intensity
: Mirrors ‘MeshStandardMaterial.aoMapIntensity’ in threejs.
  Intensity of the ambient occlusion effect. Default is 1. Zero is no occlusion effect.
  (default: 1).

ao_map_intensity
: Mirrors ‘MeshStandardMaterial.aoMapIntensity’ in threejs.
  Intensity of the ambient occlusion effect. Default is 1. Zero is no occlusion effect.
  (default: 1).

bump_map
: Mirrors ‘MeshStandardMaterial.bumpMap’ in threejs.
  The texture to create a bump map. The black and white values map to the perceived depth in relation to the lights.
  Bump doesn’t actually affect the geometry of the object, only the lighting. If a normal map is defined this will
  be ignored.
  If it is a string, a default texture is created from it.
  If it is the empty string, it is ignored.
  (default: empty string).

bump_scale
: Mirrors ‘MeshStandardMaterial.bumpScale’ in threejs.
  How much the bump map affects the material.
  (default: 1).

color
: Mirrors ‘MeshStandardMaterial.color’ in threejs.
  Color of the material.
  (default: “white”).

emissive
: Mirrors ‘MeshStandardMaterial.emissive’ in threejs.
  Emissive (light) color of the material, essentially a solid color unaffected by other lighting.
  (default: “black”).

emissive_map
: Mirrors ‘MeshStandardMaterial.emissiveMap’ in threejs.
  Set emisssive (glow) map. Default is null. The emissive map color is modulated by the emissive color and the
  emissive intensity. If you have an emissive map, be sure to set the emissive color to something other
  than black.
  (default: empty string).

emissive_intensity
: Mirrors ‘MeshStandardMaterial.emissiveIntensity’ in threejs.
  Intensity of the emissive light. Modulates the emissive color.
  (default: 1).

env_map
: Mirrors ‘MeshStandardMaterial.envMap’ in threejs.
  The environment map. To ensure a physically correct rendering, you should only add environment maps which were
  preprocessed by ‘PMREMGenerator’.
  (default: empty string).

env_map_intensity
: Mirrors ‘MeshStandardMaterial.envMapIntensity’ in threejs.
  Scales the effect of the environment map by multiplying its color.
  (default: 1).

flat_shading
: Mirrors ‘MeshStandardMaterial.flatShading’ in threejs.
  Define whether the material is rendered with flat shading.
  (default: False).

light_map
: Mirrors ‘MeshStandardMaterial.lightMap’ in threejs.
  The light map. The lightMap requires a second set of UVs.
  (default: empty string).

light_map_intensity
: Mirrors ‘MeshStandardMaterial.lightMapIntensity’ in threejs.
  Intensity of the baked light.
  (default: 1).

texture_map: string containing an url or a ‘Texture’ object
: Mirrors ‘MeshStandardMaterial.map’ in threejs.
  The color map. The texture map color is modulated by the diffuse .color.
  (Obs: the name of this parameter in ‘Python’ is not ‘map’ because it is
  a reserved word).
  (default: empty string).

metalness
: Mirrors ‘MeshStandardMaterial.metalness’ in threejs.
  How much the material is like a metal. Non-metallic materials such as wood or stone use 0.0, metallic use 1.0,
  with nothing (usually) in between. A value between 0.0 and 1.0 could be used for a rusty metal
  look. If metalnessMap is also provided, both values are multiplied.
  (default: 0).

metalness_map: string containing an url or a ‘Texture’ object
: Mirrors ‘MeshStandardMaterial.metalnessMap’ in threejs.
  The blue channel of this texture is used to alter the metalness of the material.
  (default: empty string).

normal_map: string containing an url or a ‘Texture’ object
: Mirrors ‘MeshStandardMaterial.normalMap’ in threejs.
  The texture to create a normal map. The RGB values affect the surface normal for each pixel fragment and change
  the way the color is lit. Normal maps do not change the actual shape of the surface, only the lighting. In case
  the material has a normal map authored using the left handed convention, the y component of normalScale should
  be negated to compensate for the different handedness.
  (default: empty string).

normal_scale: 2D vector
: Mirrors ‘MeshStandardMaterial.normalScale’ in threejs.
  How much the normal map affects the material. Typical ranges are 0-1.
  (default: [1,1]).

refraction_ratio
: Mirrors ‘MeshStandardMaterial.refractionRatio’ in threejs.
  The index of refraction (IOR) of air (approximately 1) divided by the index of refraction of the material. It is
  used with environment mapping modes ‘CubeRefractionMapping’ and ‘EquirectangularRefractionMapping’.
  The refraction ratio should not exceed 1.
  (default: 0.98).

roughness
: Mirrors ‘MeshStandardMaterial.roughness’ in threejs.
  How rough the material appears. 0.0 means a smooth mirror reflection, 1.0 means fully diffuse.
  If roughnessMap is also provided, both values are multiplied.
  (default: 1).

normal_map: string containing an url or a ‘Texture’ object
: Mirrors ‘MeshStandardMaterial.roughnessMap’ in threejs.
  The green channel of this texture is used to alter the roughness of the material.
  (default: empty string).

clearcoat
: Mirrors ‘MeshPhysicalMaterial.clearcoat’ in threejs.
  Represents the intensity of the clear coat layer, from 0.0 to 1.0. Use clear coat related properties to enable
  multilayer materials that have a thin translucent layer over the base layer.
  (default: 0).

clearcoat_map: string containing an url or a ‘Texture’ object
: Mirrors ‘MeshPhysicalMaterial.clearcoatMap’ in threejs.
  The red channel of this texture is multiplied against .clearcoat, for per-pixel control over a coating’s
  intensity.
  (default: empty string).

clearcoat_normal_map: string containing an url or a ‘Texture’ object
: Mirrors ‘MeshPhysicalMaterial.clearcoatNormalMap’ in threejs.
  Can be used to enable independent normals for the clear coat layer.
  (default: empty string).

clearcoat_normal_scale: 2D vector
: Mirrors ‘MeshPhysicalMaterial.clearcoatNormalScale’ in threejs.
  How much .clearcoatNormalMap affects the clear coat layer, from [0,0] to [1,1].
  (default: [1,1]).

clearcoat_roughness
: Mirrors ‘MeshPhysicalMaterial.clearcoat_roughness’ in threejs.
  Roughness of the clear coat layer, from 0.0 to 1.0.
  (default: 0).

clearcoat_roughness_map: string containing an url or a ‘Texture’ object
: Mirrors ‘MeshPhysicalMaterial.clearcoatRoughnessMap’ in threejs.
  The green channel of this texture is multiplied against .clearcoatRoughness, for per-pixel control over a
  coating’s roughness.
  (default: empty string).

ior
: Mirrors ‘MeshPhysicalMaterial.ior’ in threejs.
  Index-of-refraction for non-metallic materials, from 1.0 to 2.333.
  (default: 1.5).

reflectivity
: Mirrors ‘MeshPhysicalMaterial.reflectivity’ in threejs.
  Degree of reflectivity, from 0.0 to 1.0. Default is 0.5, which corresponds to an index-of-refraction of 1.5.
  This models the reflectivity of non-metallic materials. It has no effect when metalness is 1.0
  (default: 0.5).

sheen
: Mirrors ‘MeshPhysicalMaterial.sheen’ in threejs.
  The intensity of the sheen layer, from 0.0 to 1.0.
  (default: 0).

sheen_roughness
: Mirrors ‘MeshPhysicalMaterial.sheenRoughness’ in threejs.
  Roughness of the sheen layer, from 0.0 to 1.0.
  (default: 1).

sheen_roughness_map: string containing an url or a ‘Texture’ object
: Mirrors ‘MeshPhysicalMaterial.sheenRoughnessMap’ in threejs.
  The alpha channel of this texture is multiplied against .sheenRoughness, for per-pixel control over
  sheen roughness.
  (default: empty string).

sheen_color
: Mirrors ‘MeshPhysicalMaterial.sheenColor’ in threejs.
  The sheen tint.
  (default: “white”).

sheen_color_map: string containing an url or a ‘Texture’ object
: Mirrors ‘MeshPhysicalMaterial.sheenColorMap’ in threejs.
  The RGB channels of this texture are multiplied against .sheenColor, for per-pixel control over sheen tint.
  (default: empty string).

specular_intensity
: Mirrors ‘MeshPhysicalMaterial.specularIntensity’ in threejs.
  A float that scales the amount of specular reflection for non-metals only.
  When set to zero, the model is effectively Lambertian. From 0.0 to 1.0.
  (default: 0).

specular_intensity_map: string containing an url or a ‘Texture’ object
: Mirrors ‘MeshPhysicalMaterial.specularIntensityMap’ in threejs.
  The alpha channel of this texture is multiplied against .specularIntensity, for per-pixel control over
  specular intensity
  (default: empty string).

specular_color
: Mirrors ‘MeshPhysicalMaterial.specularColor’ in threejs.
  A Color that tints the specular reflection at normal incidence for non-metals only.
  (default: “white”).

specular_color_map: string containing an url or a ‘Texture’ object
: Mirrors ‘MeshPhysicalMaterial.specularColorMap’ in threejs.
  The RGB channels of this texture are multiplied against .specularColor, for per-pixel control over specular
  color.
  (default: empty string).

transmission
: Mirrors ‘MeshPhysicalMaterial.transmission’ in threejs.
  Degree of transmission (or optical transparency), from 0.0 to 1.0.
  Thin, transparent or semitransparent, plastic or glass materials remain largely reflective even if they are
  fully transmissive. The transmission property can be used to model these materials.
  When transmission is non-zero, opacity should be set to 1.
  (default: 0).

transmission_map: string containing an url or a ‘Texture’ object
: Mirrors ‘MeshPhysicalMaterial.transmissionMap’ in threejs.
  The red channel of this texture is multiplied against .transmission, for per-pixel control over optical
  transparency.
  (default: empty string).

#### *property* alpha_map

The alpha map texture

#### *property* ao_map

The texture for the red channel for the ambient occlusion (ao) map.

#### *property* ao_map_intensity

The ambient occlusion intensity.

#### *property* bump_map

The bump texture map.

#### *property* bump_map_scale

Bump map scale.

#### *property* clearcoat

Represents the intensity of the clear coat layer.

#### *property* clearcoat_map

Clear coat texture map.

#### *property* clearcoat_normal_map

Clear coat normal texture map.

#### *property* clearcoat_normal_scale

Clear coat normal scale.

#### *property* clearcoat_roughness

The clear coat roughness.

#### *property* clearcoat_roughness_map

The clear coat roughness texture map.

#### *property* color

The object color.

#### *property* emissive

The emissivity of the material.

#### *property* emissive_intensity

The emissivity intensity.

#### *property* emissive_map

The emissivity texture map.

#### *property* env_map

Environmental texture map.

#### *property* env_map_intensity

The intensivity of the environmental map.

#### *property* flat_shading

If the object is flat shaded.

#### gen_code(name)

#### *property* ior

Index of refraction of the material

#### *property* light_map

The texture map of the light.

#### *property* light_map_itensity

The light map intensity.

#### *property* map

The main texture map.

#### *property* metalness

The metalness of the object.

#### *property* metalness_map

The metalness texture map.

#### *property* normal_map

The normal map texture.

#### *property* normal_scale

The normal sale.

#### *property* opacity

The object opacity.

#### *property* reflectivity

The reflectivity of the material.

#### *property* refraction_ratio

The refraction ratio.

#### *property* roughness

The roughness intensity.

#### *property* roughness_map

The roughness texture map.

#### *property* shadow_side

Which side of faces casts shadows.

#### *property* sheen

The intensity of the sheen layer.

#### *property* sheen_color

The sheen color.

#### *property* sheen_color_map

The sheen color texture map.

#### *property* sheen_roughness

The sheen layer roughness.

#### *property* sheen_roughness_map

The sheen layer roughness texture map.

#### *property* side

Which side of faces will be rendered.

#### *property* specular_color

The specular color.

#### *property* specular_color_map

The specular color texture map.

#### *property* specular_intensity

The specular intensity.

#### *property* specular_intensity_map

The specular intensity texture map.

#### *property* transmission

The material transmission.

#### *property* transmission_map

The material transmission texture map.

#### *property* transparent

If the object is transparent.
