import time
from pymycobot.mycobot import MyCobot
from pymycobot.genre import Angle
from pymycobot import PI_PORT, PI_BAUD

# Constants
GRIPPER_OPEN = 100
GRIPPER_CLOSED = 0
default_position = [0, 0, 0, 0, 0, 0]
pickup_at = [-90, 90, -100, 0, 0, -60]
dropoff_at = [90, 90, -100, 0, 0, -60]
LETTER_C_PATH = [
    [0, 35, 0, 0, 0, 0],   # Starting position with pen near the board
    [60, 35, 0, 0, 0, 0],  # Start drawing the upper curve of 'C'
    [-60, 35, 0, 0, 0, 0], # Complete the lower curve of 'C'
]

# Initialize robot connection
mc = MyCobot(PI_PORT, PI_BAUD)

def move_to_position(position, speed=30):
    print(f"Moving to position: {position}")
    mc.send_angles(position, speed)
    time.sleep(2)

def operate_gripper(action):
    if action == 'open':
        print("Opening gripper...")
        mc.set_gripper_value(GRIPPER_OPEN, 70)
    elif action == 'close':
        print("Closing gripper...")
        mc.set_gripper_value(GRIPPER_CLOSED, 70)
    time.sleep(1)

def draw_letter_c():
    print("Starting to draw letter C...")
    for coords in LETTER_C_PATH:
        move_to_position(coords, 30)
    print("Finished drawing letter C.")

def main():
    print("Checking and moving to default position...")
    move_to_position(default_position)

    while True:
        cmd = input("Enter command (P: Pick pen, D: Drop pen, C: Draw 'C', Q: Quit): ").upper()
        if cmd == 'P':
            move_to_position(pickup_at)
            operate_gripper('open')
            operate_gripper('close')
        elif cmd == 'D':
            move_to_position(dropoff_at)
            operate_gripper('open')
        elif cmd == 'C':
            draw_letter_c()
        elif cmd == 'Q':
            print("Quitting and returning to default position...")
            move_to_position(default_position)
            break
        else:
            print("Invalid input. Please enter a valid command.")

if __name__ == '__main__':
    main()
