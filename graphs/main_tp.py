"""Main."""
import numpy as np
from graph import Graph
from constants import DEFAULT_GRAPH


def dijkstra(graph, source):

    queue = list(graph.vertices)
    dist = []
    prev = []
    visited = []



def find_safest_paths(inputs=0, source=0):
    inputs = [
        (0, 1, 0.9),
        (0, 2, 0.95),
        (1, 2, 0.8),
        (1, 3, 0.9),
        (3, 1, 0.99),
        (2, 3, 0.85),
        (0, 3, 1),
    ]
    log_inputs = [
        (a[0], a[1], -np.log(1 - a[2])) if a[2] != 1 else (a[1], a[2], 0)
        for a in inputs
    ]
    breakpoint()
    graph = Graph()
    graph.add_edges_list(inputs)

    return log_inputs


if __name__ == "__main__":
    g = find_safest_paths()
    print(g.adj_dict)
    breakpoint()
