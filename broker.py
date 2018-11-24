from socket import *

from datetime import datetime
from time import sleep


source_port = 2239 # Receiving port
# Sending ports
r1_port = 2234
r2_port = 2235

r1_name = '10.10.3.1'
r2_name = '10.10.4.2'

message_size = 256 # Predefined packet size

source_socket = socket(AF_INET,SOCK_STREAM)
source_socket.bind(("",source_port))
source_socket.listen(1)
print 'Broker is ready to receive'

connection_socket, addr = source_socket.accept()

r1_socket = socket(AF_INET, SOCK_DGRAM)
r2_socket = socket(AF_INET, SOCK_DGRAM)

for i in range(0,200):
	message = connection_socket.recv(message_size)
	r1_socket.sendto(message, (r1_name, r1_port))
	r2_socket.sendto(message, (r2_name, r2_port))

r1_socket.close()
r2_socket.close()
source_socket.close()
