---
layout: default
title: uaibot.simulation
parent: Python API reference
---

# uaibot.simulation module

<a id="module-uaibot.simulation"></a>

### *class* uaibot.simulation.Simulation(obj_list=[], ambient_light_intensity=12, ldr_urls=None, camera_type='perspective', width=800, height=600, show_world_frame=True, show_grid=True, load_screen_color='#19bd39', background_color='white', camera_start_pose=None)

Bases: `object`

A simulation variable.

## Parameters

obj_list
: The objects that will be added initially to the simulation.
  (default: empty list)

ambient_light_intensity
: The intensity of the ambient light.
  (default: 12).

ldr_urls
: A list containing the LDR lightning images in the following order:
  [positive_x, negative_x, positive_y, negative_y, positive_z, negative_z].
  If None, no LDR is used.
  (default: None).

camera_type
: The camera type, either “orthographic” or “perspective”.
  (default: “perspective”).

width
: The canvas width, in pixels.
  (default: 800).

height
: The canvas height, in pixels.
  (default: 600).

show_world_frame: boolean
: If the frame in the middle of the scenario is shown.
  (default: True).

show_grid
: If the grid in the scenario is shown.
  (default: True).

load_screen_color
: The color of the loading screen.
  (default: “#19bd39”).

background_color
: The color of the background.
  (default: “white”).

camera_start_pose: vector or list with 7 entries, or None
: The camera starting configuration. The first three elements is the camera position (x,y,z).
  The next three is a point in which the camera is looking at.
  The final one is the camera zoom.
  If None, uses a default configuration for the camera.
  (default: None).

#### add(obj_sim)

Add an object to the simulation. It should be an object that
can be simulated (Utils.is_a_obj_sim(obj) is true).

### Parameters

obj_sim
: The object(s) to be added to simulation.

#### *property* ambient_light_intensity

A list of all object names.

#### *property* background_color

Color of the background of the scenario

#### *property* camera_start_pose

The camera starting pose. The first three elements are the starting camera position, the next three ones
is the starting point in which the camera is looking at and the last one is the zoom

#### *property* camera_type

Type of the camera.

#### *static* create_sim_factory(objects)

Create an environment of a factory.
Factory panorama taken from:
‘[https://www.samrohn.com/360-panorama/chrysler-factory-detroit-usa-360-tour/chrysler-factory-360-panorama-tour-007/](https://www.samrohn.com/360-panorama/chrysler-factory-detroit-usa-360-tour/chrysler-factory-360-panorama-tour-007/)’

### Parameters

objects: list of objects that can be simulated (see Utils.IS_OBJ_SIM)
: The objects to be added to the scenario.

### Returns

sim: ‘Simulation’ object
: Simulation object.

#### *static* create_sim_grid(objects)

#### *static* create_sim_kinesis(objects)

Create an environment of a the Kinesis lab.
Factory panorama taken from:
‘[https://www.samrohn.com/360-panorama/chrysler-factory-detroit-usa-360-tour/chrysler-factory-360-panorama-tour-007/](https://www.samrohn.com/360-panorama/chrysler-factory-detroit-usa-360-tour/chrysler-factory-360-panorama-tour-007/)’

### Parameters

objects: list of objects that can be simulated (see Utils.IS_OBJ_SIM)
: The objects to be added to the scenario.

### Returns

sim: ‘Simulation’ object
: Simulation object.

#### *static* create_sim_outside(objects)

Create an environment of a the Kinesis lab.
Outside panorama taken from:
‘[https://opengameart.org/content/skiingpenguins-skybox-pack](https://opengameart.org/content/skiingpenguins-skybox-pack)’

### Parameters

objects: list of objects that can be simulated (see Utils.IS_OBJ_SIM)
: The objects to be added to the scenario.

### Returns

sim: ‘Simulation’ object
: Simulation object.

#### gen_code()

Generate code for injection.

#### *property* height

Height, in pixels, of the canvas

#### *property* ldr_urls

A list of the LDR light urls.

#### line *= '//------------------------------------------------------------'*

#### *property* list_of_names

A list of all object names.

#### *property* list_of_objects

A list of all objects.

#### *property* load_screen_color

Loading screen color

#### p *= PosixPath('/home/enacom/.local/lib/python3.10/site-packages/uaibot/threejs_sim.js')*

#### run()

Run simulation.

#### save(address, file_name)

Save the simulation as a self-contained HTML file.

### Parameters

address
: The address of the path (example “D:").

file_name: string
: The name of the file (“the .html” extension should not appear)

#### set_parameters(ambient_light_intensity=None, ldr_urls=None, camera_type=None, width=None, height=None, show_world_frame=None, show_grid=None, load_screen_color=None, background_color=None, camera_start_pose=None)

Change the simulation parameters.

### Parameters

ambient_light_intensity
: The intensity of the ambient light.
  If None, does not change the current value.
  (default: None).

ldr_urls
: A list containing the LDR lightning images in the following order:
  [positive_x, negative_x, positive_y, negative_y, positive_z, negative_z].
  If None, does not change the current value.
  (default: None).

camera_type
: The camera type, either “orthographic” or “perspective”.
  If None, does not change the current value.
  (default: None).

width
: The canvas width, in pixels.
  If None, does not change the current value.
  (default: None).

height
: The canvas height, in pixels.
  If None, does not change the current value.
  (default: None).

show_world_frame: boolean
: If the frame in the middle of the scenario is shown.
  If None, does not change the current value.
  (default: None).

show_grid
: If the grid in the scenario is shown.
  If None, does not change the current value.
  (default: None).

load_screen_color
: The color of the loading screen.
  If None, does not change the current value.
  (default: None).

background_color
: The color of the background.
  If None, does not change the current value.
  (default: None).

camera_start_pose: vector or list with 7 entries, or None
: The camera starting configuration. The first three elements is the camera position (x,y,z).
  The next three is a point in which the camera is looking at.
  The final one is the camera zoom.
  If None, does not change the current value.
  (default: None).

#### *property* show_grid

If the grid in the world is shown

#### *property* show_world_frame

If the world frame is shown

#### *property* width

Width, in pixels, of the canvas
