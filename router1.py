from socket import *

destination = '10.10.3.2' # Destination adress

broker_port = 2234 # Receiving port (broker)
destination_port = 12001 # Sending port (destination)

message_size = 256 # Predefined packet size

broker_socket = socket(AF_INET, SOCK_DGRAM)
broker_socket.bind(('', broker_port))

destination_socket = socket(AF_INET, SOCK_DGRAM)

print 'Router 1 is ready'
while 1:
	try:
		message, broker_address = broker_socket.recvfrom(message_size)
	except(KeyboardInterrupt):
		exit()
	destination_socket.sendto(message, (destination, destination_port))
