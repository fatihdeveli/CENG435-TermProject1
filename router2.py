from socket import *

destination = '172.17.2.16' #

broker_port = 2225 # receive
destination_port = 12002 # send

broker_socket = socket(AF_INET, SOCK_DGRAM)
broker_socket.bind(('', broker_port))

destination_socket = socket(AF_INET, SOCK_DGRAM)

print 'Router 2 is ready'
while 1:
    message, broker_address = broker_socket.recvfrom(2048)
    destination_socket.sendto(message, (destination, destination_port))

