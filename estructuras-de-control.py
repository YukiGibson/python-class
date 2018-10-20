# Ejemplos de uso del if en python

esta_lloviendo = True
tenemos_hambre = False
python_es_genial = True
ayer_pagaron = False
vamos_a_la_playa = False

# Funcion para solicitar datos por consola input("mensaje")
# La funcion input siempre retorna un str
# Tenemos que convertirlo a numero antes de hacer operaciones numericas
numero_digitado = input("Digite un numero: ")
numero_digitado_como_numero = float(numero_digitado)

if esta_lloviendo and tenemos_hambre:
    # Este codigo esta dentro del if
    print("Esta lloviendo y tenemos hambre")
elif (12 < numero_digitado_como_numero and python_es_genial) or vamos_a_la_playa:
    print("Python es genial o vamos a la playa")
else: 
    print("Esto se ejecuta sin ninguna condicion anterior es verdadera")