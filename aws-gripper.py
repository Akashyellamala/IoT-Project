import time
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from pymycobot.mycobot import MyCobot
from pymycobot.genre import Angle
from pymycobot import PI_PORT, PI_BAUD

# Constants for gripper positions
GRIPPER_OPEN = 100
GRIPPER_CLOSED = 0

# AWS IoT Core endpoint
MQTT_HOST = "a3rn8165e38k1c-ats.iot.ap-southeast-2.amazonaws.com"

# Paths to the certificate files
CA_FILE = "AmazonRootCA1.pem"  # Update with the correct name/path if different
CERT_FILE = "d12589071730d0f57fc9b92945c6d75f27092dafaedd65043cac88d90427073f-certificate.pem.crt"
PRIVATE_KEY_FILE = "d12589071730d0f57fc9b92945c6d75f27092dafaedd65043cac88d90427073f-private.pem.key"

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

def mqtt_callback(client, userdata, message):
    print("Received message from IoT Core: " + message.payload.decode())
    command = message.payload.decode()
    if command == 'open_gripper':
        control_gripper(mc, GRIPPER_OPEN)
    elif command == 'close_gripper':
        control_gripper(mc, GRIPPER_CLOSED)

def main():
    mc = MyCobot(PI_PORT, PI_BAUD)
    move_to_default(mc)

    myMQTTClient = AWSIoTMQTTClient("MyCobotClient")
    myMQTTClient.configureEndpoint(MQTT_HOST, 8883)
    myMQTTClient.configureCredentials(CA_FILE, PRIVATE_KEY_FILE, CERT_FILE)
    myMQTTClient.connect()
    myMQTTClient.subscribe("mycobot/commands", 1, mqtt_callback)

    print("MQTT Client Connected and Subscribed to Topic")
    while True:
        time.sleep(1)

if __name__ == '__main__':
    main()
