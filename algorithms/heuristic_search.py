
from collections import deque
import numpy as np


class Heuristic_Search:



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

            for neighbor, distance in sorted(self.graph.get_edges(current), key = lambda edge: self.heuristic_value(edge[0],end_index), reverse=True):	
                
                if seen.item(neighbor) == False:
                    open.append((neighbor, current_distance + distance, current_path + [neighbor]))
                    np.put(seen, neighbor, True)
                  
        return None, None
 


    def heuristic_value(self, start_index, end_index):
        """
            Returns the heuristic value of a node.
            This is the distance from the node to the end node.
        """
        start_position = self.graph.get_node_position(start_index)
        end_position = self.graph.get_node_position(end_index)

        if start_position is None or end_position is None:
            return 0;

        source_x = start_position[0]
        source_y = start_position[1]
        target_x = end_position[0]
        target_y = end_position[1]

        return abs(source_x - target_x) + abs(source_y - target_y)

    