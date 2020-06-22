M1 = [[1,0],[0,1]]
M2 = [[1,0],[0,1]]

resultado = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

p = 2
q = 2

for i in range(2):
    for j in range(2):
        for k in range(2):
            for l in range(2):
                alpha = p*(i) + k
                beta = q*(j) + l
                print(alpha, beta)
                resultado[alpha][beta] = M1[i][j]*M2[k][l]

print(resultado)
