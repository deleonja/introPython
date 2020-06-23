#Importamos la libreria de funciones matematicas
import math
from math import *
#definimos las constantes
m = 0
s = 2
x = 1
#definimos la funcion
def f(y):
    return (1/(sqrt(2*pi) *s)) *exp(-0.5*((y-m)/s)**2)

#la valuamos
a = f(x)
#la imprimimos
print(a)