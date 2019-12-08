"""Trabajo libre 12/08/19. Rutina principal."""
import numpy as np
import argparse
from itertools import combinations

from utils import (
    prim,
    bellman_ford,
    floyd_warshall,
    ford_fulkerson,
    matrix_from_edges_d,
    edges_dict_from_m,
    path_from_predecessor_matrix
)

from constants import (
    WEIGHT_MATRIX_1,
    CURRENCY_MATRIX,
    CAPACITY_MATRIX,
    DEMAND_MATRIX,
    CAPACITY_MATRIX_1,
    DEMAND_MATRIX_1,
    PAISES_DICT,
    EJ_4_21_CURRENCY_M
)

def monet_arbit(G):
    """
    Rutina del ejercicio 2 para encontrar oportunidad de arbitraje cambiario.
    Args:
        G : numpy.array de dos dimensiones (matriz) con los precios de las monedas. `G[i,j]` es
            la cantidad de moneda `j` que se puede comprar con una unidad de moneda `i`.
    """
    n = len(G)
    for i in range(n):
        print(f"Moneda: {PAISES_DICT[i]}")
        bf = bellman_ford(G, i)
        if bf[0] == True: # ciclo negativo
            # aca bellman-ford imprime el camino del ciclo negativo
            continue
        else:
            # devolver los caminos menos costosos
            for k in range(n):
                print(f"Camino suboptimo: {path_from_predecessor_matrix(bf[2], i, k)}")


def steiner_trees(R, w_m):
    """
    Genera las aristas que debemos agregar para armar un arbol de steiner.
    Args:
        R : list contiene a los vertices "protegidos"
        w_m : numpy.array de dos dimensiones con los pesos originales de las aristas
    Returns:
        dict con {(u, v) : weight(u, v)}
    """
    d, p = floyd_warshall(w_m)
    W = np.inf
    T = []
    S = np.delete(w_m, R, 0)
    S = np.delete(S, R, 1)
    for i in range(1, len(R)-2):

        for c in combinations(S, i):

            P = np.delete(S, list(c), 0)
            P = np.delete(P, list(c), 1)
            T_prima, z = prim(P)
            if z < W:
                W = z
                T = T_prima

    rv = dict()

    for e in T:
        u, v = e[0], e[1]
        if w_m[u, v] == np.inf or w_m[u, v] > d[u, v]:
            for arista in path_from_predecessor_matrix(p, u, v):
                rv.update({(u,v): [arista[0], arista[1]]})

    return T, W, rv


def max_flow_with_demands(cap_m=CAPACITY_MATRIX, dem_m=DEMAND_MATRIX):
    """
    Rutina para el ejercicio 4 de maximo flujo con demandas minimas.
    Args:
        cap_m : numpy.array de dos dimensiones con los topes de las aristas
        dem_m : numpy.array de dos dimensiones con los minimos de las aristas
    See `constants.py` for default values.
    """
    n = len(cap_m)
    rv_m = cap_m - dem_m
    rv_m[n-1,0] = 9991  # python no me quiere dejar asignarle np.inf
    s = []
    t = [np.nan]
    for i in range(n):  # para cada vertice v
        t.append(dem_m[i][~np.isnan(dem_m[i])].sum())
        s.append(dem_m[:,i][~np.isnan(dem_m[:,i])].sum())

    breakpoint()
    
    rv_m = np.r_[[s], rv_m]
    rv_m = np.c_[rv_m, np.array(t)]
    vacios_1 = np.empty((1, n+1))*np.nan
    vacios_2 = np.empty((n+2, 1))*np.nan
    rv_m = np.r_[rv_m, vacios_1]  # agrega fila vacia al final
    rv_m = np.c_[vacios_2, rv_m]  # agrega columna vacia al final

    breakpoint()

    f1, flujo_factible_d, vvv = ford_fulkerson(rv_m, 0, n+1)

    matriz_aux = matrix_from_edges_d(flujo_factible_d)
    
    matriz_aux = np.delete(matriz_aux, [0, n+1], 0)
    matriz_aux = np.delete(matriz_aux, [0, n+1], 1)
    matriz_aux[n-1, 0] = 0
    matriz_aux[0, n-1] = 0

    breakpoint()
    
    f2, aver_flujo, puff = ford_fulkerson(
        matriz_aux, 0, n-1, modificado=True, flujo_factible=flujo_factible_d
    )

    return f2, aver_flujo


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(
            description="Rutinas de los ejercicios 2, 3 y 4."
        )

    parser.add_argument("-2", "--ejercicio-2", action="store_true", default=False)

    parser.add_argument("-3", "--ejercicio-3", action="store_true", default=False)

    parser.add_argument("-4", "--ejercicio-4", action="store_true", default=False)

    args = parser.parse_args()


    if args.ejercicio_2:
        monet_arbit(-np.log(EJ_4_21_CURRENCY_M))

    elif args.ejercicio_3:
        print(steiner_trees([1, 2, 4, 6], WEIGHT_MATRIX_1))

    elif args.ejercicio_4:
        print(max_flow_with_demands(cap_m=CAPACITY_MATRIX, dem_m=DEMAND_MATRIX))
    
    else:
        print(f"Elegir el ejercicio a resolver. Puede ver las opciones en main.py -h")