import time

from pymycobot.mycobot import MyCobot
from pymycobot.genre import Angle
from pymycobot import PI_PORT, PI_BAUD

pickup_at = [-90, 90, -100, -0, 0, -60]  # Position to reach the dead leaf
dropoff_at = [90, 90, -100, -0, 0, -60]   # Position to drop the dead leaf in the basket

def reach_leaf(mc):
    # Move the arm to the position near the tree to reach the dead leaf
    mc.send_angles(pickup_at, 50)
    time.sleep(2.5)

def pickup_leaf(mc):
    # Move the arm slightly down to ensure the claw grips the dead leaf
    mc.send_angle(Angle.J6.value, -80, 50)
    time.sleep(1)
    
    # Close the gripper with more strength to ensure it grips the dead leaf
    mc.set_gripper_value(30, 100)
    time.sleep(2.5)

def move_to_basket(mc):
    # Move the arm to the position of the basket
    mc.send_angles(dropoff_at, 50)
    time.sleep(2.5)

def drop_leaf_in_basket(mc):
    # Open the gripper to drop the dead leaf in the basket
    mc.set_gripper_value(100, 70)
    time.sleep(0.5)

def do_task(mc):
    # Perform the task of picking up dead leaves and putting them in the basket
    reach_leaf(mc)
    pickup_leaf(mc)
    move_to_basket(mc)
    drop_leaf_in_basket(mc)

if __name__ == '__main__':
    mc = MyCobot(PI_PORT, PI_BAUD)
    try:
        do_task(mc)
    finally:
        mc.release_all_servos()
