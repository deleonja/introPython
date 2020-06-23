# Definimos n como un numero ingresado por el usuario
n = int(input('Ingrese un numero: '))
x = 0

# Se realia la suma
for i in range(n+1):
    x = x + i

# Se imprime
print(x)

#se toma la formula de gauss
x_gauss = (n*(n+1))/2
print(x_gauss)

# Los valores son iguales?
print(x == x_gauss)     # imprime un booleano