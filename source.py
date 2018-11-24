from socket import *
from time import sleep
from datetime import datetime

f = open("A Tale of Two Cities.txt"); # Source of sensor readings
sensor = '' # Variable to hold sensor readings

for line in f:
    sensor = sensor + line
f.close()

broker_name = '10.10.4.1' # IP address of broker
broker_port = 2239

message_size = 256 # Predefined packet size

broker_socket = socket(AF_INET, SOCK_STREAM)
broker_socket.connect((broker_name, broker_port))

payload_size = message_size-27 # Timestamp is 27 characters.

message_counter = payload_size*200 # 200 packets will be sent.

for i in range(0, message_counter, payload_size):
	# Add timestamp to the message
	message = str(datetime.utcnow()) + '~' + sensor[i:i+payload_size]
	broker_socket.send(message)
	sleep(0.3) # Wait for the messages to be processed in the network.

broker_socket.close()
