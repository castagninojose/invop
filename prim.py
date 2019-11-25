import numpy as np

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

    def generate_edges(self):
        rv = set()
        for i in self.adyacencias.items():
            aristas_i = [frozenset([i[0], j]) for j in i[1]]
            rv = rv.union(aristas_i)
        return rv

grafo = Grafo(DEFAULT_WEIGHT_MATRIX_1)

def ix_min(key, vis_l):
    
    k_array = np.array(key)
    k_array[vis_l] = np.inf
    return np.argmin(k_array)


def prim(grafo):
    n = 7
    visitados = [False] * n
    key = [np.inf] * n
    parents = [-1] * n
    key[0] = 0
    rv = set()
    while sum(visitados) < n:
        ix = ix_min(key, visitados)
        print(f'indice: {ix}')
        visitados[ix] = True
        vecinos_ix = grafo.vecinos(ix)
        if ix != 0:
            vecino_mas_cercano = grafo.adj_m[ix].argmin()
            rv = rv.union({ix,vecino_mas_cercano})
        breakpoint()
        for j in vecinos_ix:
            if not visitados[j]:
                if key[j] > grafo.adj_m[ix, j]:
                    key[j] = grafo.adj_m[ix, j]
                    parents[j] = [ix, j]

    return rv


# costo = [np.inf, np.inf, np.inf ,np.inf, np.inf, np.inf, np.inf]
# previo = [np.nan, np.nan, np.nan ,np.nan, np.nan, np.nan, np.nan]

# vertice_cero = 'a'

if __name__ == "__main__":
    print(prim(grafo))

    # grafo.adyacencias(1)