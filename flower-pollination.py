import time
from pymycobot.mycobot import MyCobot
from pymycobot.genre import Angle
from pymycobot import PI_PORT, PI_BAUD

flower_locations = [
    [-90, 90, -100, -0, 0, -60],   # Position of first flower
    [90, 90, -100, -0, 0, -60],    # Position of second flower
    # Add more positions for additional flowers as needed
]

def reach_flower(mc, flower_index):
    # Move the arm to the position near the specified flower
    mc.send_angles(flower_locations[flower_index], 50)
    time.sleep(2.5)

def pollinate(mc):
    # Perform the action of pollination
    # Add your specific code here for simulating pollination
    print("Pollinating flower...")

def move_to_next_flower(mc, current_index):
    # Move the arm horizontally to the position of the next flower
    next_index = (current_index + 1) % len(flower_locations)
    mc.send_angles(flower_locations[next_index], 50)
    time.sleep(2.5)

def do_pollination(mc):
    # Perform the task of reaching each flower, pollinating it, and moving to the next flower
    for i in range(len(flower_locations)):
        reach_flower(mc, i)
        pollinate(mc)
        if i < len(flower_locations) - 1:
            move_to_next_flower(mc, i)

if __name__ == '__main__':
    mc = MyCobot(PI_PORT, PI_BAUD)
    try:
        do_pollination(mc)
    finally:
        mc.release_all_servos()
