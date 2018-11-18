from socket import *
import thread
from time import sleep
from datetime import datetime
import numpy as np
import scipy.stats
import _strptime

r1_port = 12001
r2_port = 12002

r1_socket = socket(AF_INET, SOCK_DGRAM)
r2_socket = socket(AF_INET, SOCK_DGRAM)
r1_socket.bind(('', r1_port))
r2_socket.bind(('', r2_port))

times1 = []
times2 = []

def r1():
	while 1:
		message, r1_address = r1_socket.recvfrom(2048)
		current_time = datetime.utcnow()
		message = message.split('~')
		timestamp = message[0]
		timestamp = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S.%f")
		delay = (current_time - timestamp).microseconds
		times1.append(delay)
		#print 'Received from r1 with delay ' + str(delay)

def r2():
	while 1:
		message, r2_address = r2_socket.recvfrom(2048)
		current_time = datetime.utcnow()
		message = message.split('~')
		timestamp = message[0]
		timestamp = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S.%f")
		delay = (current_time - timestamp).microseconds
                times2.append(delay)
	

try:
	thread.start_new_thread(r1,())
	thread.start_new_thread(r2,())
except:
	print "Error: unable to start thread"
	exit()

def mean_confidence_interval(data, confidence=0.95):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
    return m, m-h, m+h


print 'Destination is ready to receive'

results_length1 = -1
results_length2 = -1
#times2.append(111)
while (True):
	sleep(2)
	if ((len(times1) == results_length1 and results_length1 != 0) and (len(times2) == results_length2 and results_length2 != 0)):
		break;
	results_length1 = len(times1)
	results_length2 = len(times2)


# Calculating confidence interval

print "1: " + str(mean_confidence_interval(times1))
print "2: " + str(mean_confidence_interval(times2))
print "done"
