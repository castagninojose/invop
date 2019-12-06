import numpy as np
import argparse
from itertools import combinations
# from scipy.sparse.csgraph import floyd_warshall, bellman_ford

from utils import prim, edges_dict, edge_dict_from_matrix
from constants import WEIGHT_MATRIX_1, CURRENCY_MATRIX

def monet_arbit(G):
    n = len(G) 
    v0_to_vi = np.zeros((1, n))
    all_to_v0 = np.zeros((n+1, 1))
    H = np.concatenate(G, v0_to_vi)
    H = np.concatenate(H, all_to_v0, axis=1)
    for i in range(n+1):
        bf = bellman_ford(H, n+1)
        if bf[1]:
            continue

def max_flow_with_demands(cap_m=CAPACITY_MATRIX, dem_m=DEMAND_MATRIX, source=0, sink=1):
    n = len(cap_m)
    rvm = cap_m - dem_m
    rvm[n-1,0] = np.inf
    s = []
    t = [np.nan]
    for i in range(n):
        t.append(dem_m[i][~np.isnan(dem_m[i])].sum())
        s.append(dem_m[:,i][~np.isnan(dem_m[:,i])].sum())
    
    rvm = np.r_[[s], rvm]
    rvm = np.c_[rvm, np.array(t)]
    vacios_1 = np.empty((1,n+1))*np.nan
    vacios_2 = np.empty((n+2, 1))*np.nan
    rvm = np.r_[rvm, vacios_1]
    rvm = np.c_[vacios_2, rvm]

    return rvm


def floyd_warshall(n, w_m):
    # init dist & predecesor mx
    d = w_m
    p = np.array([np.repeat(i, n) for i in range(n)])

    # floyd warshall. find the shortest path fron i to j
    for i in range(n):
        for j in range(n):
            if i != j:
                d[i,j] = w_m[i,j]
            else:
                d[i,j] = 0
                p[i,j] = 0
    
    for k in range(n):
        for i in range(n):
            if d[i, k] == np.inf:
                continue
            for j in range(n):
                if d[i,j] > d[i,k] + d[k,j]:
                    d[i, j] = d[i,k] + d[k,j]
                    p[i, j] = p[k, j]

    return d, p


def steiner_trees(n, R, w_m):
    d, p = floyd_warshall(
        WEIGHT_MATRIX_1, directed=False, return_predecessors=True
    )
    W = np.inf
    T = []
    H = "Kn"  # grafo completo de n nodos
    S = np.delete(w_m, R, 0)
    S = np.delete(S, R, 1)
    for i in range(S.shape[1]-1):

        for c in combinations(S, i):

            P = np.delete(S, list(c), 0)
            P = np.delete(P, list(c), 1)
            T_prima, z = prim(P)
            if W > z:
                W = z
                T = T_prima

    aristas_l = edges_dict()    

    return T, W

   
if __name__ == "__main__":
    ejs = [2, 3, 4]
    parser = argparse.ArgumentParser(
            description="Rutinas de los ejercicios 2, 3 y 4."
        )

    parser.add_argument(
        "--ejercicio",
        help=f"Elegir entre ejercicios: {ejs}",
        choices=ejs,
        required=True,
    )

    if ejercicio == 2:
        monet_arbit(-np.log(CURRENCY_MATRIX))

    if ejercicio == 3:
        print(steiner(7, [1], WEIGHT_MATRIX_1))

    if ejercicio == 4:
        print(max_flow_with_demands())
    