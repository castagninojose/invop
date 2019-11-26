import numpy as np
from itertools import combinations
from scipy.sparse.csgraph import floyd_warshall

from prim import prim
from constants import DEFAULT_WEIGHT_MATRIX_1


def floyd(n, w_m):
    # TODO agregar predecesor(es) al output de esta fun
    d = np.zeros((n,n))
    p = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            if i != j:
                d[i,j] = w_m[i,j]
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i,j] = min(d[i,j], d[i,k]+d[k,j])
                # TODO: agregar predecesor

    return d


# def partes_de_s(m, k=1):
#     [m[]]
breakpoint()
def steiner(n, R, matriz_w):
    W = np.inf
    T = []
    H = "Kn"  # grafo completo de n nodos
    S = np.delete(matriz_w, R, 0)
    S = np.delete(S, R, 1)
    for i in range(S.shape[1]-1):

        for c in combinations(S, i):

            P = np.delete(S, list(c), 0)
            P = np.delete(P, list(c), 1)
            T_prima, z = prim(P)
            if W > z:
                W = z
                T = T_prima

    return T, W

   
if __name__ == "__main__":
    d, p = floyd_warshall(DEFAULT_WEIGHT_MATRIX_1, directed=False, return_predecessors=True)
    print(d)
    print(p)
    print(steiner(7, [1], DEFAULT_WEIGHT_MATRIX_1))