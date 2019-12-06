import numpy as np
import argparse
from itertools import combinations

from utils import prim, edges_dict, bellman_ford, floyd_warshall
from constants import WEIGHT_MATRIX_1, CURRENCY_MATRIX, CAPACITY_MATRIX, DEMAND_MATRIX

def monet_arbit(G):
    """
    Rutina del ejercicio 2 para encontrar arbitraje monetario.
    Args:
        G : numpy.array de dos dimensiones (matriz) con los precios de las monedas
    """
    n = len(G) 
    v0_to_vi = np.zeros((1, n))
    all_to_v0 = np.zeros((n+1, 1))
    H = np.concatenate(G, v0_to_vi)
    H = np.concatenate(H, all_to_v0, axis=1)
    for i in range(n+1):
        bf = bellman_ford(H, n+1)
        if bf[1]:
            continue

def max_flow_with_demands(cap_m=CAPACITY_MATRIX, dem_m=DEMAND_MATRIX):
    """
    Rutina para el ejercicio 4 de maximo flujo con demandas minimas.
    Args:
        cap_m : numpy.array de dos dimensiones con los topes de las aristas
        dem_m : numpy.array de dos dimensiones con los minimos de las aristas
    """
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


def steiner_trees(R, w_m):
    """
    Genera arboles de steiner. Para el ej 3.
    Args:
        R : list contiene a los vertices protegidos
        w_m : numpy.array de dos dimensiones con los pesos originales de las aristas
    """
    d, p = floyd_warshall(w_m)
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

    aristas_l = edges_dict(T)

    return T, W

   
if __name__ == "__main__":
    
    ej_disp = ["ej2", "ej3", "ej4"]

    parser = argparse.ArgumentParser(
            description="Rutinas de los ejercicios 2, 3 y 4."
        )

    parser.add_argument(
        "--ejercicio",
        help=f"Elegir entre ejercicios: {ej_disp}",
        choices=ej_disp,
        required=True,
    )

    args = parser.parse_args()

    target = args.ejercicio

    if target == "ej2":
        # monet_arbit(-np.log(CURRENCY_MATRIX))
        bellman_ford(CURRENCY_MATRIX, 1)

    if target == "ej3":
        print(steiner_trees([1], WEIGHT_MATRIX_1))

    if target == "ej4":
        print(max_flow_with_demands())
    