import time
from pymycobot.mycobot import MyCobot
from pymycobot.genre import Angle
from pymycobot import PI_PORT, PI_BAUD

def check_default_position(mc):
    current_angles = mc.get_angles()
    default_position = [0, 0, 0, 0, 0, 0]
    if current_angles == default_position:
        return True
    return False

def move_to_default(mc):
    if check_default_position(mc):
        print("Already in default position.")
    else:
        print("Moving to default position...")
        mc.send_angles([0, 0, 0, 0, 0, 0], 40)
        time.sleep(2)

def move_joint(mc, joint_id, angle, speed):
    print(f"Moving Joint {joint_id} to {angle}° at speed {speed}.")
    mc.send_angle(joint_id, angle, speed)
    time.sleep(3)

def main():
    mc = MyCobot(PI_PORT, PI_BAUD)
    move_to_default(mc)  # Move to default position at startup

    while True:
        user_input = input("Press 'X' to move J1 to 90°, 'Y' to move J1 to -90°, or 'Q' to quit: ").upper()
        if user_input == 'X':
            move_joint(mc, Angle.J1.value, 90, 50)
        elif user_input == 'Y':
            move_joint(mc, Angle.J1.value, -90, 50)
        elif user_input == 'Q':
            print("Returning to default position and quitting the program...")
            move_to_default(mc)
            break
        else:
            print("Invalid input. Please press 'X', 'Y', or 'Q'.")

if __name__ == '__main__':
    main()
