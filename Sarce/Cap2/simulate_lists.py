a = [1, 3, 5, 7, 11]
b = [13, 17]
c = a + b # Lista a con los elementos de b como sus ultimos
print(c) # lo mencionado arriba
b[0] = -1 # cambia el primer valor por -1
d = [e+1 for e in a] # toma la lista d como cada elemento de la lista a +1
print(d)
d.append(b[0] + 1) # Añade el primer termino de b mas 1 al ultimo termino de d
d.append(b[-1] + 1) # Toma el ultimo termino de d mas 1 y lo agrega a d
print(d[-2:]) # imprime los ultimos dos terminos de d en lista
for e1 in a:
    for e2 in b:
        print(e1 + e2) #suma cada elemento de a con cada elemento de b