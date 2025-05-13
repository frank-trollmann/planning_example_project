

from os import path
import random
import time

from requests import get


class Timed_Experiment:

    def __init__(self, graph, pathfinder_constructor, nr_runs, random_seed=None):
        self.graph = graph
        self.pathfinder_constructor = pathfinder_constructor
        self.nr_runs = nr_runs
        self.random_seed = random_seed

        self.run_times = []
        self.nr_extensions = []
        

    def run(self):
        if self.random_seed is not None:
            random.seed(self.random_seed)

        
        for i in range(self.nr_runs):

            start_node = random.randint(0, self.graph.num_nodes - 1)
            end_node = random.randint(0, self.graph.num_nodes - 1)
            pathfinder = self.pathfinder_constructor(self.graph)

            print(f"Running {self.pathfinder_constructor.__name__} on {start_node} to {end_node}")

            start = time.time_ns()
            _, _ = pathfinder.search(start_node, end_node)
            end = time.time_ns()
            time_ns = end - start
            self.run_times.append(time_ns)
            self.nr_extensions.append(pathfinder.get_last_step_count())

    def get_average_time(self):	
        """
            Returns the average time taken for the runs in nanoseconds.
        """
        return sum(self.run_times) / len(self.run_times)

    def get_max_time(self):
        """
            Returns the maximum time taken for the runs in nanoseconds.
        """
        return max(self.run_times)
    
    def get_min_time(self):
        """
            Returns the minimum time taken for the runs in nanoseconds.
        """
        return min(self.run_times)
    
    def get_overall_time(self):
        """
            Returns the overall time taken for the runs in nanoseconds.
        """
        return sum(self.run_times)
    
    def get_nr_extensions(self):
        """
            Returns the overall number of nodes extended
        """
        return sum(self.nr_extensions)
    
    def get_average_extension_time(self):
        """
            Returns the average time taken for one extension
        """
        return self.get_overall_time() / self.get_nr_extensions()