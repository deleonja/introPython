import math
from math import *
# declaran las constantes no se convierten al SI, puesto que el resultado seria el mismo
M_1 = 47 #g
M_2 = 67 #g
T_1 = 4 #°C
T_2 = 20 #°C
rho = 1.038 #g/cc
c = 3.7 #J/gK
K = 5.4E-3 #W/cmK
T_w = 100 #°C
T_y = 70 #°C


#se define la funcion
def t(M,T):
    return ((M**(2/3))*c*(rho**(1/3))/( ((4*pi/3)**(2/3))*K*pi**2 ))*log(0.76*((T -T_w)/(T_y -T_w)))

t(M_2,T_1)
t(M_2,T_2)

print('Tiempo de cocción para un huevote del refri: ' + str(round(t(M_2,T_1),2)) + 's')
print('Tiempo de cocción para un huevote a temperatura ambiente: ' + str(round(t(M_2,T_2),2)) + 's')