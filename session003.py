# 1. Implementar un ciclo para guardar en dos listas los valores de t y y(t)
# utilizando la fórmula y(t) = v0*t + 1/2*g*t^2.

v0 = 55                         # velocidad inicial
g = 9.8                         # gravedad

n = 10                          # número de pedazos del intervalo [0,2*v0/g]

tMax = 2*v0/g                   # límite superior del intervalo de t

t = [0]*(n+2)                   # lista para almacenar los valores de t
y = [0]*(n+2)                   # lista para almacenar los valores de y(t)

dt = tMax/(n+1)                 # diferencial de tiempo

for i in range(1, n+2):         # sobre los n+1 pedazos de intervalo
    t[i] = t[i-1] + dt
    y[i] = v0*t[i] - 1/2*g*t[i]**2

for i in range(1, n+2):         # ciclo para redondear a dos decimales
    t[i] = round(t[i], 2)
    y[i] = round(y[i], 2)

# 2 Store data in a nested list
ty1 = []
ty1.append(t)
ty1.append(y)

ty2 = []
for i in range(len(t)):
    ty2.append([t[i], y[i]])

for row in ty2:
    print(row)
