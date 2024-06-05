import time
from pymycobot.mycobot import MyCobot
from pymycobot.genre import Angle
from pymycobot import PI_PORT, PI_BAUD

# Define positions
default_position = [0, 0, 0, 0, 0, 0]  # Adjust as necessary for your setup
pickup_at = [-90, 90, -100, 0, 0, -60]
dropoff_at = [0, 90, -100, 0, 0, -60]

def move_to_position(mc, position, speed=30):
    """Move to specified position with given speed."""
    print(f"Moving to position: {position} at speed {speed}.")
    mc.send_angles(position, speed)
    time.sleep(2.5)  # Wait for movement to complete

def get_pencil(mc):
    """Procedure to pick up the pencil."""
    mc.send_angle(Angle.J6.value, 30, speed=30)
    time.sleep(2.5)
    mc.set_gripper_value(30, speed=30)
    time.sleep(2.5)

    # Confirm pencil pickup
    x = input("Is the pencil in position (y/N)? ")
    while x.lower() != 'y':
        if x.lower() == 'n':
            raise Exception("Did not pick up pencil")
        x = input("Please input 'y' when pencil is secured: ")

    mc.set_gripper_value(10, speed=30)  # Adjust gripper to secure pencil
    time.sleep(2.5)

def drop_pencil(mc):
    """Drop the pencil at the drop-off position."""
    mc.set_gripper_value(100, speed=30)  # Open gripper to drop
    time.sleep(0.5)

def return_to_default(mc):
    """Return robot to default starting position."""
    if mc.get_angles() != default_position:
        print("Returning to default position...")
        move_to_position(mc, default_position)
    else:
        print("Already in default position.")

def main():
    mc = MyCobot(PI_PORT, PI_BAUD)
    return_to_default(mc)  # Ensure robot starts at default position

    while True:
        user_input = input("Enter 'P' to pick up, 'D' to drop off, 'Q' to quit: ").upper()
        if user_input == 'P':
            move_to_position(mc, pickup_at)
            get_pencil(mc)
        elif user_input == 'D':
            move_to_position(mc, dropoff_at)
            drop_pencil(mc)
        elif user_input == 'Q':
            print("Quitting...")
            return_to_default(mc)
            break
        else:
            print("Invalid input. Please press 'P', 'D', or 'Q'.")

if __name__ == '__main__':
    main()
