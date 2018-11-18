from socket import *

from datetime import datetime
from time import sleep


source_port = 2237
r1_port = 2224
r2_port = 2225
source_socket = socket(AF_INET,SOCK_STREAM)
source_socket.bind(("",source_port))
source_socket.listen(1)
print 'Broker is ready to receive'

connection_socket, addr = source_socket.accept()

r1_name = '172.17.2.18'
r2_name = '172.17.2.19'

r1_socket = socket(AF_INET, SOCK_DGRAM)
r2_socket = socket(AF_INET, SOCK_DGRAM)

for i in range(0,376):
	message = connection_socket.recv(2048)
	r1_socket.sendto(message, (r1_name, r1_port))
	r2_socket.sendto(message, (r2_name, r2_port))
	
r1_socket.close()
r2_socket.close()
source_socket.close()
