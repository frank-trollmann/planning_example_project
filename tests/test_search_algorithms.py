import unittest
from algorithms.breadth_first_search import BreadthFirstSearch
from algorithms.depth_first_search import DepthFirstSearch
from evaluation.TimedExperiment import Timed_Experiment
from graph.graph import Graph


class TestDataset(unittest.TestCase):
    """
        tests the dataset class
    """

    def setUp(self):
        self.graph = Graph()
        self.graph.add_edge(0, 1)
        self.graph.add_edge(1, 2)
        self.graph.add_edge(0, 3)


    def test_bfs(self):
        """
            test interaction between dataset download and check for downloading
        """
        bfs = BreadthFirstSearch(self.graph)

        # case 1: path can be found        
        path, distance = bfs.search(0, 2)
        assert path == [1, 2]
        assert distance == 2
        
        # case 2: path cannot be found
        path, distance = bfs.search(1, 3)
        assert path == None
        assert distance == None
        
        


    def test_dfs(self):
        """
            test interaction between dataset download and check for downloading
        """
        dfs = DepthFirstSearch(self.graph)

        # case 1: path can be found        
        path, distance = dfs.search(0, 2)
        assert path == [1, 2]
        assert distance == 2
        
        # case 2: path cannot be found
        path, distance = dfs.search(1, 3)
        assert path == None
        assert distance == None


    def test_timed_experiment(self):
        """
            test that timed experiment works and runs the correct number of times.
        """
        experiment = Timed_Experiment(self.graph, BreadthFirstSearch, 10, random_seed=42)
        experiment.run()
        assert len(experiment.run_times) == 10

    def tearDown(self):
        pass

