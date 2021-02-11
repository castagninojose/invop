param N := 7; # qty regiones
param M := 5; # qty proveedores
param B := 15; # bins de escuelas
param BIG_M_CAP := 1000000;

set C := {1..M}; # proveedores
set R := {1..N}; # regiones
set T := {1..B}; # bins de escuelas

param max_t[T] := <1> 20, <2> 40, <3> 60, <4> 80, <5> 100, <6> 150, <7> 200, <8> 300, <9> 400, <10> 500, <11> 600, <12> 700, <13> 800, <14> 900, <15> 1000;
param min_t[T] := <1> 0, <2> 20,<3> 40, <4> 60, <5> 80, <6> 100, <7> 150, <8> 200, <9> 300, <10> 400, <11> 500,  <12> 600,  <13> 700, <14> 800, <15> 900;

param E_R[R]:= <1> 10, <2> 287, <3> 77, <4> 248, <5> 195, <6> 61, <7> 122;

param company_region_matrix[R*C] :=   |1, 2, 3, 4, 5|
                                    |1|1, 1, 0, 0, 1|
                                    |2|1, 1, 0, 0, 0|
                                    |3|1, 0, 1, 0, 1|
                                    |4|0, 0, 1, 1, 1|
                                    |5|1, 0, 0, 1, 0|
                                    |6|1, 1, 0, 1, 0|
                                    |7|0, 1, 0, 1, 1|;

param company_price_matrix[T*C] :=  |1,             2,         3,         4,         5        |
                                    |1|2996,        2182,      1991,      1605,      1600     |
                                    |2|2996,        2182,      1991,      1521,      1600     |
                                    |3|2996,        1916,      1491,      1452,      1500     |
                                    |4|2996,        1810,      1375,      1367,      1400     |
                                    |5|2896,        1597,      1190,      1232,      1300     |
                                    |6|2427,        1331,      1090,      1232,      1200     |
                                    |7|2192,        1091,      990,       1132,      1150     |
                                    |8|1957,        1038,      890,       1132,      1100     |
                                    |9|1287,        785,       850,       999,       990      |
                                    |10|1000,       BIG_M_CAP, BIG_M_CAP, 949,       960      |
                                    |11|900,        BIG_M_CAP, BIG_M_CAP, 899,       899      |
                                    |12|800,        BIG_M_CAP, BIG_M_CAP, 849,       799      |
                                    |13|BIG_M_CAP,  BIG_M_CAP, BIG_M_CAP, BIG_M_CAP, 749      |
                                    |14|BIG_M_CAP,  BIG_M_CAP, BIG_M_CAP, BIG_M_CAP, BIG_M_CAP|
                                    |15|BIG_M_CAP,  BIG_M_CAP, BIG_M_CAP, BIG_M_CAP, BIG_M_CAP|;

# param solutions_offset_matrix[R*C] := |1,   2, 3, 4|
#                                     |1|248, 0, 0, 0|
#                                     |2|287, 0, 0, 0|
#                                     |3|77,  0, 0, 0|
#                                     |4|22,  0, 0, 0|
#                                     |5|105, 0, 0, 0|
#                                     |6|61,  0, 0, 0|;

# param solutions_offset_matrix_2[R*C] :=   |1, 2,   3,   4|
#                                         |1|0, 248, 0,   0|
#                                         |2|0, 287, 0,   0|
#                                         |3|0, 0,   77,  0|
#                                         |4|0, 0,   22,  0|
#                                         |5|0, 0,   0, 105|
#                                         |6|0, 61,  0,   0|;

var schools_qty_by_region_company[R*C] integer; 
var price_bin_by_company[C*T] binary; 
var schools_qty_by_company_bin[C*T] real;
# var solution_offset[R*C] binary;
# var solution_offset_2[R*C] binary;
# var solution_offset_3[R*C] binary;
# var solution_offset_4[R*C] binary;

# Restricciones
subto c1: forall <j> in R : sum <i> in C : schools_qty_by_region_company[j,i] == E_R[j];
subto c2: forall <i> in C : forall <t> in T : sum <j> in R : schools_qty_by_region_company[j,i] >= min_t[t] - (1 - price_bin_by_company[i,t]) * BIG_M_CAP;
subto c3: forall <i> in C : forall <t> in T : sum <j> in R : schools_qty_by_region_company[j,i] <= max_t[t] + (1 - price_bin_by_company[i,t]) * BIG_M_CAP;
subto c4: forall <i> in C : sum <t> in T : price_bin_by_company[i,t] == 1;
subto c5: forall <i> in C : forall <t> in T : schools_qty_by_company_bin[i,t] >= sum <j> in R : schools_qty_by_region_company[j,i] - (1 - price_bin_by_company[i,t]) * BIG_M_CAP;
subto c6: forall <i> in C : forall <j> in R : schools_qty_by_region_company[j,i] <= company_region_matrix[j,i]*BIG_M_CAP;
subto c7: forall <i> in C : sum <t> in T : schools_qty_by_company_bin[i,t] == sum <j> in R : schools_qty_by_region_company[j,i];

# subto c8: forall <j> in R : forall <i> in C : if solutions_offset_matrix[j,i] != 0
#     then schools_qty_by_region_company[j,i] >= (solutions_offset_matrix[j,i] + 1) * solution_offset[j,i] end;

# subto c9: forall <j> in R : forall <i> in C : if solutions_offset_matrix[j,i] != 0
#     then 800 - schools_qty_by_region_company[j,i] >= ((800 - (solutions_offset_matrix[j,i] - 1)) * solution_offset_2[j,i]) end;

# subto c10: forall <j> in R : forall <i> in C : if  (solutions_offset_matrix[j,i] != 0)
#     then sum <i> in C : sum <j> in R : solution_offset[j,i] + solution_offset_2[j,i] == 1 end;

# subto c11: forall <j> in R : forall <i> in C : if solutions_offset_matrix_2[j,i] != 0
#     then schools_qty_by_region_company[j,i] >= (solutions_offset_matrix_2[j,i] + 1) * solution_offset_3[j,i] end;

# subto c12: forall <j> in R : forall <i> in C : if solutions_offset_matrix_2[j,i] != 0
#     then 800 - schools_qty_by_region_company[j,i] >= ((800 - (solutions_offset_matrix_2[j,i] - 1)) * solution_offset_4[j,i]) end;

# subto c13: forall <j> in R : forall <i> in C : if  (solutions_offset_matrix_2[j,i] != 0)
#     then sum <i> in C : sum <j> in R : solution_offset_3[j,i] + solution_offset_4[j,i] == 1 end;

# Funcion objetivo
minimize cost: sum <i> in C : sum<t> in T : company_price_matrix[t,i] * schools_qty_by_company_bin[i,t];