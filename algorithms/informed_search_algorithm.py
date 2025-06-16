
from algorithms.search_algorithm import Search_Algorithm

class Informed_Search_Algorithm(Search_Algorithm):  
    """
        Parent class for all informed search algorithms.
        this class implements a common heuristic
    """

    def __init__(self, graph):
        super().__init__(graph)

    def heuristic_value(self, start_index, end_index):
        """
            Returns the heuristic value of a node.
            This is the distance from the node to the end node.
        """
        start_position = self.graph.get_node_position(start_index)
        end_position = self.graph.get_node_position(end_index)

        if start_position is None or end_position is None:
            return 0

        source_x = start_position[0]
        source_y = start_position[1]
        target_x = end_position[0]
        target_y = end_position[1]

        return abs(source_x - target_x) + abs(source_y - target_y)




    