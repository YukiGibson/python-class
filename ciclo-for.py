print(range(10))

cantidad = 0

for numero in range(5, 27):
    if numero % 2 == 1:
        print(numero)
        cantidad = cantidad + 1


print("Numeros impares: {}".format(cantidad))