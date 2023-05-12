from collections import deque


class BaseAlgorithm:
    """
    Base class for all algorithms.
    """
    #process_compare_prop = 'arrival_time'

    def __init__(self, processes):
        """
        Initialize the algorithm.
        :param processes: list of processes to be executed.
        """
        self.processes = deque(processes)

    def run(self):
        """
        Run the algorithm.
        :return: {
            "processes": list of executed processes,
            "time": total time of execution,
            "throughput": total throughput,
            "average_turnaround_over_service": average turnaround over service (used for performance analysis),
            "average_turnaround_time": average turnaround time,
            "average_response_time": average response time
        }
        """
        raise NotImplementedError
