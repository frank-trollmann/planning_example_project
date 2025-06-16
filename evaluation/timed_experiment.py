import random
import time

from requests import get


class Timed_Experiment:
    """
        Runs experiments and keeps track of statistics.
    """

    def __init__(self, graph, pathfinder_constructor, nr_runs, random_seed=None, verbose = False):
        self.graph = graph
        self.pathfinder_constructor = pathfinder_constructor
        self.nr_runs = nr_runs
        self.random_seed = random_seed
        self.verbose = verbose

        self.run_times = []
        self.nr_extensions = []
        self.successful_run_times = []
        self.unsucessful_run_times = []
        self.successful_extensions = []
        self.unsuccesful_extensions = []
        

    def run(self):
        """
            run the experiments as configured
        """
        if self.random_seed is not None:
            random.seed(self.random_seed)

        
        for i in range(self.nr_runs):

            start_node = random.randint(0, self.graph.num_nodes - 1)
            end_node = random.randint(0, self.graph.num_nodes - 1)
            pathfinder = self.pathfinder_constructor(self.graph)

            if self.verbose:
                print(f"Running {self.pathfinder_constructor.__name__} on {start_node} to {end_node}")

            start = time.time_ns()
            result, _ = pathfinder.search(start_node, end_node)
            end = time.time_ns()
            time_ns = end - start
            self.run_times.append(time_ns)
            self.nr_extensions.append(pathfinder.get_last_step_count())
            if result == None:
                self.unsucessful_run_times.append(time_ns)
                self.unsuccesful_extensions.append(pathfinder.get_last_step_count())
            else:
                self.successful_run_times.append(time_ns)
                self.successful_extensions.append(pathfinder.get_last_step_count())

    def get_nr_successful_runs(self):
        """
            Returns the number of successful runs.
        """
        return len(self.successful_run_times)	
    
    def get_nr_unsuccessful_runs(self):	
        """
            Returns the number of unsuccessful runs.
        """
        return len(self.unsucessful_run_times)	

    def get_average_time(self):	
        """
            Returns the average time taken for the runs in nanoseconds.
        """
        return sum(self.run_times) / len(self.run_times)

    def get_average_successful_time(self):
        """
            Returns the average time taken for the successful runs in nanoseconds.
        """
        return sum(self.successful_run_times) / len(self.successful_run_times)	

    def get_average_unsuccessful_time(self):
        """
            Returns the average time taken for the unsuccessful runs in nanoseconds.
        """
        return sum(self.unsucessful_run_times) / len(self.unsucessful_run_times)	


    def get_max_time(self):
        """
            Returns the maximum time taken for the runs in nanoseconds.
        """
        return max(self.run_times)

    def get_max_successful_time(self):	
        """
            Returns the maximum time taken for the successful runs in nanoseconds.
        """
        return max(self.successful_run_times)	
    
    def get_max_unsuccessful_time(self):	
        """
            Returns the maximum time taken for the unsuccessful runs in nanoseconds.
        """
        return max(self.unsucessful_run_times)	
    
    def get_min_time(self):
        """
            Returns the minimum time taken for the runs in nanoseconds.
        """
        return min(self.run_times)
    
    def get_min_successful_time(self):	
        """
            Returns the minimum time taken for the successful runs in nanoseconds.
        """
        return min(self.successful_run_times)	
    
    def get_min_unsuccessful_time(self):	
        """
            Returns the minimum time taken for the unsuccessful runs in nanoseconds.
        """
        return min(self.unsucessful_run_times)	
    
    def get_overall_time(self):
        """
            Returns the overall time taken for the runs in nanoseconds.
        """
        return sum(self.run_times)

    def get_overall_successful_time(self):	
        """
            Returns the overall time taken for the successful runs in nanoseconds.
        """
        return sum(self.successful_run_times)	
    
    def get_overall_unsuccessful_time(self):	
        """
            Returns the overall time taken for the unsuccessful runs in nanoseconds.
        """
        return sum(self.unsucessful_run_times)	

    def get_nr_extensions(self):
        """
            Returns the overall number of nodes extended
        """
        return sum(self.nr_extensions)
    
    def get_nr_successful_extensions(self):	
        """
            Returns the overall number of nodes extended in successful runs
        """
        return sum(self.successful_extensions)	
    
    def get_nr_unsuccessful_extensions(self):	
        """
            Returns the overall number of nodes extended in unsuccessful runs
        """
        return sum(self.unsuccesful_extensions)	

    def get_average_extension_time(self):
        """
            Returns the average time taken for one extension
        """
        return self.get_overall_time() / self.get_nr_extensions()
    
    def get_average_successful_extension_time(self):	
        """
            Returns the average time taken for one extension in successful runs
        """
        return self.get_overall_successful_time() / self.get_nr_successful_extensions()	
    
    def get_average_unsuccessful_extension_time(self):	
        """
            Returns the average time taken for one extension in unsuccessful runs
        """
        return self.get_overall_unsuccessful_time() / self.get_nr_unsuccessful_extensions()	