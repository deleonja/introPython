# Monto inicial
A = float(input('Monto inicial: '))

# tasa de interes por año
p = float(input('Tasa de interes por año: '))

# cantidad de años
n = int(input('Número de años: '))

C = round((A*(1+(p/100))**n),2)

print('La cantidad que tiene luego de ' + str(n) + ' años, es: ' + str(C) + ' euros.')
