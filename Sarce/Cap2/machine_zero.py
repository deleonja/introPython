eps = 1.0                               # Se define eps
while 1.0 != 1.0 + eps:                 # Condiciones del ciclo
    print('...............', eps)         # Se imprime el valor de eps
    eps = eps/2.0                       # Como se modifica el valor de eps, y es el contador
print('final eps:', eps)                # Se imprime el valor final

# El programa al tener un contador que cada vuelta se divide entre dos, en la n-esima vuelta, el valor de eps seria 1/2^n
# para un n muy grande, el valor es demasiado pequeño, tal que la suma 1+eps es aproximadamente 1, y el programa se detiene