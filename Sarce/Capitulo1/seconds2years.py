# Se denomina la variable de segundos
segundos = 10**9

# Conversion a minutos
minutos = segundos / 60

# Conversion a horas
horas = minutos / 60

# Conversion a dias
dias = horas / 24

# Conversion a años
años = dias / 365
años = int(años)

if años > 82:
    print('El bebé no tiene esperanza de vivir tanto xd')
else:

    print('El bebe tiene la posibilidad de vivir ' + str(años) + ' años')