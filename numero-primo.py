# imprimir los numeros primos entre 0 y 100

value = 0

for number in range(2, 100):
    es_primo = True
    for posible_divisor in range(2, number):
        # print("{} / {} = 1".format(number, value))
        if number % posible_divisor == 0:
            es_primo = False
            break
    if es_primo:
        print(number)


