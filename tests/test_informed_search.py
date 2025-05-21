import unittest
from algorithms.a_star import A_Star
from algorithms.breadth_first_search import Breadth_First_Search
from algorithms.depth_first_search import Depth_First_Search
from algorithms.dijkstra import Dijkstra
from evaluation.timed_experiment import Timed_Experiment
from graph.graph import Graph


class TestDataset(unittest.TestCase):
    """
        tests the dataset class
    """

    def setUp(self):
        self.graph = Graph()
        
        self.graph.add_edge(0, 1)
        self.graph.add_edge(1, 2)
        self.graph.add_edge(2, 3)
        self.graph.add_edge(0, 4)
        self.graph.add_edge(0, 5)
        self.graph.add_edge(0, 6)
        self.graph.convert_to_spatial([
            [0,0],
            [1,0],
            [2,0],
            [3,0],
            [0,1],
            [-1,0],
            [0,-1]
        ])

        self.graph



    def test_dijkstra(self):
        """
            test interaction between dataset download and check for downloading
        """
        dijkstra = Dijkstra(self.graph)

        # case 1: path can be found        
        path, distance = dijkstra.search(0, 3)
        assert path == [1, 2,3]
        assert dijkstra.get_last_step_count() == 7
        
        # case 2: path cannot be found
        path, distance = dijkstra.search(3, 0)
        assert path == None
        assert distance == None
        
        


    def test_A_Star(self):
        """
            test interaction between dataset download and check for downloading
        """
        a_star = A_Star(self.graph)

    	 # case 1: path can be found        
        path, distance = a_star.search(0, 3)
        assert path == [1, 2,3]
        assert a_star.get_last_step_count() == 4
        
        # case 2: path cannot be found
        path, distance = a_star.search(3, 0)
        assert path == None
        assert distance == None

