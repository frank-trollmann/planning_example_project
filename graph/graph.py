
import pickle
from collections import deque

class Graph:
    """
        Graph representation for directed weighted graphs.

        Assumptions: 
        - nodes are represented by their id and have no other content.
        - edges are directed and weighted.

        Graphs can also be extended with positions. For this purpose, call add_node_positions

    """
    def __init__(self): 
        self.adjacency_list = []
        self.node_positions = None
        self.num_nodes = 0
        self.num_edges = 0

    def add_edge(self, from_index, to_index, weight = 1):
        """ 
            adds an edge to the graph 
        """
        while max(from_index,to_index) >= len(self.adjacency_list):
            self.adjacency_list.append([])
            self.num_nodes += 1

        self.adjacency_list[from_index].append((to_index,weight))
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

    def add_node_positions(self, node_positions):
        """
            can be used to set positions for nodes after the fact
        """
        self.node_positions = node_positions

    def get_node_position(self, node_index):
        """
            returns the position of a node.
            If no positions are loaded, returns None.
        """
        if self.node_positions is None:
            return None
        return self.node_positions[node_index]



    def get_edge_tuples(self):
        """ 
            returns edges of the graph as a list of tuples.
            This can be used for compatibility with graph visualization libraries.
        """
        
        edges = []
        for source in range(len(self.adjacency_list)):
            for target, _ in self.adjacency_list[source]:
                edges.append((source, target))
        return edges