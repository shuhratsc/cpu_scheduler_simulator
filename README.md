# CPU Scheduler Simulator
## Description
This is a CPU scheduler simulator that simulates the behavior of different CPU scheduling algorithms.
The simulator is written in Python and uses matplotlib to plot the results.
Following algorithms are implemented:
* First Come First Serve (FCFS)
* Round Robin (RR)
* Shortest Remaining Task (SRT)
* Highest Response Ratio Next (HRRN)
## Environment Setup
The simulator requires Python 3.6 or higher. Required Python packages are listed in `requirements.txt`.
They can be installed by executing the following command:
```bash
pip3 install -r requirements.txt
```
## Usage
After cloning the repository and [setting up the environment](#environment-setup),
you can run the simulator can be run by executing the following command:
```bash
python3 simulate.py -a <algorithm> -p <processes.json>
```
The following arguments are available:
* `-a <algorithm>`: The scheduling algorithm to use. Possible values are
`FCFS`, `RR`, `SRT` and `HRRN`,
* `-p <processes.json>`: The path to the JSON file containing the processes to schedule. See the section below for more information.

### processes.json
The processes JSON file contains the processes to schedule. It is a JSON array of objects. Each object represents a process and has the following properties:
* `pid`: The process ID. This is a string.
* `arrival_time`: The arrival time of the process. This is an integer.
* `service_time`: The total burst time of the process. This is an integer.
* `disk_i_o_time`: The total time a process spends waiting on disk i/o. This is an integer.
* `disk_i_o_inter`: Intervals at which process goes into a waiting state. This is a list of integer(s).

### Example for processes.json
```json
[
  {
    "pid": "A",
    "arrival_time": 0,
    "service_time": 6,
    "disk_i_o_time": 1,
    "disk_i_o_inter": [3]
  },
  
  {
    "pid": "B",
    "arrival_time": 2,
    "service_time": 12,
    "disk_i_o_time": 2,
    "disk_i_o_inter": [4,8]
  },
  
  {
    "pid": "C",
    "arrival_time": 4,
    "service_time": 8,
    "disk_i_o_time": 1,
    "disk_i_o_inter": [4]
  },
  
  {
    "pid": "D",
    "arrival_time": 6,
    "service_time": 10,
    "disk_i_o_time": 0,
    "disk_i_o_inter": []
  },
  
  {
    "pid": "E",
    "arrival_time": 8,
    "service_time": 4,
    "disk_i_o_time": 2,
    "disk_i_o_inter": [1,3]
  }
 
]

```

## Output
The simulator will output the following information:
* Average response time
* Average turnaround time
* Average ratio of turnaround and service time
* Throughput
* CPU total time
* Simulation time

