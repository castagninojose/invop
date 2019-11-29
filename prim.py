import numpy as np

from collections import defaultdict

from constants import WEIGHT_MATRIX_1

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

grafo = Grafo(WEIGHT_MATRIX_1)

def ix_min(key, vis_l):
    
    k_array = np.array(key)
    k_array[vis_l] = np.inf
    return np.argmin(k_array)

def vecino_mas_cercano(dist_row, vis_l):
    dist_r = dist_row.copy()
    dist_r[:,vis_l] = np.inf
    return dist_r.argmin()


def prim(G):
    grafo = Grafo(G)
    n = len(grafo.vertices)
    visitados = np.array([False] * n)
    key = np.array([np.inf] * n)
    parents = np.array([-1] * n)
    key[0] = 0
    rv = []
    weights_rv = 0
    while sum(visitados) < (n-1):
        ix = ix_min(key, visitados)
        visitados[ix] = True
        if ix != 0:
            vmc = vecino_mas_cercano(grafo.adj_m[ix], visitados)
            rv.append([ix, vmc])
            parents[ix] = vmc
            weights_rv = weights_rv + grafo.adj_m[ix, vmc]
            
        breakpoint () 
        vecinos_ix = grafo.vecinos(ix)
        for jh in vecinos_ix:
            if not visitados[jh]:
                if key[jh] > grafo.adj_m[ix, jh]: 
                    key[jh] = grafo.adj_m[ix, jh]
                    parents[jh] = jh

    rv.insert(0, [0, rv[0][0]])
    weights_rv = weights_rv + grafo.adj_m[ix, np.argmin(visitados)]

    return rv , weights_rv


# costo = [np.inf, np.inf, np.inf ,np.inf, np.inf, np.inf, np.inf]
# previo = [np.nan, np.nan, np.nan ,np.nan, np.nan, np.nan, np.nan]

# vertice_cero = 'a'

if __name__ == "__main__":
    print(prim(WEIGHT_MATRIX_1))
