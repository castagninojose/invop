param N:=6; # qty regiones
param M:=4; # qty proveedores
param B:=13; # bins de escuelas
param BIG_M_CAP:=1000000;

set C:={1..M}; # proveedores
set R:={1..N}; # regiones
set T:= {1..B}; # bins de escuelas

param max_t[T]:= <1> 20, <2> 40, <3> 60, <4> 80, <5> 100, <6> 150, <7> 200, <8> 300, <9> 400, <10> 500, <11> 600, <12> 700, <13> 800;
param min_t[T]:= <1> 0, <2> 20,<3> 40, <4> 60, <5> 80, <6> 100, <7> 150, <8> 200, <9> 300, <10> 400, <11> 500,  <12> 600,  <13> 700;

param E_R[R]:= <1> 248, <2> 287, <3> 77, <4> 22, <5> 105, <6> 61;

param matriz_proveedor_region[R*C]:=  |1, 2, 3, 4|
                                    |1|1, 1, 0, 0|
                                    |2|1, 1, 0, 0|
                                    |3|1, 0, 1, 0|
                                    |4|1, 0, 1, 1|
                                    |5|1, 0, 0, 1|
                                    |6|1, 1, 0, 1|;

param matriz_proveedor_precio[T*C]:=  |1,           2,         3,         4        |
                                    |1|4696,        2662,      1991,      1605     |
                                    |2|4696,        2182,      1991,      1521     |
                                    |3|4696,        1916,      1991,      1352     |
                                    |4|4696,        1810,      1075,      1267     |
                                    |5|4696,        1597,      890,       1132     |
                                    |6|4227,        1331,      BIG_M_CAP, 1132     |
                                    |7|3992,        1091,      BIG_M_CAP, BIG_M_CAP|
                                    |8|3757,        1038,      BIG_M_CAP, BIG_M_CAP|
                                    |9|3287,        785,       BIG_M_CAP, BIG_M_CAP|
                                    |10|2818,       785,       BIG_M_CAP, BIG_M_CAP|
                                    |11|2348,       785,       BIG_M_CAP, BIG_M_CAP|
                                    |12|1878,       BIG_M_CAP, BIG_M_CAP, BIG_M_CAP|
                                    |13|843.5375,   BIG_M_CAP, BIG_M_CAP, BIG_M_CAP|;

var schools_by_company_qty[R*C] integer; 
var price_bin_by_company[C*T] binary; 
var company_schools_by_bin[C*T] real;

# Restricciones
subto c1: forall <j> in R : sum <i> in C : schools_by_company_qty[j,i] == E_R[j];
subto c2: forall <i> in C : forall <t> in T : sum <j> in R : schools_by_company_qty[j,i] >= min_t[t] - (1 - price_bin_by_company[i,t]) * BIG_M_CAP;
subto c3: forall <i> in C : forall <t> in T : sum <j> in R : schools_by_company_qty[j,i] <= max_t[t] + (1 - price_bin_by_company[i,t]) * BIG_M_CAP;
subto c4: forall <i> in C : sum <t> in T : price_bin_by_company[i,t] == 1;
subto c5: forall <i> in C : forall <t> in T : company_schools_by_bin[i,t] >= sum <j> in R : schools_by_company_qty[j,i] - (1 - price_bin_by_company[i,t]) * BIG_M_CAP;
subto c6: forall <i> in C : forall <j> in R : schools_by_company_qty[j,i] <= matriz_proveedor_region[j,i]*BIG_M_CAP;
subto c7: forall <i> in C : sum <t> in T : company_schools_by_bin[i,t] == sum <j> in R : schools_by_company_qty[j,i];


# Función objetivo
minimize cost: sum <i> in C : sum<t> in T : matriz_proveedor_precio[t,i] * company_schools_by_bin[i,t];