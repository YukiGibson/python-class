curriculum = {
    "nombre": "Laureano",
    "apellido": "Sanchez",
    "edad": 23,
    "ciudad": "San Jose",
    "educacion": [
        {
            "institucion_educativa": "colegio dos cercas",
            "anno_finalizacion": 2013,
            "grado_academico": "bachiller"
        }, {
            "institucion_educativa": "ulacit",
            "anno_finalizacion": 2017,
            "grado_academico": "bachillerato en ingenieria informatica"
        }
    ],
    "experiencia": [
        {
            "empresa": "deposito las gravilias",
            "puesto": "tesorero",
            "anno de inicio": 2014,
            "anno de finalizacion": 2014,
            "trabajo_actual": False,
            "descripcion": "Tesorero en departamento de contabilidad"
        }, {
            "empresa": "imprenta vargas",
            "puesto": "analista programador",
            "anno de inicio": 2017,
            "anno de finalizacion": 2018,
            "trabajo_actual": False,
            "descripcion": "programador de sistemas web y de escritorio"
        }, {
            "empresa": "Microsoft",
            "puesto": "Support Engineer",
            "anno de inicio": 2018,
            "trabajo_actual": True,
            "descripcion": "Soporte Tecnico en Microsoft"
        }
    ]
}
# el caso en que el trabajo sea un trabajo finalizado


def calcular_annos_para_trabajo_finalizado(trabajo):
    return trabajo["anno de finalizacion"] - trabajo["anno de inicio"]


def calcular_annos_para_trabajo_actual(trabajo, ano_actual):
    return ano_actual - trabajo["anno de inicio"]


# funcion coordinadora
def obtener_total_annos_para_trabajo(trabajo, ano_actual):
    if trabajo["trabajo_actual"]:
        return calcular_annos_para_trabajo_actual(trabajo, ano_actual)
    else:
        return calcular_annos_para_trabajo_finalizado(trabajo)


def obtener_cantidad_de_empleos(el_curriculum):
    if "experiencia" in el_curriculum:
        return len(el_curriculum["experiencia"])
    else:
        return 0


def obtenga_total_annos_trabajados(el_curriculum, anno_actual):
    total_annos_laborados = 0
    for trabajo in el_curriculum["experiencia"]:
        total_annos_laborados += obtener_total_annos_para_trabajo(trabajo, anno_actual)
    return total_annos_laborados


# print(obtener_cantidad_de_empleos(curriculum))
print(obtenga_total_annos_trabajados(curriculum, 2018))

