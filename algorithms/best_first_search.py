
import numpy as np
from queue import PriorityQueue

from algorithms.informed_search_algorithm import Informed_Search_Algorithm

class Best_First_Search(Informed_Search_Algorithm):
    """
        Implementation of best first search with manhattan distance heuristic
    """

    def __init__(self, graph):
        super().__init__(graph)

    def search(self, start_index, end_index):
        """
            Perform a backtrack search from start_index to end_index.
            Returns a tuple consisting of
            - the path from start_index to end_index 
            - the distance of the path (as a tuple)
        """
        self.last_step_count = 0

        # used np array for fast lookup of closed list
        closed = np.zeros((self.graph.num_nodes), dtype=int)
        # use priority queue for visiting in order of path length
        open = PriorityQueue()
        open.put((self.heuristic_value(start_index,end_index), start_index, []))

        while not open.empty():
            self.last_step_count += 1
            current_distance, current, current_path = open.get()

            # found goal
            if current == end_index:
                return current_path, current_distance
            
            # seen this before with a shorter path -> can skip
            if closed.item(current) == True:
                continue
            np.put(closed, current, True)

            # add all neighbors to open list
            for neighbor, distance in self.graph.get_edges(current):
                if closed.item(neighbor) == False:
                    open.put((self.heuristic_value(neighbor, end_index), neighbor, current_path + [neighbor]))
                  
        return None, None
    