
import numpy as np
import heapq


class Search_Algorithm:
    """
        Base class for all search algorithms
    """

    def __init__(self, graph):
        self.graph = graph
        self.last_step_count = 0


    def get_last_step_count(self):
        """
            Returns the number of steps taken in the last search. 
            This corresponds to the number of nodes that have been expanded.
        """
        return self.last_step_count


    def search(self, start_index, end_index):
            """
                Perform the search.
                This function should be implemented by all children.
            """
            raise NotImplementedError("This method should be overridden by subclasses")