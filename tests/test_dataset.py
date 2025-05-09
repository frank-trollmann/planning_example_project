import unittest
from data.dataset import Dataset


class TestDataset(unittest.TestCase):
    """
        tests the dataset class
    """

    def setUp(self):
        self.dataset = Dataset(test_mode = True)


    def test_download_and_remove(self):
        """
            test interaction between dataset download and check for downloading
        """
        # before download, dataset should not contain 
        assert self.dataset.is_downloaded() == False

        # check that after download data and images are available
        self.dataset.download()
        assert self.dataset.is_downloaded() == True

        # check that downloaded data has content
        graph = self.dataset.load_graph();
        assert graph is not None	
        assert graph.num_nodes > 0	
        assert graph.num_edges > 0	

        # check that remove_all correctly cleans this data
        self.dataset.remove_all()
        assert self.dataset.is_downloaded() == False


    def test_correct_content(self):
        # before download, dataset should not contain 
        assert self.dataset.is_downloaded() == False

         # check that downloaded data has content
        graph = self.dataset.load_graph();
        assert graph is not None	
        assert graph.num_nodes > 0	
        assert graph.num_edges > 0	

        # check if automatic download works
        assert self.dataset.is_downloaded() == True

        # check that remove_all correctly cleans this data
        self.dataset.remove_all()
        assert self.dataset.is_downloaded() == False

    def tearDown(self):
        self.dataset.remove_all()

