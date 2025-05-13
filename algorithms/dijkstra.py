
import numpy as np
from queue import PriorityQueue
from graph.graph import Graph


class Dijkstra:



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
        open.put((0, start_index, []))

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
                    open.put((current_distance + distance, neighbor, current_path + [neighbor]))
                  
        return None, None




    