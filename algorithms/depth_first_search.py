
from queue import LifoQueue
from collections import deque
import numpy as np


class Depth_First_Search:



    def __init__(self, graph):
        self.graph = graph
        self.last_step_count = 0;


    def get_last_step_count(self):
        """
            Returns the number of steps taken in the last search. 
            This corresponds to the number of nodes that have been expanded.
        """
        return self.last_step_count;

    def search(self, start_index, end_index):
        """
            Perform a backtrack search from start_index to end_index.
            Returns a tuple consisting of
            - the path from start_index to end_index 
            - the distance of the path (as a tuple)
        """

        # seen denotes which nodes have aleady been seen. For efficient lookup we use numpy arrays.
        seen = np.zeros((self.graph.num_nodes), dtype=bool)
        open = deque()
        self.last_step_count = 0;

        open.append((start_index,0,[]))

        while len(open) > 0:
            self.last_step_count += 1
            current, current_distance, current_path = open.pop()
            
            if current == end_index:
                return current_path, current_distance

            for neighbor, distance in self.graph.get_edges(current):
                
                if seen.item(neighbor) == False:
                    open.append((neighbor, current_distance + distance, current_path + [neighbor]))
                    np.put(seen, neighbor, True)
                  
        return None, None




    