import numpy as np

WEIGHT_MATRIX_1 = np.array(
    [[np.inf, 2, 3, 3, np.inf,np.inf,np.inf],
    [2, np.inf, 4, np.inf, 3, np.inf, np.inf],
    [3, 4, np.inf, 5, 1, 6, np.inf],
    [3, np.inf, 5, np.inf, np.inf, 7, np.inf],
    [np.inf, 3, 1, np.inf, np.inf, 8, np.inf],
    [np.inf, np.inf, 6, 7, 8, np.inf, 9],
    [np.inf, np.inf, np.inf ,np.inf, np.inf, 9, np.inf]]
)

WEIGHT_MATRIX_2 = np.array(
    [[np.inf, 2, 3, 3, np.inf,np.inf,np.inf],
    [2, np.inf, 4, np.inf, 3, np.inf, np.inf],
    [3, 4, np.inf, 5, 1, 6, np.inf],
    [3, np.inf, 5, np.inf, np.inf, 7, np.inf],
    [np.inf, 3, 1, np.inf, np.inf, 8, np.inf],
    [np.inf, np.inf, 6, 7, 8, np.inf, 9],
    [np.inf, np.inf, np.inf ,np.inf, np.inf, 9, np.inf]]
)

CAPACITY_MATRIX = np.array(  # upper bounds for flow problems
    [[np.nan, 10, 20, np.nan, np.nan,np.nan],
    [np.nan, np.nan, np.nan, np.nan, 10, np.nan],
    [np.nan, 10, np.nan, 5, np.nan, np.nan],
    [np.nan, 15, np.nan, np.nan, np.nan, 15],
    [np.nan, np.nan, np.nan, 10, np.nan, 20],
    [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]]
)

DEMAND_MATRIX = np.array(  # lower bounds for flow problems
    [[np.nan, 4, 7, np.nan, np.nan, np.nan],
    [np.nan, np.nan, np.nan, np.nan, 3, np.nan],
    [np.nan, 5, np.nan, 0, np.nan, np.nan],
    [np.nan, 1, np.nan, np.nan, np.nan, 2],
    [np.nan, np.nan, np.nan, 4, np.nan, 6],
    [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]]
)

CURRENCY_MATRIX = np.array(  # M[i,j] = qty of currency j bought with currency i
    [[1, 0.0167, 14.073, 0.0703, 0.625, 106.016, 0.112, 0.0556, 58.539, 0.0222, 0.326],
    [59.837, 1, 842.312, 4.208, 37.431, 6345.05, 7.732, 3.329, 3503.57, 1.329, 19.509],
    [0.071, 0.00119, 1, 0.00499, 0.0444, 7.526, 0.00799, 0.00395, 4.156, 0.00158, 0.0231],
    [14.207, 0.237, 199.994, 1, 8.887, 1506.54, 1.598, 0.7904, 831.867, 0.315, 4.632],
    [1.559, 0.0261, 21.947, 0.109, 1, 165.328, 0.175, 0.0867, 91.299, 0.0346, 0.508],
    [0.00909, 0.00015, 0.128, 0.00064, 0.00569, 1, 0.00102, 0.00051, 0.532, 0.0002, 0.00296],
    [8.4331, 0.141, 118.711, 0.593, 5.275, 894.244, 1, 0.469, 493.776, 0.187, 2.749],
    [17.36, 0.29, 244.37, 1.22, 10.86, 1840.8, 1.05, 1, 1016.4, 0.39, 5.66],
    [0.017, 0.00028, 0.24, 0.0012, 0.011, 1.79, 0.0019, 0.00094, 1, 0.00038, 0.0055],
    [45.03, 0.75, 633.86, 3.17, 28.17, 4774.8, 5.06, 2.5, 2636.5, 1, 14.68],
    [3.065, 0.0512, 43.15, 0.215, 1.918, 325.04, 0.345, 0.17, 179.48, 0.068, 1]]
    )

PAISES_DICT = {  # useful for ex 2
    0: 'argentina',
    1: 'eeuu',
    2: 'chile',
    3: 'brasil',
    4: 'uruguay',
    5: 'paraguay',
    6: 'bolivia',
    7: 'peru',
    8: 'colombia',
    9: 'canada',
    10: 'mexico',
    # 11: 'venezuela',
    # 12: 'ecuador'
}

EJ_4_21_CURRENCY_M = np.array(
    [[1, 0.0179, 12.25, 0.0746],
    [59.5, 1, 715.9, 4.15],
    [0.082, 0.014, 1, 0.0058],
    [15.4, 0.24, 172.34, 1]]
)

aver = np.array(
    [[np.inf, 16, 13, np.inf, np.inf, np.inf], 
    [np.inf, np.inf, 10, 12, np.inf, np.inf], 
    [np.inf, 4, np.inf, np.inf, 14, np.inf], 
    [np.inf, np.inf, 9, np.inf, np.inf, 20], 
    [np.inf, np.inf, np.inf, 7, np.inf, 4], 
    [np.inf, np.inf, np.inf, np.inf, np.inf, np.inf]]
    ) 