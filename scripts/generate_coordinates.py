"""
    This script generates the coordinate files for the dataset and stores them in data/coordinates.
    Files are stored as pickle files. Their content is a list of coordinates, indexed by node index.

    Since this script is not in the main folder, it needs to be called as a module to resolve it's dependencies.
    Call it with: python -m scripts.generate_coordinates.
"""

import pickle
import time
import os
print(os.getcwd())

import igraph as ig
import data.dataset

print(os.getcwd())

def generate_coordinates(layout_name):
    """
    Generates the coordinates for the graph and stores them in a pickle file.
    :param layout: The layout of the graph.
    :return: None
    """
    dataset = data.dataset.Dataset()
    graph = dataset.load_graph()
    edges = graph.get_edge_tuples()

    g = ig.Graph(edges=edges, directed = True);
    layout = g.layout(layout=layout_name)

    with open(f"data/coordinates/if_{layout_name}.pickle", "wb") as f:
        pickle.dump(layout.coords, f) 


if __name__ == "__main__":

    layouts = ["auto", "star", "circle", "grid"]

    for layout_name in layouts:
        print("Generating layout for ", layout_name)
        print("This may take a while...")
        start = time.time_ns()
        generate_coordinates(layout_name);
        end = time.time_ns()
        print("Layout generated in ", (end - start) / 1e9, " seconds")