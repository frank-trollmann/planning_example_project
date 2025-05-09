

class Graph:
    """
        Graph representation for this example.

        Assumptions: 
        - nodes are represented by their id and have no other content.
        - edges are directed and unweighted.
    """
    def __init__(self): 
        self.adjacency_list = []
        self.num_nodes = 0
        self.num_edges = 0

    def add_edge(self, from_index, to_index):
        """ 
            adds an edge to the graph 
        """
        while from_index >= len(self.adjacency_list):
            self.adjacency_list.append([])
            self.num_nodes += 1

        self.adjacency_list[from_index].append(to_index)
        self.num_edges += 1

    def get_edges(self,from_index):
        """ 
            returns the adjacency list of a node.
        """
        return self.adjacency_list[from_index]
    
    def print_graph(self):
        """ 
            prints the graph to command line.
        """
        for index in range(len(self.adjacency_list)):
            print(f"{index}: {self.adjacency_list[index]}")