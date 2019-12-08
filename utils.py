"""
Modulo de funciones auxiliares. La primera parte son funciones más agnósticas o no-especificas.
Hacia el final aparecen algunas implementaciones de subrutinas utiles para los algoritmos principales.
"""
import numpy as np

from constants import (
    WEIGHT_MATRIX_1,
    CURRENCY_MATRIX,
    PAISES_DICT,
    EJ_4_21_CURRENCY_M,
    FF_TESTING_M,
    CAPACITY_MATRIX,
    DEMAND_MATRIX,
)


class Grafo:
    """
    Para representar grafos. Deprecada por ahora :(
    """
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


def edges_dict_from_m(G):
    """
    Genera diccionario con las aristas como keys y los valores como values.
    Args:
        G = numpy.array
    Devuelve:
        dict con las aristas y pesos representados por G como keys y values respectivamente.
    Nota: 
        Ignora las diagonales ya que asume que no hay self-loops (i.e.) aristas `(u,u)`.
    """
    n = G.shape[0]
    rv = {}
    for i in range(n):
        rv.update(
            {(i, j): G[i, j] for j in range(n) if j != i}
        )
    return rv


def matrix_from_edges_d(d):
    """
    Genera una matriz a partir de un diccionario de aristas.
    Args:
        d = dict con aristas como keys y sus "pesos". {(u,v) : peso(u, v)}.
    Devuelve:
        numpy.array de dos dimensiones (matriz de nxn).
    """
    n = 1 + max(
        [v[0] for v in d.keys()] + [v[1] for v in d.keys()]
    )  # para ver el tamaño de la matrix me fijo el indice maximo de los vertices + 1

    rv = np.empty((n,n))*np.nan

    for arista, value in d.items():
        u, v = arista[0], arista[1]
        if isinstance(value, float):
            rv[u, v] = value
    
    return rv


def path_from_predecessor(p, i, j):
    """
    Buscar camino del vertice `i` al `j` usando un vector `p` de predecesores.
    """
    rv = []
    while i != j:
        rv.append([i, p[i]])
        i = p[i]

    return rv


def path_from_predecessor_matrix(P, i, j):
    """
    Buscar camino del vertice `i` al `j` usando la matriz de predecesores `P`.
    """
    return path_from_predecessor(P[j,:], i, j)


def vecinos(G, v):
    """
    Genera una lista con los vecinos del vertice `v` en `G`.
    """
    aristas_finitas = G[v,:] < np.inf
    vecinos_lista = np.where(aristas_finitas.tolist())[0]
    return vecinos_lista


def ix_min(key, vis_l):
    """
    Busca el minimo en `key` ignorando los indices que aparecen en `vis_l`.
    Args:
        - key : list de enteros
        - vis_l : list de booleanos
    """
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
    
    weights_rv = sum([G[l[0]][l[1]] for l in rv])
    return rv, weights_rv


def bellman_ford(G, source):
    # init
    n = len(G)
    aristas_d = edges_dict_from_m(G)
    dist_l = [float('Inf')] * n
    predecessor = [-1] * n
    dist_l[source] = 0
    ciclo_negativo_flag = False
    # relax
    for i in range(n-1):
        for e in aristas_d.keys():
            u, v = e[0], e[1]
            if (dist_l[v] > dist_l[u] + aristas_d[e]):
                dist_l[v] = dist_l[u] + aristas_d[e]
                predecessor[v] = u
    
    # now look for negative weight cycles
    for e in aristas_d:
        u, v = e[0], e[1]
        if (dist_l[v] != float('Inf') and dist_l[v] > dist_l[u]):
            print(f"Existe ciclo negativo entre {PAISES_DICT[source]} y {PAISES_DICT[v]}")
            camino = path_from_predecessor(predecessor, source, v)
            print(f"Camino: {camino}")
            return True, dist_l, predecessor
        
    
    return False, dist_l, predecessor
            



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
                if dist_m[i, j] > dist_m[i, k] + dist_m[k, j]:
                    dist_m[i, j] = dist_m[i, k] + dist_m[k, j]
                    predecessor_m[i, j] = predecessor_m[k, j]

    return dist_m, predecessor_m


def camino_superador(G, source, sink, padre):
    
    visitados = [False] * (G.shape[0])
    cola = []
    cola.append(source)
    visitados[source] = True

    while cola: 
        u = cola.pop(0)
        for v in vecinos(G, u): 
            if visitados[v] == False and G[u, v] > 0: 
                cola.append(v) 
                visitados[v] = True
                padre[v] = u

    if visitados[sink]:
        return True, padre
    else:
        return False, padre


def ford_fulkerson(G, source, sink, modificado=False, ff=None):
    """
    Args:
        - G : np.array
        - source : int
        - sink : int
        - (opcional) modificado : boolean para ejecutar la version modificada para la ultima parte del ej 4.
        - (opcional) caps : np.array con las capacidades de las aristas
        - (opcional) floors : np.array con las demandas de las aristas.
    """
    
    # init
    flujos_cap_d = edges_dict_from_m(G)
    flujos_residual = flujos_cap_d.copy()
    for arista in flujos_cap_d.keys():
        u, v = arista[0], arista[1]
        if isinstance(flujos_cap_d[arista], int):
            flujos_cap_d.update({arista : 0})  # donde no hay `inf` ni `nan` pongo flujo 0

    padre = [-1] * G.shape[0]
    R = matrix_from_edges_d(flujos_cap_d)
    rv = 0
    while camino_superador(R, source, sink, padre)[0]:  # mientras haya camino superador en el residual
        flujo_camino = np.inf
        s = sink 
        while(s !=  source): 
            flujo_camino = min(flujo_camino, R[padre[s], s]) 
            s = padre[s] 

        # actualizo flujo maximo
        rv +=  flujo_camino

        # actualizo capacidades residuales
        v = sink
        while(v != source):
            if modificado:
                # version modificada de actualizar las capacidades residuales
                u = padre[v]
                if isinstance(G[u, v], float):
                    R[u, v] = R[u, v] - ff[(u, v)]
                elif isinstance(G[v, u], float):
                    R[u, v] = ff[(v, u)] - R[v, u]
                else:
                    R[u, v] = 0
                v = padre[v]
            else:
                u = padre[v]
                R[u, v] -= flujo_camino
                R[v, u] += flujo_camino
                v = padre[v]

    return rv, edges_dict_from_m(G-R), R

if __name__ == "__main__":
    print(ford_fulkerson(FF_TESTING_M, 0, 5))
