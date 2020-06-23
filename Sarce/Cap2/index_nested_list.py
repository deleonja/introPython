q = [['a', 'b' ,'c'], ['d', 'e', 'f'], ['g', 'h']]

# Inciso a
print(q[0][0])          # primer elemento de la primera sublista
print(q[1])             # segunda sublista
print(q[2][1])          # segundo elemento de la tercera sublista
print(q[1][0])          # primer elemento de la segunda sublista
print(q[-1][-2])        # el negativo toma desde el final de la lista

print('---------')
# Inciso b
for i in q:
    for j in range(len(i)):
        print(i[j])