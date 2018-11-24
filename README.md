# CENG435-TermProject1
CENG435 - Data Communications and Networking Term Project 1

## Authors
Fatih DEVELİ 2330892
Resul ÇİFTÇİ 1942598
Group 3

## Getting Started

The source files should be sent to related virtual machines.

### Prerequisites

Python packages scipy and numpy must be installed.

```
$ sudo apt-get install python-pip
$ sudo pip install numpy scipy
```

### Setting up the virtual machines

Send the source files to related virtual machines.

source.py -------> s  
broker.py -------> b  
router1.py ------> r1  
router2.py ------> r2  
destination.py --> d  


## Deployment

To run the system, python scripts on each node should be executed.

```
$ python broker.py
```

source.py must be run only if all other scripts are already running. Running order of other
scripts is not important.

### Running the tests
tc/netem commands are used to apply network emulation delay to the system.

If the command is run for the first time on an interface, "add" version should be used, 
otherwise "add" must be replaced with "change".

#### Experiment 1

To apply 1ms network emulation delay in r1 and r2, following commands are used:
```
# tc qdisc add dev eth1 root netem delay 1ms 5ms distribution normal
# tc qdisc add dev eth2 root netem delay 1ms 5ms distribution normal
```

#### Experiment 2

To apply 20ms network emulation delay in r1 and r2, following commands are used:

```
# tc qdisc change dev eth1 root netem delay 20ms 5ms distribution normal
# tc qdisc change dev eth2 root netem delay 20ms 5ms distribution normal
```

#### Experiment 3
To apply 60ms network emulation delay in r1 and r2, following commands are used:
```
# tc qdisc change dev eth1 root netem delay 60ms 5ms distribution normal
# tc qdisc change dev eth2 root netem delay 60ms 5ms distribution normal
```
