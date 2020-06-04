# 04 de junio, 2020
# Autor: José Alfredo de León 

# En esta sesión se platicó sobre el capítulo 1 del libro 
# y se realizó este ejemplo para ilustrar un programa 
# sencillo utilizando buenas prácticas de programación.

# Cosas importantes: 
#
# 1. Antes de escribir el código pensar en el algoritmo.
# 2. Escribir el algoritmo comentado. 
# 3. Finalmente escribir el código según los pasos del 
# algoritmo. 

# Importar sys para poder leer desde terminal los números
import sys

# 1. Pedir el primer numero
primer_numero = sys.argv[1]
primer_numero = float(primer_numero)

# 2. Pedir el segundo número
segundo_numero = float(sys.argv[2])

# 3. Efectuar la suma
suma = primer_numero + segundo_numero

# 4. Imprimir la suma
print("Suma1 = " + str(suma))
print("Suma2 = %2.0f" % suma)
print("Suma3 = %3.1f" % suma)


# Ejemplo: poner en terminal 'python3 session001.py 10.2 + 15.7'
#
# En terminal aparecerá:
# Suma1 = 25.9
# Suma2 = 26
# Suma3 = 25.9
# 
#

# Recordatorio: 
# Se accede a la shell interactiva de python colocando en la 
# terminal 'python3'

