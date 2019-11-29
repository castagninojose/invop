import numpy as np

from constants import CAPACITY_MATRIX, DEMAND_MATRIX, WEIGHT_MATRIX_1

def edge_dict_from_matrix(w_m):
    n = w_m.shape[1]
    rv = []
    for i in range(n):
        for k in range(n):
            if w_m[i,k] < np.inf:
                rv.append((i,k))
    
    return {i : rv[i] for i in range(len(rv))}

def generate_new_cap_m(cap_m=CAPACITY_MATRIX, dem_m=DEMAND_MATRIX, source=0, sink=1):
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

if __name__ == "__main__":
    print(edge_dict_from_matrix(CAPACITY_MATRIX))
    print(edge_dict_from_matrix(DEMAND_MATRIX))
    print(edge_dict_from_matrix(WEIGHT_MATRIX_1))
    rvm = generate_new_cap_m()
    print(rvm)