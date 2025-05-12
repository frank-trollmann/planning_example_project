from graph.graph import Graph

import os
import pickle
from urllib.request import urlretrieve
from pathlib import Path
import gzip



class Dataset:
    """
        This class is a convenience wrapper for dataset functions. It taks care of interaction with the file system and downloading the dataset.
    """

    def __init__(self, test_mode = False):
        """
            constructor. 
            If test_case is true, this will use different folders so unit tests don't interfere with any downloaded data.
        """
        self.FILE_NAME = "dataset.txt.gz"

        if test_mode:
            self.FILE_DIR = "data/download/test/"
        else:
            self.FILE_DIR = "data/download/"

 
    def download(self) -> None:
        """ 
            download the dataset from stanford and unzip it to data/dataset
        """
        try:

            # make directory if not exists
            from pathlib import Path
            Path(self.FILE_DIR).mkdir(parents=True, exist_ok=True)
            
            url = "https://snap.stanford.edu/data/email-EuAll.txt.gz"
            urlretrieve(url, self.FILE_DIR + self.FILE_NAME)
        except:
            print("Error downloading the dataset. Please check your internet connection or the URL.")

    def is_downloaded(self) -> bool:
        """ 
            checks if the data alread has been downloaded 
        """

        return os.path.exists(self.FILE_DIR + self.FILE_NAME)

    def remove_all(self) -> None:
        """ 
            removes all files associated with this dataset from the computer
        """

        if os.path.exists(self.FILE_DIR + self.FILE_NAME):
            os.remove(self.FILE_DIR + self.FILE_NAME)

    def load_graph(self) -> Graph:
        """ 
            loads the graph from the dataset file 
            This will automatically download the file if it is not already downloaded.    
        """

        if not self.is_downloaded():
            self.download();

        # open the file
        with gzip.open(self.FILE_DIR + self.FILE_NAME, 'rt') as f:
            lines = f.readlines()

        # create a graph
        graph = Graph()

        # parse the lines
        for line in lines:
            if line.startswith("#"):
                continue
            
            from_index, to_index = map(int, line.split())
            graph.add_edge(from_index, to_index)

        return graph
    
    def add_node_positions(self, graph, type):
        """
            loads the node positions from a pickle file and attaches them to the graph.
            The file should contain a list of coordinates, indexed by node index.
        """
        file_name = f"data/coordinates/{type}.pickle"
        with open(file_name, "rb") as f:
            node_positions = pickle.load(f)
            graph.add_node_positions(node_positions)
