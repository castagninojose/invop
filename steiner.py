import numpy as np
from itertools import combinations
from scipy.sparse.csgraph import floyd_warshall

# from prim import prim
from constants import WEIGHT_MATRIX_1


def floyd(n, w_m):
    # TODO agregar predecesor(es) al output de esta fun
    # d = np.zeros((n,n))
    d = w_m
    # np.fill_diagonal(d, 0)
    p = np.array([np.repeat(i, n) for i in range(n)])
    for i in range(n):
        for j in range(n):
            if i != j:
                d[i,j] = w_m[i,j]
            else:
                d[i,j] = 0
                p[i,j] = -9991
    for k in range(n):
        for i in range(n):
            if d[i, k] == np.inf:
                # continue
                p[i, k] = -9991
            for j in range(n):
                if d[i,j] > d[i,k] + d[k,j]:
                    d[i, j] = d[i,k] + d[k,j]
                    p[i, j] = p[k, j]

    return d, p


def steiner(n, R, matriz_w):
    d, p = floyd_warshall(
        WEIGHT_MATRIX_1, directed=False, return_predecessors=True
    )
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
    # print(steiner(7, [1], WEIGHT_MATRIX_1))
    predecesor_np = floyd_warshall(WEIGHT_MATRIX_1, directed=False, return_predecessors=True)[1]
    predecesor_lp = floyd(7, WEIGHT_MATRIX_1)[1]
    print(f"Lopiibe: {predecesor_lp}")
    print(f"Numpaai: {predecesor_np}")
