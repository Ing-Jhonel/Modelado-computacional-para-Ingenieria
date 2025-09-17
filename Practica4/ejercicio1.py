import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def ej1(vars):
    x, y = vars
    return [x**2 + y**2 - 4, np.exp(x) + y - 1]

# Resolver
sol1 = fsolve(ej1, [0.5, 0.5])
print("Ejercicio 1:", sol1)

# Graficar
x = np.linspace(-3, 3, 400)
y = np.linspace(-3, 3, 400)
X, Y = np.meshgrid(x, y)

# Curvas de nivel de las ecuaciones
plt.contour(X, Y, X**2 + Y**2 - 4, [0], colors='r')
plt.contour(X, Y, np.exp(X) + Y - 1, [0], colors='b')

# Solución encontrada
plt.plot(sol1[0], sol1[1], 'go')

plt.title("Ejercicio 1")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()

