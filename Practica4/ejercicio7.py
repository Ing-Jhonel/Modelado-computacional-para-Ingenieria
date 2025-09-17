import numpy as np
from scipy.optimize import fsolve

sistema = lambda v: [
    np.exp(v[0]) + v[1] + v[2] - 7,   # e^x + y + z = 7
    v[0]**2 + v[1]**2 - 4,            # x^2 + y^2 = 4
    v[2] - v[1] - 1                   # z - y = 1
]

sol = fsolve(sistema, [1, 1, 1])
print("Ejercicio 7 - solución aproximada (x,y,z) =", sol)
