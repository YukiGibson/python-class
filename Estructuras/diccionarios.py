import pprint


# vamos a empeazar declarando un diccionario vacio
diccionario_vacio = {}

# un diccionario con valores establecidos como literales
datos_personales = {
    "nombre": "John",
    "apellido": "Smith",
    "edad": 20,
    "carreras": [
        "Computacion",
        "Fisica"
    ],
    "universidad": {
        "nombre": "Universidad Super Patito",
        "fundacion": 2001
    }
}

print(datos_personales.keys())

# ahora vamos a acceder a los valores del diccionario

print(datos_personales["nombre"])

datos_personales["nombre"] = "Jane"

# agregar una nueva llave
datos_personales["email"] = "jane.smith@example.com"

pprint.pprint(datos_personales)

# vamos a imprimir todos los valores del diccinario

for key in datos_personales.keys():
    print(datos_personales[key])


# un diccionario dentro de otro diccionario
print(datos_personales["universidad"]["nombre"])

# lista dentro de un diccionario
print(datos_personales["carreras"][0])

print("*************************************\n")

"""

"""
