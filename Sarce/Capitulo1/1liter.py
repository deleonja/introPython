# Cantidad en litros
litros = float(input('Cantidad de litros: '))

# Conversion de litros a cc
cc = litros / 1000

# Tomando las densidades de cada material/sustancia
iron = 7.8
air = 0.0012
gasoline = 0.67
ice = 0.9
human_body = 1.03
silver = 10.5
platinium = 21.4

# Encontrando la masa m=\rho * V
masa_iron = round((iron * cc),5)
masa_air = round((air * cc),10)
masa_gasoline = round((gasoline * cc),5)
masa_ice = round((ice * cc),5)
masa_human_body = round((human_body * cc),5)
masa_silver = round((silver * cc),5)
masa_platinium = round((platinium * cc),5)

#Mostrando los valores
print('Masa del hierro: ' + str(masa_iron) + 'g')
print('Masa del aire: ' + str(masa_air) + 'g')
print('Masa del gasolina: ' + str(masa_gasoline) + 'g')
print('Masa del hielo: ' + str(masa_ice) + 'g')
print('Masa del cuerpo humano: ' + str(masa_human_body) + 'g')
print('Masa del plata: ' + str(masa_silver) + 'g')
print('Masa del platinum: ' + str(masa_platinium) + 'g')

