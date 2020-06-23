from math import sqrt
for n in range(1, 60):
    r = 2
for i in range(n):
    r = sqrt(r)
for i in range(n):
    r = r**2
print('%d times sqrt and **2: %.16f' % (n, r))

# El resultado es 1 debido a que al realizar las 59 raices cuadradas el programa aproxima el resultado a 1
# y al elevarlo 59 veces 1, el resultado es 1