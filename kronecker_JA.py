M1 = [[1,0],[0,1]]
M2 = [[1,0],[0,1]]

resultado = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
resultado2 = [[0]*4]*4

print(resultado2)
print()

m = len(M1)
n = len(M1[0])
p = len(M2)
q = len(M2[0])

for i in range(m):
    for j in range(n):
        for k in range(p):
            for l in range(q):
                alpha = p*(i) + k
                beta = q*(j) + l
                #print(alpha, beta)
                resultado[alpha][beta] = M1[i][j]*M2[k][l]
                resultado2[alpha][beta] = M1[i][j]*M2[k][l]

print(resultado)
print(resultado2)
