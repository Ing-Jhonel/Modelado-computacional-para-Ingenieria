# SISTEMA 2 (usando def)
import numpy as np
from scipy.optimize import fsolve

def sistema2(v):
    x, y, z = v
    return [
        np.sin(x) + y - 2,   # sin(x) + y = 2
        y**2 + z - 3,        # y^2 + z = 3
        x + z**2 - 4         # x + z^2 = 4
    ]

sol2 = fsolve(sistema2, [1, 1, 1])
print("Ejercicio 9 - solución aproximada (x,y,z) =", sol2)
