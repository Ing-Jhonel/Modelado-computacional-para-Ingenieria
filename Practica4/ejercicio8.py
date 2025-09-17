# SISTEMA 1
import numpy as np
from scipy.optimize import fsolve

sistema1 = lambda v: [
    v[0]**2 + v[1]**2 + v[2]**2 - 9,   # x^2 + y^2 + z^2 = 9
    v[0]*v[1] - 2,                     # xy = 2
    v[0] + v[2] - 3                    # x + z = 3
]

sol1 = fsolve(sistema1, [1, 1, 1])
print("Sistema 1 - solución aproximada (x,y,z) =", sol1)
