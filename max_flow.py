import numpy as np

from constants import CAPACITY_MATRIX, DEMAND_MATRIX, WEIGHT_MATRIX_1

capacidad_excedente = CAPACITY_MATRIX - DEMAND_MATRIX

def edge_list_from_matrix(w_m):
    n = w_m.shape[1]
    rv = []
    for i in range(n):
        for k in range(n):
            if w_m[i,k] < np.inf:
                # breakpoint()
                rv.append((i,k))
    
    return {i : rv[i] for i in range(len(rv))}

def generate_gp(cap_m=CAPACITY_MATRIX, dem_m=DEMAND_MATRIX, source=0, sink=1):
    n = len(cap_m)
    rv = np.zeros((n+2, n+2))
    rv[0,n] = np.inf
    rv[2:, 2:] = cap_m - dem_m
    breakpoint()
    for i in range(n):
        rv[i, n-1] = sum(dem_m[i])
        rv[i, n] = 'sas'


breakpoint()




if __name__ == "__main__":
    print(edge_list_from_matrix(CAPACITY_MATRIX))
    print(edge_list_from_matrix(DEMAND_MATRIX))
    print(edge_list_from_matrix(WEIGHT_MATRIX_1))
    generate_gp()