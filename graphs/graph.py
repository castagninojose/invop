"""Graph class."""
import numpy as np


class Graph:
    def __init__(self):  # Crea un grafo vacio
        self.adj_dict = {}
        self.vertices = set()

    def add_vertex(self, vertex):
        self.vertices.add(vertex)

    def get_size(self):
        return len(self.vertices)

    def weighted_neighbors(self, vertex):
        if vertex not in self.adj_dict:
            return set()
        else:
            return self.adj_dict[vertex]

    def neighbors(self, vertex):
        if vertex not in self.adj_dict:
            return set()
        else:
            return {u[0] for u in self.adj_dict[vertex]}

    def add_edge(self, edge):  # edge = (u,v,peso) dirigida
        weight = 1
        if len(edge) == 3:
            source, target, weight = edge
        elif len(edge) == 2:
            source, target = edge
        else:
            print("Invalid use. Edges should be [source, target, weight]")
        self.vertices.add(source)
        self.vertices.add(target)
        if source not in self.adj_dict:
            self.adj_dict[source] = set()
        self.adj_dict[source].add((target, weight))

    def add_edges_list(self, edges_list):
        for edge in edges_list:
            self.add_edge(edge)

    def bfs_search(self, root):
        queue = [root]
        visited = [False] * self.get_size()
        visited[root] = True
        while queue:
            node = queue.pop(0)
            for n in self.neighbors(node):
                if not visited[n]:
                    queue.append(n)
                    visited[n] = True

    def dijkstra(self, root):
        print(root)
        queue = [root]
        visited = [False] * self.get_size()
        distances = [np.inf] * self.get_size()
        distances[root] = 0
        paths = {n: [0] for n in self.adj_dict.keys()}
        while queue:
            aux = np.array(distances)
            aux[visited] = np.inf
            node = np.argmin(aux)
            queue.remove(node)
            visited[node] = True
            for neighbor in self.neighbors(node):
                if not visited[neighbor]:
                    if neighbor not in queue:
                        queue.append(neighbor)
                    neighbor_distance = dict(self.adj_dict[node])[neighbor]
                    if distances[neighbor] > distances[node] + neighbor_distance:
                        distances[neighbor] = distances[node] + neighbor_distance
                        paths[neighbor] = paths[node] + [neighbor]
        distances[node] = (
            distances[paths[node][-2]] + dict(self.adj_dict[paths[node][-2]])[node]
        )
        return paths, np.exp(-np.array(distances))


if __name__ == "__main__":
    g = Graph()


# from collections import defaultdict


# class Graph:
#     def __init__(self, edges, directed=False):
#         self._dict = defaultdict(set)
#         self._directed = directed
#         self.add_edges(edges)

#     def add_edges(self, edges):
#         for n1, n2 in edges:
#             self.add(n1, n2)

#     def add(self, node_1, node_2):
#         if {node_1, node_2} in self._dict.values():
#             pass
#         else:
#             self._dict[self.size].update({node_1, node_2})

#     @property
#     def nodes(self):
#         return set.union(*self._dict.values())

#     @property
#     def size(self):
#         return len(self._dict.keys())
