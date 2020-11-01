"""Graph class.
TODO: add support for inputs:
    dict of dicts,
    dict of lists,
    numpy.matrix,
    2d numpy ndarray,
    scipy sparse matrix

"""
class Graph:

    def __init__(self, edges, directed=False):
        self._dict = defaultdict(set)
        self.directed = directed
        self.add_edges(edges)

    def add_edges(self, edges):
        for n1, n2 in edges:
            self.add(n1, n2)

    def add(node_1, node_2):
        self._dict[node_1] = node_2


if __name__ == '__main__':
    g = Graph({0: {1, 2}, 1: {2, 3}, 2: {1, 3}, 3: {3, 4}})
    breakpoint()
    print(g.edges)
    print(g.nodes)