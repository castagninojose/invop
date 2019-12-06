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

def edge_dict_from_matrix(w_m):
    # devuelve un diccionario de aristas a partir de una matriz de pesos
    n = w_m.shape[1]
    rv = []
    for i in range(n):
        for k in range(n):
            if w_m[i,k] < np.inf:
                rv.append((i,k))
    
    return {i : rv[i] for i in range(len(rv))}

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
            rv.append([parents[ix], ix])

        vecinos_ix = vecinos(G, ix)
        for jx in vecinos_ix:
            if not visitados[jx]:
                if key[jx] > G[ix, jx]:
                    key[jx] = G[ix, jx]
                    parents[jx] = ix
    
    weights_rv = sum([grafo.adj_m[l[0]][l[1]] for l in rv])
    return rv , weights_rv

def edges_dict(G):
    # generar diccionario con los ejes como keys y los valores de G como value
    rv = {}
    for i in range(len(G)):
        rv.update({(i, j): G[i, j] for j in range(len(G)) if j != i})
    return rv


def path_from_predecessor_vector(p, i, j):
    # reconstruir camino a de i a j a partir de un vector predecesor
    pass

def path_from_predecessor_matrix(p, i, j):
    pass

def bellman_ford(G, source):
    # init
    n = len(G)
    aristas_d = edges_dict(G)
    dist_l = [float('Inf')] * n
    predecessor = [-1] * n
    dist_l[source] = 0
    # relax
    for i in range(n-1):
        for e in aristas_d.keys():
            if (dist_l[e[1]] > dist_l[e[0]] + aristas_d[e]):
                dist_l[e[1]] = dist_l[e[0]] + aristas_d[e]
                predecessor[e[1]] = e[0]
    
    # now look for negative weight cycles
    for e in aristas_d:
        if (dist_l[e[1]] != float('Inf') and dist_l[e[1]] > dist_l[e[0]]):
            print(f"Existe ciclo negativo p: {predecessor}")
            
    return dist_l, predecessor






if __name__ == "__main__":
    print(edges_dict(WEIGHT_MATRIX_1))
    print(edge_dict_from_matrix(WEIGHT_MATRIX_1))
    # print(bellman_ford(CURRENCY_MATRIX, 1))
    # print(monet_arbit(-np.log(CURRENCY_MATRIX)))
