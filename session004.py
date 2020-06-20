#   En este programa se da un breve ejemplo de cómo definir una función en
#   python.

#   19.06.2020
#   J.A. de León

def makeList(a,b):
    '''
    Función para crear una lista con dos elementos.

    Argumentos:
    a: objeto de tipo int
    b: objeto de tipo int

    Retorna objeto de tipo lista.

    Ej: makeList(1,2) = [1,2]
    '''
    # 1. Revisar los argumentos
    if (type(a) != int):
        print('Se esperaba objeto de tipo int en el primer argumento')
        return

    if (type(b) != int):
        print('Se esperaba objeto de tipo int en el segundo argumento')
        return

    # 2. Crear una lista para guardar los argumentos
    List = []

    # 3. Añadir elementos a la lista
    List.append(a)
    List.append(b)

    # 4. Retornar la lista creada
    return List


# Uso de la función makeList
ListaPrueba1 = makeList(4,5)
print(ListaPrueba1)

print()

ListaPrueba2 = makeList('a',3)
#print(ListaPrueba2)


asdfljsdfljasdñfjqwoiehrqwenflñksahjdflkjasd
asdfljsdfljasdñfjqwoiehrqwenflñksahjdflkjasdasdfjalkñsdf
fasjdfñakldjs
fasdkljfalkdjsfls
