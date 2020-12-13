"""Main."""
import numpy as np
from graph import Graph
from constants import DEFAULT_GRAPH


def dijkstra(graph, source):

    queue = list(graph.vertices)
    dist = []
    prev = []
    visited = []



def find_safest_paths(inputs=DEFAULT_GRAPH, source=0):
    log_inputs = [
        (a[0], a[1], -np.log(1 - a[2])) if a[2] != 1 else (a[1], a[2], 0)
        for a in inputs
    ]
    graph = Graph()
    log_graph = Graph()
    graph.add_edges_list(inputs)
    log_graph.add_edges_list(log_inputs)

    return graph.bfs_search(source)


if __name__ == "__main__":
    g = find_safest_paths()
    breakpoint()
