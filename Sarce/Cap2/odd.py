# Definimos n como un numero ingresado por el usuario
n = int(input('Ingrese un numero: '))

# Definimos el contador
count = 1

# por definicion de numero impar, todo numero con modulo 2 que de 1, es impar y se imprime, de lo contrario no hace nada
while count <= n:
    if count % 2 == 1:
        print(count)
    else: 
        None
    count = count + 1