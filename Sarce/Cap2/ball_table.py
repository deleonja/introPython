# Ingresa el numero de valores
n = int(input('Ingrese el numero de intervalor: '))         # numero de intervalos

v_o = float(input('Ingrese la velocidad inicial: '))        # velocidad inicial
g = 9.8 #m/s^2      gravedad
# Intervalo
a = 0               # tiempo inicial
b = 2*v_o / g       # tiempo final

# separacion
h = (b-a) / n       # separacion entre cada intervalo
print(' t | y ')    # Encabesado de la tabla

# Tabla con for

for i in range(n+1):
    t = a + i*h
    y = (v_o *t) - (0.5 * g * t**2)
    print(round(t,2), '|', round(y,2))
    if (t <= b) or (y >= 0):      # Para hacer que termine cuando el tiempo iguale el tiempo final
        continue
    else:
        break

print('-------------------')

# Tabla con while

i = 0

print(' t | y ')

while (i <= (n)):
    t = a + i*h
    y = (v_o *t) - (0.5 * g * t**2)
    print(round(t,2), '|', round(y,2))
    i += 1

print('-------------------')