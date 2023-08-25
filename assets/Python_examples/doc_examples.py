import uaibot as ub
import numpy as np
import os 

def creating_a_simulation():
    sim = ub.Simulation() 
    sim.save(os.path.dirname(__file__), "creating_a_simulation")

def adding_objects_to_the_simulation():
    cube_position = ub.Utils.trn([0.06, -0.525, 0.05]) #Create HTM for positioning the cube
    cube = ub.Box(htm=cube_position, width=0.1, depth=0.1, height=0.1, color="red") #Instantiate cube

    robot = ub.Robot.create_epson_t6(color="gray") #Instantiate robot

    sim = ub.Simulation([cube, robot]) #Instantiate simulation

    sim.save(os.path.dirname(__file__), "adding_objects_to_the_simulation")

def moving_simulation_elements():

    cube_position = ub.Utils.trn([0.12, -0.525, 0.05]) #Create HTM for positioning the cube
    cube = ub.Box(htm=cube_position, width=0.1, depth=0.1, height=0.1, color="red") #Instantiate cube

    robot = ub.Robot.create_epson_t6(color="gray") #Instantiate robot

    sim = ub.Simulation([cube, robot]) #Instantiate simulation

    for i in range(392):
        robot.add_ani_frame(time = i*0.02, q = [ np.cos(i/50), np.cos(i/50), 0.04*np.cos(i/25)+0.06])
        if i == 157:
            robot.attach_object(cube) #Catch cube

        if i == 314:
            robot.detach_object(cube) #Release cube

    sim.save(os.path.dirname(__file__), "moving_simulation_elements")

if __name__ == "__main__":
    creating_a_simulation()
    adding_objects_to_the_simulation()
    moving_simulation_elements()
