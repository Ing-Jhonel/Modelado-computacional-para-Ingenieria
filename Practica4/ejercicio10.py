# SISTEMA 3 (usando def)
import numpy as np
from scipy.optimize import fsolve

def sistema3(v):
    x, y, z = v
    return [
        x**2 + y - 1,   # x^2 + y = 1
        y**2 + z - 2,   # y^2 + z = 2
        z**2 + x - 3    # z^2 + x = 3
    ]

sol3 = fsolve(sistema3, [1, 1, 1])
print("Ejercicio 10 - solución aproximada (x,y,z) =", sol3)
