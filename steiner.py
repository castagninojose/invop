import numpy as np
from scipy.sparse.csgraph import floyd_warshall
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

    return d

   
if __name__ == "__main__":
    floyd_warshall(DEFAULT_WEIGHT_MATRIX_1, directed=False, return_predecessors=True)