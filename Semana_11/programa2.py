def sort_row(ejemplo2, row_index):
    if row_index < 0 or row_index >= len(ejemplo2):
        print("Índice de fila fuera de rango")
        return

    ejemplo2[row_index] = sorted(ejemplo2[row_index])

# Array bidimencional de 3x3

ejemplo2  = [
    [3,  7,  2],

    [5,  1,  4],

    [9,  0,  3]
]
# Ordenar la segunda fila (índice 1)

row_index = 1

print("Matriz antes de ordenar:")
for row in ejemplo2:
    print(row)

sort_row(ejemplo2, row_index)

print("\nMatriz después de ordenar la fila", row_index, "en orden ascendente:")
for row in ejemplo2:
    print(row)