import time
import ssl
import json
import paho.mqtt.client as mqtt
from pymycobot.mycobot import MyCobot
from pymycobot.genre import Angle
from pymycobot import PI_PORT, PI_BAUD

# MQTT setup
MQTT_HOST = "a3rn8165e38k1c-ats.iot.ap-southeast-2.amazonaws.com"
MQTT_PORT = 8883
MQTT_TOPIC = "mycobot/commands"

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

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    try:
        data = json.loads(payload)
        handle_commands(data)
    except json.JSONDecodeError:
        print("Error decoding JSON")

def handle_commands(data):
    for command in data.get('commands', []):
        if command['action'] == 'move_to_position':
            move_to_position(command['position'], command['speed'])
        elif command['action'] == 'operate_gripper':
            operate_gripper(command['state'])
        elif command['action'] == 'draw_letter_c':
            draw_letter_c()
        elif command['action'] == 'quit':
            quit_program()

def move_to_position(position, speed=30):
    print(f"Moving to position: {position}")
    mc.send_angles(position, speed)
    time.sleep(2)

def operate_gripper(action):
    state = GRIPPER_OPEN if action == 'open' else GRIPPER_CLOSED
    print(f"{action.capitalize()}ing gripper...")
    mc.set_gripper_value(state, 70)
    time.sleep(1)

def draw_letter_c():
    print("Starting to draw letter C...")
    for coords in LETTER_C_PATH:
        move_to_position(coords, 30)
    print("Finished drawing letter C.")

def quit_program():
    print("Quitting and returning to default position...")
    move_to_position(default_position)
    client.loop_stop()
    client.disconnect()

def main():
    global client
    client = mqtt.Client()
    client.tls_set(
        ca_certs="AmazonRootCA1.pem",
        certfile="certificate.pem.crt",
        keyfile="private.pem.key",
        cert_reqs=ssl.CERT_REQUIRED,
        tls_version=ssl.PROTOCOL_TLSv1_2
    )
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(MQTT_HOST, MQTT_PORT, 60)
    client.loop_start()

    print("Checking and moving to default position...")
    move_to_position(default_position)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Program exiting...")
        client.loop_stop()
        client.disconnect()

if __name__ == '__main__':
    main()
