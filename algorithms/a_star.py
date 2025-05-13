
import numpy as np
from queue import PriorityQueue
from graph.graph import Graph


class A_Star:



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
        self.last_step_count = 0;

        # used np array for fast lookup of closed list
        closed = np.zeros((self.graph.num_nodes), dtype=int)
        # use priority queue for visiting in order of path length
        open = PriorityQueue()
        heuristic_value = self.heuristic_value(start_index, end_index)
        open.put((heuristic_value, start_index, 0, []))

        while not open.empty():
            self.last_step_count += 1
            _, current_index, current_distance, current_path = open.get()

            # found goal
            if current_index == end_index:
                return current_path, current_distance
            
            # seen this before with a shorter path -> can skip
            if closed.item(current_index) == True:
                continue
            np.put(closed, current_index, True)

            # add all neighbors to open list
            for neighbor, distance in self.graph.get_edges(current_index):
                if closed.item(neighbor) == False:
                    new_distance = current_distance + distance
                    new_heuristic = new_distance + self.heuristic_value(neighbor, end_index)
                    open.put((new_heuristic, neighbor, new_distance, current_path + [neighbor]))
                  
        return None, None
    

    def heuristic_value(self, start_index, end_index):
        """
            Returns the heuristic value of a node.
            This is the distance from the node to the end node.
        """
        source_x = self.graph.get_node_position(start_index)[0]
        source_y = self.graph.get_node_position(start_index)[1]
        target_x = self.graph.get_node_position(end_index)[0]
        target_y = self.graph.get_node_position(end_index)[1]

        return ((source_x - target_x) ** 2 + (source_y - target_y) ** 2) ** 0.5




    