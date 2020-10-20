# Importar librerías. matplotlib.pyplot para graficar
import numpy as np
import matplotlib.pyplot as plt

# Crear un arreglo con los valores de x
x = np.arange(0,5,0.1)

# Crear arreglo con los valores de y
y = np.sin(x)

# Decirle a python que grafique
plt.plot(x, y, 'ok', lw=5, label="f(x)=sin(x)")
plt.legend()
plt.ylabel("f(x)")
plt.xlabel("x")
plt.grid()

plt.savefig("pf.pdf")

#plt.show()
