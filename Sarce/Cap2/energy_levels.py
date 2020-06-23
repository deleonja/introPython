import math
from math import *

# se definen las constantes
m_e = 9.1094E-31 #kg    masa del electron
e_c = 1.6022E-19 #C     carga del electron
eps_o = 8.8542E-12 #C^2 s^2 kg^-1 m^-3      permitividad magnética en el vacío
h = 6.6261E-34 #J s     constante de plank

#tomamos la energia como K *1/n^2, donde K
K = -(m_e * (e_c**4))/(8*(eps_o**2)*(h**2))     # por simplicidad, se define una cosntante
print(K) #J

n = 20

# Tomamos el ciclo
for i in range(1,n+1):
    print('E[', i,'] =', K*(1/i**2))

print('---------------------------------------------------')
print('---------------------------------------------------')


# Para mostrar los valores se utilizará una matriz de 5x5
resultado = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

for i in range(5):
    for j in range(5):
        resultado[i][j] = resultado[i][j] +(K*((1/((i+1)**2))-(1/((j+1)**2))))

#se imprime fila por fila
for i in range(5):
    print(resultado[i])

print('---------------------------------------------------')
print('---------------------------------------------------')

#Curiosidades. Si no se cambia de nivel de energia, el cambio de E es cero, por lo que en toda la diagonal deben de haber ceros:
for i in range(5):
    print(resultado[i][i])

# La matriz es anti-simetrica
print('---------------------------------------------------')
print('---------------------------------------------------')