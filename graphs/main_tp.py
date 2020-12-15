"""Main."""
import pickle

import numpy as np

from constants import DEFAULT_GRAPH
from graph import Graph


def dijkstra(graph, source):

    queue = list(graph.vertices)
    dist = []
    prev = []
    visited = []


def find_safest_paths(inputs=DEFAULT_GRAPH, source=0):
    log_inputs = [
        # (a[1], a[2], 0) if a[2] == 1 else (a[0], a[1], -np.log(a[2]))
        (a[0], a[1], -np.log(a[2]))
        for a in inputs
    ]
    graph = Graph()
    log_graph = Graph()
    graph.add_edges_list(inputs)
    log_graph.add_edges_list(log_inputs)
    return log_graph.dijkstra(source)


if __name__ == "__main__":

    with open('/home/puff/git-repos/invop/graphs/data/microapple.input', 'rb') as f:
        datos_red = pickle.load(f)
        g = find_safest_paths(inputs=datos_red)
        print(g)
