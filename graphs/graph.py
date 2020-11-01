"""Graph class.
TODO: add support for inputs:
    dict of dicts,
    dict of lists,
    numpy.matrix,
    2d numpy ndarray,
    scipy sparse matrix

"""
from collections import defaultdict



class Graph:

    def __init__(self, edges, directed=False):
        self._dict = defaultdict(set)
        self.directed = directed
        self.size = len(self._dict.keys())
        self.add_edges(edges)

    def add_edges(self, edges):
        for n1, n2 in edges:
            self.add(n1, n2)

    def add(self, node_1, node_2):
        self.size += 1
        self._dict[self.size].update({node_1, node_2})


if __name__ == '__main__':
    g = Graph([[1, 2], [2, 3], [1, 3], [3, 4]])
    print(g._dict)
