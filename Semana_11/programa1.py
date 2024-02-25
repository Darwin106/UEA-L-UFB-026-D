# array bidimensionales ejercicio 1

ejemplo_array = [
#   0,   1,     2 Columna

    [8,  6,    6], # 0 Fila

    [9,  17,   77],  # 1

    [21, 9,    54]]  # 2


def buscar(ejemplo_array, valor):
    for i in range(len(ejemplo_array)):
        for j in range(len(ejemplo_array[i])):
            if ejemplo_array[i][j] == valor:
                return f"El valor {valor} , se encontro en la posión ({i}, {j})."
    return f"El valor {valor}, no se encontro en la matriz"


# Valor a buscarr

valor_a_buscar = 8

# Llamada a la función para buscar el valor
resul = buscar(ejemplo_array, valor_a_buscar)

print(resul)