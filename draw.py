import time
from pymycobot.mycobot import MyCobot
from pymycobot.genre import Angle
from pymycobot import PI_PORT, PI_BAUD

# Constants for gripper operation and drawing parameters
GRIPPER_OPEN = 100
GRIPPER_CLOSED = 0

# Define the drawing patterns with joint angles
PATTERNS = {
    'square': [
        [0, -45, 45, -45, 0, 0], [0, -45, -45, 45, 0, 0], 
        [0, 45, -45, 45, 0, 0], [0, 45, 45, -45, 0, 0], [0, -45, 45, -45, 0, 0]
    ],
    'triangle': [
        [0, -60, 0, 60, 0, 0], [0, -30, -60, 30, 0, 0], 
        [0, 30, -60, 30, 0, 0], [0, -60, 0, 60, 0, 0]
    ],
    'star': [
        [0, -60, 0, 60, 0, 0], [0, -30, -45, 30, 0, 0], 
        [0, 30, -45, 30, 0, 0], [0, 60, 0, -60, 0, 0],
        [0, 0, -90, 0, 0, 0], [0, -60, 0, 60, 0, 0]
    ]
}

def initialize_robot():
    mc = MyCobot(PI_PORT, 115200)
    mc.send_angles([0, 0, 0, 0, 0, 0], 50)
    time.sleep(2)
    return mc

def draw_pattern(mc, pattern_key):
    if pattern_key not in PATTERNS:
        print("Pattern not found!")
        return
    print(f"Drawing {pattern_key}...")
    for angles in PATTERNS[pattern_key]:
        mc.send_angles(angles, 50)
        time.sleep(1.5)

def main():
    mc = initialize_robot()
    print("Choose a pattern to draw:")
    while True:
        choice = input("Enter 1 for square, 2 for triangle, 3 for star, 4 to quit: ")
        if choice == '1':
            draw_pattern(mc, 'square')
        elif choice == '2':
            draw_pattern(mc, 'triangle')
        elif choice == '3':
            draw_pattern(mc, 'star')
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
