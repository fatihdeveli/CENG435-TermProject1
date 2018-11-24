from socket import *

destination = '10.10.5.2' # Destination address

broker_port = 2235 # Receiving port (broker)
destination_port = 12002 # Sending port (destination)

message_size = 256 # Predefined packet size

broker_socket = socket(AF_INET, SOCK_DGRAM)
broker_socket.bind(('', broker_port))

destination_socket = socket(AF_INET, SOCK_DGRAM)

print 'Router 2 is ready'
while 1:
	try:
		message, broker_address = broker_socket.recvfrom(message_size)
	except(KeyboardInterrupt):
		exit()
	destination_socket.sendto(message, (destination, destination_port))
