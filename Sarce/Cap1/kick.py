import math
from math import *
# definimos cada una de las variables en unidades del SI
rho = 1.2
g = 9.8
a = 0.11
A = pi*a**2
m = 0.43
C_D = 0.4
v_1 = 120 / 3.6
v_2 = 30 / 3.6

# Fuerzas
F_g = round((m*g),1)

def F_d(x):
    return 0.5*C_D*rho*A*x**2

F_d(v_1)
F_d(v_2)

#Razon entre las fuerzas
k_1 = round((F_d(v_1) / F_g),1)
k_2 = round((F_d(v_2) / F_g),1)


# Muestra de valores

print('La fuerza gravitatoria es: ' + str(F_g) + 'N')
print('La fuerza de arrastre para un golpe suave: ' + str(round((F_d(v_1)),1)) + 'N')
print('La razón entre ambas fuerzas es: ' + str(k_1))
print('La fuerza de arrastre para un golpe fuerte: ' + str(round((F_d(v_2)),1)) + 'N')
print('La razón entre ambas fuerzas es: ' + str(k_2))