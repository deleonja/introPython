# Tomamos la lista vacia para ingresar los valores
lista_intervalos = []

# Se solicita al usuario que ingrese el intervalo
a = float(input('Ingrese el inicio del intervalo: '))
b = float(input('Ingrese el final del intervalo: '))

# Ingrese el numero de intervalos
n = int(input('Ingrese el numero de intervalos: '))

# Longitud de los intervalos
h = (b-a)/n

# Coordenadas
for i in range(n+1):
    lista_intervalos.append(a+i*h)

print(lista_intervalos)
