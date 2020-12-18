"""Trabajo Práctico Investigación Operativa 2020."""
import argparse
import logging
import pickle
from datetime import datetime

start_runtime = datetime.now()

logging.basicConfig(level=logging.DEBUG)

import numpy as np

from constants import DEFAULT_GRAPH, MICROAPPLE_GRAPH
from graph import Graph


def find_safest_paths(inputs=DEFAULT_GRAPH, source=0):
    """
    Creates a Graph instance with `inputs` and uses a version of Dijkstra
    to find the safest paths between `source` and all other nodes.

    Parameters
    ----------
    inputs : list of tuples
        All edges and their corresponding weights.
    source : int
        Source node from which packages will be sent.

    Returns
    -------
    List with paths to each node and distance.

    """
    log_inputs = [
        (a[0], a[1], -np.log(a[2]))
        for a in inputs
    ]
    log_graph = Graph()
    log_graph.add_edges_list(log_inputs)
    return log_graph.dijkstra(source)


if __name__ == "__main__":
    logging.info("Finding safest paths...")
    paths, distance = find_safest_paths(inputs=MICROAPPLE_GRAPH)
    for key in paths.keys():
        print(key, paths[key], distance[key])
    logging.info(f"Computation took: {datetime.now() - start_runtime}")
