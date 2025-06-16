import numpy as np
import heapq

from algorithms.informed_search_algorithm import Informed_Search_Algorithm

class A_Star(Informed_Search_Algorithm):
    """
        Implementation of the A* algorithm with manhattan distance heuristic
    """

    def __init__(self, graph):
        super().__init__(graph)

    def search(self, start_index, end_index):
            """
                Perform A* search search from start_index to end_index.
                Returns a tuple consisting of
                - the path from start_index to end_index 
                - the distance of the path (as a tuple)
            """
            self.last_step_count = 0
            closed = np.zeros((self.graph.num_nodes), dtype=int)
            distances = np.full((self.graph.num_nodes), -1, dtype=float)
            open = []

            heapq.heappush(open,(0, start_index, []))
            distances[start_index] = 0

            while not len(open) == 0:
                _ , current, current_path = heapq.heappop(open)	
                current_distance = distances[current]

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
                    known_distance = distances[neighbor]
                    
                    if known_distance < 0 or known_distance > new_distance:
                        h = self.heuristic_value(neighbor, end_index)
                        heapq.heappush(open,(new_distance + h, neighbor, current_path + [neighbor]))
                        distances[neighbor] = new_distance
                    
            return None, None
