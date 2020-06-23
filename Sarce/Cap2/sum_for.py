# se define el valor inicial de la suma
s = 0

# se suman todos los inversos de los numeros entre 1 y 100
for i in range(1,101):
    s += 1/i        # no es un contador, "s" guarda la sumatoria

# se imprime el valor final
print(s)