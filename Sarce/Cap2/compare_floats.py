import math                             # Para tener notacion cientifica
from math import *

# copiamos el codigo

a = 1/947.0*947
b = 1
if a != b:
    print('Wrong result!')

tol = 1E-100                            # Numero muy pequeño para comparar con la resta

if abs(a-b) < tol:
    print('Wrong result!')
else:
    None                                # si el programa no imprime "wrong result!" se sabra que funciono