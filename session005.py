import funcion_producto_de_kronecker as kron

# 2. Se definen las matrices      EL USUARIO SOLO INGRESA LAS MATRICES
Matriz_1 = [[1,1],[1,1]] # Matriz de mxn
Matriz_2 = [[1,0],[0,1]] # Matriz de pxq

    # 2.1. Se definen las dimensiones de las matrices
m = len(Matriz_1)
n = len(Matriz_1[0])
p = len(Matriz_2)
q = len(Matriz_2[0])


# 3. Se valúa la función
kron.pKronecker(n=n,m=m,p=p,q=q,M_1=Matriz_2, M_2=Matriz_1)
