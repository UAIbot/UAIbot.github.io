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

def ABB_CRB():
    robot = ub.Robot.create_abb_crb() #Instantiate robot
    sim = ub.Simulation([robot]) #Instantiate simulation
    sim.save(os.path.dirname(__file__), "ABB_CRB")

def DARWIN_MINI():
    robot = ub.Robot.create_darwin_mini() #Instantiate robot
    sim = ub.Simulation([robot]) #Instantiate simulation
    sim.save(os.path.dirname(__file__), "DARWIN_MINI")

def EPSON_T6():
    robot = ub.Robot.create_epson_t6() #Instantiate robot
    sim = ub.Simulation([robot]) #Instantiate simulation
    sim.save(os.path.dirname(__file__), "EPSON_T6")

def FRANKA_ERMIKA_3():
    robot = ub.Robot.create_franka_ermika_3() #Instantiate robot
    sim = ub.Simulation([robot]) #Instantiate simulation
    sim.save(os.path.dirname(__file__), "FRANKA_ERMIKA_3")

def KUKA_KR5():
    robot = ub.Robot.create_kuka_kr5() #Instantiate robot
    sim = ub.Simulation([robot]) #Instantiate simulation
    sim.save(os.path.dirname(__file__), "KUKA_KR5")

def KUKA_LBR_IIWA():
    robot = ub.Robot.create_kuka_lbr_iiwa() #Instantiate robot
    sim = ub.Simulation([robot]) #Instantiate simulation
    sim.save(os.path.dirname(__file__), "KUKA_LBR_IIWA")

def STAUBLI_TX60():
    robot = ub.Robot.create_staubli_tx60() #Instantiate robot
    sim = ub.Simulation([robot]) #Instantiate simulation
    sim.save(os.path.dirname(__file__), "STAUBLI_TX60")

if __name__ == "__main__":
    creating_a_simulation()
    adding_objects_to_the_simulation()
    moving_simulation_elements()
    ABB_CRB()
    DARWIN_MINI()
    EPSON_T6()
    FRANKA_ERMIKA_3()
    KUKA_KR5()
    KUKA_LBR_IIWA()
    STAUBLI_TX60()
