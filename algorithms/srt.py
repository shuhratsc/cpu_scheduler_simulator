import bisect
from collections import deque

from algorithms.base_algorithm import BaseAlgorithm


class SRT(BaseAlgorithm):
    #process_compare_prop = 'remaining_time'

    def __init__(self, processes):
        processes = sorted(processes, key=lambda x: (x.arrival_time, x.service_time))
        super().__init__(processes)
        self.ready_queue = deque([])
        self.running_process = None
        self.time = 0
        self.idle_time = 0

    def run(self):
        """
        Run the algorithm.
        :return: {
            "processes": list of executed processes,
            "time": total time of execution,
            "throughput": total throughput,
            "average_turnaround_over_service": average turnaround over service (used as performance metric),
            "average_turnaround_time": average turnaround time,
            "average_response_time": average response time
        }
        """
        executed_processes = []

        while self.processes or self.ready_queue or self.running_process:

            if self.running_process and self.running_process.remaining_time == 0:
                self.running_process.finish_time = self.time
                self.running_process.turnaround_time = self.running_process.finish_time - self.running_process.arrival_time
                self.running_process.turnaround_over_service = self.running_process.turnaround_time / self.running_process.service_time
                executed_processes.append(self.running_process)
                self.running_process = None

                if not self.processes and not self.ready_queue:
                    break

            arrived_processes = self.get_arrived_processes()

            if arrived_processes:
                min_process = min(arrived_processes, key=lambda x: x.remaining_time)

                if self.running_process is None:
                    self.running_process = min_process
                    self.running_process.start_time = self.time
                    self.running_process.response_time = self.running_process.start_time - self.running_process.arrival_time

                elif self.running_process.remaining_time > min_process.remaining_time:
                    self.append_to_ready_queue(self.running_process)
                    self.running_process = min_process
                    self.running_process.start_time = self.time
                    self.running_process.response_time = self.running_process.start_time - self.running_process.arrival_time



                for _ in range(len(arrived_processes)):
                    self.processes.popleft()

                if self.running_process in arrived_processes:
                    arrived_processes.remove(self.running_process)
                for process in arrived_processes:
                    self.append_to_ready_queue(process)
                arrived_processes.clear()

            # If no process is running, then pick the process from ready queue
            if self.running_process is None and self.ready_queue:
                self.running_process = self.ready_queue.popleft()
                if self.running_process.start_time == 'n/a':
                    self.running_process.start_time = self.time
                    self.running_process.response_time = self.running_process.start_time - self.running_process.arrival_time



            # If process is running, then get next important time and update the time
            next_time = self.get_next_important_time()
            if self.running_process:
                self.running_process.remaining_time -= next_time - self.time
            else:
                self.idle_time += next_time - self.time
            self.time = next_time

        # Calculate total time, throughput, average turnaround/service time, average turnaround time,
        # average response time
        total_time = self.time
        throughput = len(executed_processes) / total_time
        average_turnaround_over_service = sum(process.turnaround_over_service for process in executed_processes) / len(executed_processes)
        average_turnaround_time = sum(process.turnaround_time for process in executed_processes) / len(
            executed_processes)
        average_response_time = sum(process.response_time for process in executed_processes) / len(
            executed_processes)
        return {
            "processes": executed_processes,
            "total_time": total_time,
            "throughput": throughput,
            "average_turnaround_over_service": average_turnaround_over_service,
            "average_turnaround_time": average_turnaround_time,
            "average_response_time": average_response_time
        }

    def get_arrived_processes(self):
        """
        Get processes which arrived at current time.
        :return: list of arrived processes
        """
        arrived_processes = []
        for process in self.processes:
            if process.arrival_time == self.time:
                arrived_processes.append(process)
            else:
                break
        return arrived_processes

    def append_to_ready_queue(self, process):
        """
        Append process to ready queue based on priority.
        :param process: process to be appended
        """
        #bisect.insort(self.ready_queue, process)
        self.ready_queue.append(process)

    def get_next_important_time(self):
        """
        Find next point of time that need a decision
        :return: Int
        """
        if self.running_process is not None:
            if not self.processes:
                return max(self.time + self.running_process.remaining_time, self.time)

            return min(
                self.time + (self.running_process.remaining_time or 1),
                self.processes[0].arrival_time
            )

        if self.ready_queue:
            return self.time + 1

        if self.processes:
            return self.processes[0].arrival_time

        return self.time + 1

    def remove_processes(self, processes):
        """
        Remove processes from processes list
        :param processes: list of processes
        :return: None
        """
        for process in processes:
            self.processes.remove(process)
