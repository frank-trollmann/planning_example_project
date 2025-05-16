
import numpy as np
import heapdict 
from queue import PriorityQueue



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

        # storage for closed items, path tracking (to reconstruct path in the end) and shortest distances.
        closed = np.zeros((self.graph.num_nodes), dtype=int)
        previous = np.full((self.graph.num_nodes), -1, dtype=int)
        open = heapdict.heapdict();

        # use priority queue for visiting in order of path length
        open[start_index] = 0

        while len(open) > 0:
            self.last_step_count += 1
            current_node_index, current_distance = open.popitem()

            # found goal
            if current_node_index == end_index:
                return self.reconstruct_path(previous, start_index, end_index), current_distance
            
            # seen this before with a shorter path -> can skip
            # this should not happen
            if closed.item(current_node_index) == True:
                continue
            
            # mark as closed
            np.put(closed, current_node_index, True)

            # visit all neighbors
            for neighbor, distance in self.graph.get_edges(current_node_index):
                if closed.item(neighbor) == True:
                    continue
                new_distance = current_distance + distance
                known_distance = open.get(neighbor)

                if known_distance is None or known_distance > new_distance:
                    open[neighbor] = new_distance
                    np.put(previous, neighbor, current_node_index)

                  
        return None, None

    def reconstruct_path(self, previous, start_index, end_index):
        """
            Reconstruct the path from start_index to end_index using the previous array.
            Returns a list of nodes in the path.
        """
        path = []
        current = end_index
        while current != start_index:
            path.append(current)
            current =  previous.item(current)
        path.reverse()
        return path


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


        