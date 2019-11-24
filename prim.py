import numpy as np
import pandas as pd

from collections import defaultdict

DEFAULT_WEIGHT_MATRIX_1 = np.matrix(
    [[np.inf, 2, 3, 3, np.inf,np.inf,np.inf],
    [2, np.inf, 4, np.inf, 3, np.inf, np.inf],
    [3, 4, np.inf, 5, 1, 6, np.inf],
    [3, np.inf, 5, np.inf, np.inf, 7, np.inf],
    [np.inf, np.inf,1, np.inf, np.inf, 8, np.inf],
    [np.inf, np.inf, 6, 7, 8, np.inf, 9],
    [np.inf, np.inf, np.inf ,np.inf, np.inf, 9, np.inf]]
)


class Grafo:
    
    def __init__(self, adj_m=[]):
        self.adj_m = adj_m
        self.vertices = np.arange(self.adj_m.shape[1])
        self.adyacencias = {v : self.vecinos(v) for v in self.vertices}
        # self.aristas = [(v, self.vecinos(v)) for v in self.vertices]

    def vecinos(self, j):
        aristas_finitas = self.adj_m[j,:] < np.inf
        vecinos_lista = np.where(aristas_finitas.tolist())[1]
        return vecinos_lista

    def generate_weights(self):
        rv = set()
        for i in self.adyacencias.items():
            aristas_i = [frozenset([i[0], j]) for j in i[1]]
            rv = rv.union(aristas_i)
        return rv

grafo = Grafo(DEFAULT_WEIGHT_MATRIX_1)

def prim(grafo, pesos=None):
    no_visitados_list = list(grafo.vertices)
    n = len(no_visitados_list)
    g = [np.inf] * n
    g[0] = 0
    dist_vecinos = []
    rv = []
    e = grafo.generate_weights()
    while len(no_visitados_list) > 0:
        ix = np.argmin(g)
        no_visitados_list.remove(ix)
        if ix != 0:
            vecinos_ix = grafo.vecinos(ix)
            dist_vecinos = [grafo.adj_m[ixgenerate_weights]]
            rv.append(grafo.vecinos(ix))
            ## cambiar usando e  arbol.vertices.append(grafo.vertices[ix])
        # adyacencias_ix = grafo.adyacencias[ix]
        # aristas_no_visitadas = [*set(adyacencias_ix) - set(visitados), ]


        breakpoint()
        for j in no_visitados_list:
            if g[j] > grafo.adj_m[ix, j]:
                g[j] = grafo.adj_m[ix, j]
                dist_vecinos[j] = [ix, j]

        return rv


# costo = [np.inf, np.inf, np.inf ,np.inf, np.inf, np.inf, np.inf]
# previo = [np.nan, np.nan, np.nan ,np.nan, np.nan, np.nan, np.nan]

# vertice_cero = 'a'

if __name__ == "__main__":
    prim(grafo)
    # grafo.adyacencias(1)