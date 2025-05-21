
import numpy as np
from queue import PriorityQueue
from graph.graph import Graph
import heapdict 
from queue import PriorityQueue


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
            distances = np.full((self.graph.num_nodes), -1, dtype=float)
            # use priority queue for visiting in order of path length
            open = PriorityQueue()
            open.put((0, 0, start_index, []))
            distances[start_index] = 0

            while not open.empty():
                _, current_distanceX , current, current_path = open.get()
                current_distance = distances[current];

                # seen this before with a shorter path -> can skip
                if closed[current] == True:
                    continue
                np.put(closed, current, True)

                self.last_step_count += 1

                # found goal
                if current == end_index:
                    return current_path, current_distance

                # add all neighbors to open list
                for neighbor, distance in self.graph.get_edges(current):
                    if closed.item(neighbor) == True:
                        continue
                    new_distance = current_distance + distance
                    known_distance = distances[neighbor];
                    
                    if known_distance < 0 or known_distance > new_distance:
                        h = self.heuristic_value(neighbor, end_index)
                        open.put((new_distance + h, new_distance, neighbor, current_path + [neighbor]))
                        distances[neighbor] = new_distance
                    
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




    