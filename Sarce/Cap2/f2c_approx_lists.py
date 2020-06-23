# Definimos las listas
List_F = []         # lista para valores en F
List_C = []         # lista para valores en centígrados
List_C_approx = []  # lista para lso valores aproximados

print('------------------') # table heading
F = 0 # start value for C
dF = 10 # increment of C in loop
while F <= 100: # loop heading with condition
    C = round(((5 / 9)*(F - 32)),3) # Conversion a centigrados
    C_approx = (1/2)*(F-30)         # aproximacion
    List_F.append(F)                
    List_C.append(C)
    List_C_approx.append(C_approx)  # se añaden los valores a cada lista
    F = F + dF # 3rd statement inside loop
print('------------------') # end of table line (after loop)

# se imprimen las listas
print(List_F)
print()
print(List_C)
print()
print(List_C_approx)

# Lista global para cada valor en las 2 unidades de medidas
conversion = []

for i in range(10):
    conversion.append([List_F[i],List_C[i],List_C_approx[i]])   # se añaden a la lista global

print('-----------------------')

for i in range(len(conversion)):
    print(conversion[i])