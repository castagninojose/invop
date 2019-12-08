# Uso

`python main.py -<e>` eligiendo alguno de los ejercicios 2, 3 o 4.

### Ejercicio 2:

Arbitraje monetario. Dada `G` una matriz asimétrica de cambios entre las monedas de 11 paises, busca oportunidades de arbitraje
usando Bellman-Ford para encontrar ciclos negativos en la matriz `-log(G)`. Si no encuentra, devuelve el camino menos costoso

### Ejercicio 3:

Implementación del algoritmo de arboles de Steiner que aparece en [Graphs, Networks and algorithms.](https://doc.lagout.org/science/0_Computer%20Science/2_Algorithms/Graphs%2C%20Networks%20and%20Algorithms%20%284th%20ed.%29%20%5BJungnickel%202012-11-09%5D.pdf)

### Ejercicio 4:
    
Máximo flujo para un grafo `G = (V, E)` donde las aristas además de un tope tienen también un piso mímino de flujo.
Construimos un grafo `G' = (V', E')` definiendolo del siguiente modo:

`V' = V + {s', t'}` con `s'` y `t'` nuevos source y sink respectivamente.  
Luego para cada arista `(u, v)` en `G` seteamos las capacidades `c'` asi:

* Una arista `(u, v)` con capacidad igual a la diferencia entre el tope y el piso de `(u, v)` en `G`.
* Una arista `(s', v)` con capacidad igual al piso de `(u, v)`
* Una arista `(u, t')` con capacidad igual al piso de `(u, v)`

De esta manera podemos encontrar un flujo factible en `G` buscando un flujo máximo en `G'` que luego podemos ir aumentando usando `ford_fulkerson`.  
Para una descripción más detallada del procedimiento ir [aquí](https://pdfs.semanticscholar.org/03a2/785783f43202925da70ae842eeda9cebd77e.pdf)
