
s = 0           # valor inicial de la suma
k = 1           # se define el contador
M = 100         # limite superior de la suma

# se realiza la suma, para elementos entre 1 y 100
while k <= M:
    s += 1/k
    k += 1

# se imprime el valor total
print(s)