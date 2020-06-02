import numpy as np

Cf = 33595.256687
Cr = 57855.954844
lf = 2.492077
lr = 2.752993
m = 2979.512691
Iz = 4549.291614
Vx = 20
L = lf + lr

K10 = np.array([0.7910, 0.1847, 0.2223, -0.3194])
K15 = np.array([0.7910, 0.1875, 1.3818, -0.0078])
K20 = np.array([0.7910, 0.2142, 2.0337,  0.1326])
K25 = np.array([0.7910, 0.2354, 2.5522,  0.2133])
K30 = np.array([0.7910, 0.2535, 2.9557,  0.2650])

Q_k = np.eye(4) * 1.0
Q_k = np.array([[0, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 1]])
H_k = np.array([[1, 0, 0, 0],
                [0, 0, 1, 0]])