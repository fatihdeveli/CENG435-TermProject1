from socket import *
from time import sleep
from datetime import datetime

f = open("A Tale of Two Cities.txt"); # Obtain the sensor readings
sensor = ''
for line in f:
    sensor = sensor + line
f.close()

server_name = '172.17.2.15' # IP address of broker
server_port = 2237
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_name,server_port))
payload_size = 2048-27 # characters

length = len(sensor)

for i in range(0, length, payload_size):
	message = str(datetime.utcnow()) + '~' + sensor[i:i+payload_size]
	client_socket.send(message)
	sleep(0.05)

client_socket.close()
