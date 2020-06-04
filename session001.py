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
