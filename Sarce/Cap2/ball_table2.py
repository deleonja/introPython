# Ingresa el numero de valores
n = int(input('Ingrese el numero de intervalor: '))     


v_o = float(input('Ingrese la velocidad inicial: '))    # velocidad incial
g = 9.8 #m/s    gravedad
# Intervalo
a = 0                   # tiempo incial
b = 2*v_o / g           # tiempo final

# separacion de los intervalos
h = (b-a) / n


# Listas vacias para ingresar los valores

Lista_t = []                # lista para los datos del tiempo
Lista_y = []                # lista para los datos de la posicion

# Añadiendo los datos a las listas

for i in range(n+1):
    t = round((a + i*h),4)
    y = round(((v_o *t) - (0.5 * g * t**2)),4)
    Lista_t.append(t)
    Lista_y.append(y)
    if (t <= b) or (y >= 0):
        continue
    else:
        break

print(Lista_t)
print(Lista_y)

# Tabla imprimiendo uno a uno los datos de las listas
print(' t | y ')

for i in range(len(Lista_t)):
    print(Lista_t[i], '|', Lista_y[i])

print('-------------------')

