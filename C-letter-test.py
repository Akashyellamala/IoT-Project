import time
from pymycobot.mycobot import MyCobot
from pymycobot.genre import Angle
from pymycobot import PI_PORT, PI_BAUD

# Constants
DEFAULT_POSITION = [0, 0, 0, 0, 0, 0]
# Adjusted path for drawing 'C' at a lower position
LETTER_C_PATH = [
    [0, -40, -90, -40, 60, 0],  # Start at a lower point
    [0, -45, -95, -45, 65, 10],
    [0, -50, -100, -50, 70, 20],
    [0, -45, -95, -45, 65, 30],
    [0, -40, -90, -40, 60, 40]  # End at a lower point
]

def setup_robot():
    mc = MyCobot(PI_PORT, PI_BAUD)
    return mc

def move_to_position(mc, position, speed=50):
    print(f"Moving to position: {position} at speed {speed}.")
    mc.send_angles(position, speed)
    time.sleep(3)  # Adjust time as needed

def draw_letter_c(mc):
    print("Starting to draw letter C at a lower position.")
    for pos in LETTER_C_PATH:
        move_to_position(mc, pos, speed=30)
    print("Letter 'C' drawn at a lower position.")

def main():
    mc = setup_robot()
    print("Moving to default position...")
    move_to_position(mc, DEFAULT_POSITION)  # Move to default position at startup

    print("Drawing letter 'C' at startup.")
    draw_letter_c(mc)  # Draw 'C' at startup

    while True:
        user_input = input("Press 'Q' to quit and return to default position: ").upper()
        if user_input == 'Q':
            print("Quitting program and returning to default position...")
            move_to_position(mc, DEFAULT_POSITION)
            break
        else:
            print("Invalid input. Please press 'Q' to quit.")

if __name__ == '__main__':
    main()
