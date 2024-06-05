import time
from pymycobot.mycobot import MyCobot
from pymycobot.genre import Angle
from pymycobot import PI_PORT, PI_BAUD

# Constants for gripper positions
GRIPPER_OPEN = 0
GRIPPER_CLOSED = 100

def check_current_position(mc, target_position):
    current_position = mc.get_angles()
    return current_position == target_position

def move_to_default(mc):
    if check_current_position(mc, [0, 0, 0, 0, 0, 0]):
        print("Already in default position.")
    else:
        print("Moving to default position...")
        mc.send_angles([0, 0, 0, 0, 0, 0], 40)
        time.sleep(2)
    mc.set_gripper_value(GRIPPER_OPEN, 70)
    print("Gripper opened.")

def move_joint(mc, joint_id, angle, speed):
    current_angle = mc.get_angles()[joint_id - 1]
    if current_angle == angle:
        print(f"Joint {joint_id} is already at {angle}°.")
    else:
        print(f"Moving Joint {joint_id} to {angle}° at speed {speed}.")
        mc.send_angle(joint_id, angle, speed)
        time.sleep(3)

def control_gripper(mc, state):
    current_value = mc.get_gripper_value()
    if (state == GRIPPER_OPEN and current_value == GRIPPER_OPEN) or \
       (state == GRIPPER_CLOSED and current_value == GRIPPER_CLOSED):
        print(f"Gripper already {'opened' if state == GRIPPER_OPEN else 'closed'}.")
    else:
        mc.set_gripper_value(state, 70)  # Adjusted speed to 70
        print(f"Gripper {'opened' if state == GRIPPER_OPEN else 'closed'}.")

def main():
    mc = MyCobot(PI_PORT, PI_BAUD)
    move_to_default(mc)  # Move to default position at startup

    while True:
        user_input = input("Press 'X' for J1 to 90°, 'Y' for J1 to -90°, 'J' to close gripper, 'L' to open gripper, or 'Q' to quit: ").upper()
        if user_input == 'X':
            move_joint(mc, Angle.J1.value, 90, 50)
        elif user_input == 'Y':
            move_joint(mc, Angle.J1.value, -90, 50)
        elif user_input == 'J':
            control_gripper(mc, GRIPPER_CLOSED)
        elif user_input == 'L':
            control_gripper(mc, GRIPPER_OPEN)
        elif user_input == 'Q':
            print("Returning to default position and quitting the program...")
            move_to_default(mc)
            break
        else:
            print("Invalid input. Please press 'X', 'Y', 'J', 'L', or 'Q'.")

if __name__ == '__main__':
    main()
