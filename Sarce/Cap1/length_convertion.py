# El usuario brinda la cantidad en metros
metros = input('Ingrese la cantidad en metros: ')
metros = float(metros)

# Conversión a centimetros
centimetros = round((metros *100),2)

# Conversion a pulgadas
inches = round((centimetros / 2.54),2)

# Conversion a pies
foots = round((inches / 12),2)

# Conversion a yardas
yards = round((foots / 3),2)

# Conversion a millas inglesas
miles = round((yards / 1760),2)


print('Unidad en pulgadas: ' + str(inches) + 'in')
print('Unidad en pies: ' + str(foots) + 'ft')
print('Unidad en yardas: ' + str(yards) + 'yd')
print('Unidad en millas: ' + str(miles) + 'mi')