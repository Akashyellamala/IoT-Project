import time
from pymycobot.mycobot import MyCobot
from pymycobot.genre import Angle
from pymycobot import PI_PORT, PI_BAUD

# Constants
GRIPPER_OPEN = 100
GRIPPER_CLOSED = 0
default_position = [0, 0, 0, 0, 0, 0]
pickup_at = [-90, 90, -100, 0, 0, -60]  # Assuming these are the pickup coordinates
dropoff_at = [90, -90, -100, 0, 0, -60]  # Assuming these are the dropoff coordinates
LETTER_L_PATH = [
    [0, 0, 0, 0, 0, 0],      # Initial position for starting the letter 'L'
    [-90, 90, -100, 0, 0, 0], # Move to the starting point of the vertical line
    [-90, 90, 0, 0, 0, 0],    # Draw the vertical line up
    [0, 90, 0, 0, 0, 0],      # Move horizontally to start the base of 'L'
    [0, 180, 0, 0, 0, 0]      # Draw the base of 'L'
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

def draw_letter_l():
    print("Starting to draw letter L...")
    for coords in LETTER_L_PATH:
        move_to_position(coords, 30)
    print("Finished drawing letter L.")

def main():
    print("Checking and moving to default position...")
    move_to_position(default_position)

    while True:
        cmd = input("Enter command (P: Pick pen, L: Draw 'L', Q: Quit): ").upper()
        if cmd == 'P':
            move_to_position(pickup_at)
            operate_gripper('open')
            operate_gripper('close')
        elif cmd == 'L':
            draw_letter_l()
        elif cmd == 'Q':
            print("Quitting and returning to default position...")
            move_to_position(dropoff_at)
            operate_gripper('open')
            move_to_position(default_position)
            break
        else:
            print("Invalid input. Please enter a valid command.")

if __name__ == '__main__':
    main()
