# Esto es una lista de numeros
lista_de_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
lista_vacia = []

lista_vacia.append("Hola")
lista_vacia.append("otro")

for numero in range(0, 50):
    lista_vacia.append(str(numero))

# print(lista_vacia[:])

# podemos consultar la cantidad de elementos que tiene una lista
# print(len(lista_vacia))

def print_matrix(matrix):
    output = ""
    for fila in matrix:
        output += str(fila) + "\n"
    return output


def dibuje_diagonal_en_matriz(matrix):
    for fila in range(0, len(matrix)):
        for columna in range(0, len(matrix[fila])):
            if fila == columna:
                matrix[fila][columna] = '@'
    return matrix

matrix = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]

print(print_matrix(matrix))
print(matrix[0][1])
# composicion de funciones
print(print_matrix(dibuje_diagonal_en_matriz(matrix)))

# con set, convertimos la lista en un conjunto
# teoria de conjuntos en mate, solo les preocupa la existencia de un valor
a = set([1, 2, 23, 34, 45, 67])
b = set([4, 3, 23, 76, 94, 101, 23])

# union de conjuntos
print(a.union(b))

# interseccion
print(a.intersection(b))

# diferencia
print(a.difference(b))