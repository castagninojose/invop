"""Graph class.
posible inputs:
    [ x ] dict of sets,
    [ ] np.ndarray / np.matrix,
    [ ] sp.sparse,
    [ ] dict of dicts,
    [ ] dict of lists

"""
from collections import defaultdict


class Graph:

    def __init__(self, edges, directed=False):
        self._dict = defaultdict(set)
        self._directed = directed
        self.add_edges(edges)

    def add_edges(self, edges):
        for n1, n2 in edges:
            self.add(n1, n2)

    def add(self, node_1, node_2):
        self._dict[self.size].update({node_1, node_2})

    @property
    def nodes(self):
        return set.union(*self._dict.values())
    
    @property
    def size(self):
        return len(self._dict.keys())


if __name__ == '__main__':
    g = Graph([[1, 2], [2, 3], [1, 3], [3, 4]])
    g.add('puff', 1)
    print(g._dict)
    print(g.size)
    print(g.nodes)
