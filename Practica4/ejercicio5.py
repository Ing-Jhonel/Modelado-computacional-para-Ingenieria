import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# --- Sistema 2 ---
def sistema2(vars):
    x, y = vars
    return [np.log(x + 2) + y - 1, x**2 - y - 2]

# Resolver
sol2 = fsolve(sistema2, [1, 1])
print("Ejercicio 5:", sol2)

# Graficar
x = np.linspace(-1.9, 3, 400)  # x > -2 para que log(x+2) esté definido
y = np.linspace(-3, 3, 400)
X, Y = np.meshgrid(x, y)

plt.contour(X, Y, np.log(X + 2) + Y - 1, [0], colors='r')
plt.contour(X, Y, X**2 - Y - 2, [0], colors='b')
plt.plot(sol2[0], sol2[1], 'go')
plt.title("Ejercicio 5")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()
