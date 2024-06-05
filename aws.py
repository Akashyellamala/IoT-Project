from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import time

# Unique client ID for your device
clientId = "MyCobotClient"

# Your AWS IoT endpoint (substitute with your actual endpoint)
endpoint = "YOUR_AWS_IOT_ENDPOINT"

# Paths to the certificates and private key
caFilePath = "/mnt/data/AmazonRootCA1.pem"  # Using the Amazon Root CA 1 file
keyFilePath = "/mnt/data/d12589071730d0f57fc9b92945c6d75f27092dafaedd65043cac88d90427073f-private.pem.key"  # Your private key
certFilePath = "/mnt/data/d12589071730d0f57fc9b92945c6d75f27092dafaedd65043cac88d90427073f-certificate.pem.crt"  # Your certificate

# Initialize the MQTT client
mqttClient = AWSIoTMQTTClient(clientId)
mqttClient.configureEndpoint(endpoint, 8883)  # Port 8883 is the default port for AWS IoT MQTT
mqttClient.configureCredentials(caFilePath, keyFilePath, certFilePath)

# Connect and subscribe to AWS IoT
mqttClient.connect()

# Callback function to handle incoming messages
def customCallback(client, userdata, message):
    print("Received a new message: ")
    print(message.payload)
    print("from topic: ")
    print(message.topic)
    print("--------------\n\n")

# Subscribe to a topic
mqttClient.subscribe("mycobot/commands", 1, customCallback)

# Keep the client connected and listening for messages
while True:
    time.sleep(1)
