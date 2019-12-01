import numpy as np

from collections import defaultdict

from constants import WEIGHT_MATRIX_1, CURRENCY_MATRIX, PAISES_DICT


class Grafo:
    
    def __init__(self, adj_m=[]):
        self.adj_m = adj_m
        self.vertices = np.arange(self.adj_m.shape[1])

    def adyacencias(self):
        return {v : self.vecinos(v) for v in self.vertices}

    def vecinos(self, j):
        aristas_finitas = self.adj_m[j,:] < np.inf
        vecinos_lista = np.where(aristas_finitas.tolist())[0]
        return vecinos_lista

    def generate_edges(self):
        rv = set()
        for i in self.adyacencias().items():
            aristas_i = [frozenset([i[0], j]) for j in i[1]]
            rv = rv.union(aristas_i)
        return rv

grafo = Grafo(WEIGHT_MATRIX_1)
grafo.generate_edges()

def vecinos(G, v):
    aristas_finitas = G[v,:] < np.inf
    vecinos_lista = np.where(aristas_finitas.tolist())[0]
    return vecinos_lista

def ix_min(key, vis_l):
    k_array = np.array(key)
    k_array[vis_l] = np.inf
    return np.argmin(k_array)

def prim(G):
    n = len(G)
    visitados = np.array([False] * n)
    key = np.array([np.inf] * n)
    parents = np.array([0] * n)
    key[0] = 0
    rv = []
    weights_rv = 0
    while sum(visitados) < (n):
        ix = ix_min(key, visitados)
        visitados[ix] = True
        if ix != 0:
            # vmc = vecino_mas_cercano(grafo.adj_m[ix], visitados)
            rv.append([parents[ix], ix])
            # parents[vmc] = ix
            # weights_rv = weights_rv + grafo.adj_m[parents[ix], ix]

        vecinos_ix = vecinos(G, ix)
        for jx in vecinos_ix:
            if not visitados[jx]:
                if key[jx] > G[ix, jx]:
                    key[jx] = G[ix, jx]
                    parents[jx] = ix

            
    # rv.insert(0, [0, rv[0][0]])
    # weights_rv = weights_rv + grafo.adj_m[ix, np.argmin(visitados)]
    
    weights_rv = sum([grafo.adj_m[l[0]][l[1]] for l in rv])
    return rv , weights_rv

def edges_dict(G):
    rv = {}
    for i in range(len(G)):
        rv.update({(i, j): G[i, j] for j in range(len(G)) if j != i})
    return rv

def bellman_ford(G, source):
    # init
    n = len(G)
    aristas_d = edges_dict(G)
    d = [float('Inf')] * n
    p = [-1] * n
    d[source] = 0

    # relax
    for i in range(n-1):
        for e in aristas_d.keys():
            if (d[e[0]] > d[e[1]] + aristas_d[e]):
                d[e[1]] = d[e[0]] + aristas_d[e]
                p[e[1]] = e[0]
    
    for e in aristas_d:
        if (d[e[1]] != float('Inf') and d[e[1]] > d[e[0]]):
            print(f"Existe ciclo negativo entre {e[0]} y {e[1]}.")
    return d, p


if __name__ == "__main__":
    print(bellman_ford(-np.log(CURRENCY_MATRIX), 1))
