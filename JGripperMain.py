import time
from pymycobot.mycobot import MyCobot
from pymycobot.genre import Angle
from pymycobot import PI_PORT, PI_BAUD

# Constants for gripper positions
GRIPPER_OPEN = 100
GRIPPER_CLOSED = 0

def get_current_position(mc):
    return mc.get_angles()

def move_to_default(mc):
    default_position = [0, 0, 0, 0, 0, 0]
    current_position = get_current_position(mc)
    if current_position != default_position:
        print("Moving to default position...")
        mc.send_angles(default_position, 40)
        time.sleep(2)
    else:
        print("Already in default position.")

def move_joint(mc, joint_id, angle, speed):
    current_position = get_current_position(mc)
    if current_position[joint_id - 1] != angle:
        print(f"Moving Joint {joint_id} to {angle}° at speed {speed}.")
        mc.send_angle(joint_id, angle, speed)
        time.sleep(3)
    else:
        print(f"Joint {joint_id} is already at {angle}°.")

def control_gripper(mc, state):
    current_value = mc.get_gripper_value()
    if current_value != state:
        mc.set_gripper_value(state, 70)
        print(f"Gripper {'opened' if state == GRIPPER_OPEN else 'closed'}.")
    else:
        print(f"Gripper already {'opened' if state == GRIPPER_OPEN else 'closed'}.")

def main():
    mc = MyCobot(PI_PORT, PI_BAUD)
    move_to_default(mc)  # Move to default position at startup

    while True:
        user_input = input("Press 'X' for J1-90°, 'Y' for J1--90°, 'Z' for J2-90°,'U' for J2--90°, 'C' for J3--90°,'R' for J3-90°, 'T' for J4-90°,'B' for J4--90°, 'D' for J5-90°, 'E' for J5-0°, 'F' for J5--90°, 'N' for J6--90°,'M' for J6-90°, 'G' to open gripper, 'H' to close gripper, or 'Q' to quit: ").upper()
        if user_input == 'X':
            move_joint(mc, Angle.J1.value, 90, 50)
        elif user_input == 'Y':
            move_joint(mc, Angle.J1.value, -90, 50)
        elif user_input == 'Z':
            move_joint(mc, Angle.J2.value, 50, 50)
        elif user_input == 'U':
            move_joint(mc, Angle.J2.value, -50, 50)  
        elif user_input == 'C':
            move_joint(mc, Angle.J3.value, -90, 50)
        elif user_input == 'R':
            move_joint(mc, Angle.J3.value, 0, 50)
        elif user_input == 'T':
            move_joint(mc, Angle.J4.value, 90, 50)
        elif user_input == 'B':
            move_joint(mc, Angle.J4.value, -90, 50)
        elif user_input == 'D':
            move_joint(mc, Angle.J5.value, 90, 100)
        elif user_input == 'E':
            move_joint(mc, Angle.J5.value, 0, 100)
        elif user_input == 'F':
            move_joint(mc, Angle.J5.value, -90, 100)
        elif user_input == 'N':
            move_joint(mc, Angle.J6.value, -90, 100)
        elif user_input == 'M':
            move_joint(mc, Angle.J6.value, 90, 100)   
        elif user_input == 'G':
            control_gripper(mc, GRIPPER_OPEN)
        elif user_input == 'H':
            control_gripper(mc, GRIPPER_CLOSED)
        elif user_input == 'Q':
            print("Returning to default position and quitting the program...")
            move_to_default(mc)
            control_gripper(mc, GRIPPER_OPEN)  # Ensure gripper is open when quitting
            break
        else:
            print("Invalid input. Please press 'X', 'Y', 'Z', 'U', 'C', 'R', 'T', 'B', 'D', 'E', 'F', 'N', 'M', 'G', 'H', or 'Q'.")

if __name__ == '__main__':
    main()
