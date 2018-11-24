from socket import *
import thread
from time import sleep
from datetime import datetime
import numpy as np
import scipy.stats
import _strptime

# Receiving ports
r1_port = 12001 
r2_port = 12002

message_size = 256 # Predefined packet size

r1_socket = socket(AF_INET, SOCK_DGRAM)
r2_socket = socket(AF_INET, SOCK_DGRAM)
r1_socket.bind(('', r1_port))
r2_socket.bind(('', r2_port))

# Lists to hold end-to-end delays of packets arriving from r1 and r2.
times1 = []
times2 = []

def r1(): # Thread r1 communicates with router 1
	while 1:
		message, r1_address = r1_socket.recvfrom(message_size)
		current_time = datetime.utcnow()
		try:
			message = message.split('~') # '~' is the separator
			timestamp = message[0] # First part is the timestamp
			timestamp = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S.%f")
			# Convert the format to be able to calculate time elapsed
			delay = (current_time - timestamp).microseconds
			times1.append(delay)
			print '\033[94m' + str(message[0]) + ': Message from r1 with delay ' + str(delay) + '\033[0m'
			print message[1]
		# If corrupted data is received, above commands fail and throw a ValueError
		except(ValueError):
			continue

def r2(): # Thread r2 communicates with router 2
	while 1:
		message, r2_address = r2_socket.recvfrom(message_size)
		current_time = datetime.utcnow()
		try:
			message = message.split('~')
			timestamp = message[0]
			timestamp = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S.%f")
			delay = (current_time-timestamp).microseconds
                	times2.append(delay)
		except(ValueError):
			continue

try:
	thread.start_new_thread(r1,())
	thread.start_new_thread(r2,())
except:
	print "Error: unable to start thread"
	exit()


"""
Function calculates the confidence interval of given data.
Returns 3 values: mean, upper and lower limits of confidence interval.
"""
def mean_confidence_interval(data, confidence=0.95):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
    return m, m-h, m+h

print 'Destination is ready to receive'

results_length1 = -1
results_length2 = -1
while (True):
	sleep(3) # Wait before checking if the processes in threads have ended.
	# Check if thread processes have ended.
	if ((len(times1) == results_length1 and results_length1 != 0) and (len(times2) == results_length2 and results_length2 != 0)):
		break;
	# Threads are active, continue
	results_length1 = len(times1)
	results_length2 = len(times2)


# Calculating confidence interval
print "Received " + str(results_length1) + " packets from r1"
print "Received " + str(results_length2) + " packets from r2"
print "r1 confidence interval: " + str(mean_confidence_interval(times1))
print "r2 confidence interval: " + str(mean_confidence_interval(times2))
print "Process completed successfully."
