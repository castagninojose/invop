import numpy as np

from collections import defaultdict

from constants import WEIGHT_MATRIX_1, CURRENCY_MATRIX, PAISES_DICT, EJ_4_21_CURRENCY_M, aver


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


def edges_dict(G):
    # generar diccionario con los ejes como keys y los valores de G como value
    rv = {}
    for i in range(len(G)):
        rv.update({(i, j): G[i, j] for j in range(len(G)) if j != i})
    return rv


def path_from_predecessor_vector(p, i, j):
    # reconstruir camino a de i a j a partir de un vector `p` predecesor
    # rv = [i]
    # destino_col = p
    # while destino_col[i] != j:
    #     rv.append(i)
    #     i = destino_col[i]
    pass

def path_from_predecessor_matrix(p, i, j):
    rv = []
    destino_col = p[j, :]
    while i != j:
        rv.append([i, destino_col[i]])
        i = destino_col[i]

    return rv

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
    return rv, weights_rv


def bellman_ford(G, source):
    # init
    n = len(G)
    aristas_d = edges_dict(G)
    dist_l = [float('Inf')] * n
    predecessor = [-1] * n
    dist_l[source] = 0
    ciclo_negativo_flag = False
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
            ciclo_negativo_flag = True
            return True, dist_l, predecessor
        else:
            continue
            
    return dist_l, predecessor


def floyd_warshall(w_m):
    # init dist & predecesor mx
    n = w_m.shape[0]  # mx has to be squared
    dist_m = w_m
    predecessor_m = np.array([np.repeat(i, n) for i in range(n)])

    # floyd warshall. find the shortest path fron i to j
    for i in range(n):
        for j in range(n):
            if i != j:
                dist_m[i,j] = w_m[i,j]
            else:
                dist_m[i,j] = 0
                predecessor_m[i,j] = 0
    
    for k in range(n):
        for i in range(n):
            if dist_m[i, k] == np.inf:
                continue
            for j in range(n):
                if dist_m[i,j] > dist_m[i,k] + dist_m[k,j]:
                    dist_m[i, j] = dist_m[i,k] + dist_m[k,j]
                    predecessor_m[i, j] = predecessor_m[k, j]

    return dist_m, predecessor_m


def breadth_first_search(G, source, sink, padre):
    n = G.shape[0]
    visitados = [False] * n
    cola = [source]
    visitados[source] = True
    while cola:
        u = cola.pop(0)
        nei = vecinos(G, u)
        for k in nei:
            if visitados[k] == False and G[u, k] > 0 and G[u, k] !=np.inf:
                cola.append(k)
                visitados[k] = True
                padre[k] = u

    return True if visitados[sink] else False


def ford_fulkerson(G, source, sink):
    padre = [-1] * G.shape[0]
    rv = 0

    while breadth_first_search(G, source, sink, padre):
        flujo_c = np.inf
        s = sink
        while (s != source):
            flujo_c = min(flujo_c, G[padre[s],s])
            s = padre[s]
        
        rv = rv + flujo_c

        v = sink
        while v != source:
            u = padre[v]
            G[u,v] = G[u,v] - flujo_c
            G[v,u] = G[v,u] + flujo_c
            v = padre[v]

    return rv

if __name__ == "__main__":
    print(ford_fulkerson(aver, 0, 5))