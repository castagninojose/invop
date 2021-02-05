param N:=3; # qty regiones
param M:=3; # qty proveedores
param B:=3; # bins de escuelas
# cantidad total de escuelas = 9

set C:={1..M}; # proveedores
set R:={1..N}; # regiones
set T:= {1..B}; # bins de escuelas

# set E_R:={1..B};


param matriz_proveedor_region[R*C]:=  |1, 2, 3|
                                    |1|1, 1, 1|
                                    |2|1, 1, 1|
                                    |3|1, 1, 0|;

param matriz_proveedor_precio[T*C]:=  |1, 2, 3|
                                    |1|11, 10, 9|
                                    |2|10, 9, 1000|
                                    |3|8, 1000, 1000|;

param matriz_indicadora[T*C]:=    |1, 2, 3|
                                |1|1, 1, 1|
                                |2|1, 1, 0|
                                |3|1, 0, 0|;


var schools_by_company_qty[R*C] integer; 
var price_bin_by_company[C*T] binary; 
var company_schools_by_bin[C*T] integer;
var min_t[T] real;
var max_t[T] real;

# Restricciones
subto c1: forall <i> in C : sum <t> in T : price_bin_by_company[i,t] == 1;
subto c2: forall <i> in C : forall <t> in T : company_schools_by_bin[i,t] >= sum <j> in R : schools_by_company_qty[j,i] - (1 - price_bin_by_company[i,t]) * 1000;
subto c3: forall <i> in C : forall <j> in R : schools_by_company_qty[i,j] <= matriz_proveedor_region[i,j];
subto c4: forall <i> in C : sum <t> in T : company_schools_by_bin[i,t] == sum <j> in R : schools_by_company_qty[j,i];
subto c5: forall <j> in R : sum <i> in C : schools_by_company_qty[j,i] == 3;
subto c6: forall <t> in T : forall <i> in C : min_t[t] <= matriz_proveedor_precio[t,i];
subto c7: forall <t> in T : forall <i> in C : max_t[t] >= matriz_proveedor_precio[t,i] * matriz_indicadora[t,i];
subto c8: forall <i> in C : forall <t> in T : sum <j> in R : schools_by_company_qty[j,i] >= min_t[t] - (1 - price_bin_by_company[i,t]) * 1000;
subto c9: forall <i> in C : forall <t> in T : sum <j> in R : schools_by_company_qty[j,i] <= max_t[t] + (1 - price_bin_by_company[i,t]) * 1000;


# Función objetivo
minimize f: sum <i> in C : sum<t> in T : (matriz_proveedor_precio[i,t] * company_schools_by_bin[i,t]);