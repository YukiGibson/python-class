
# Los nombres de las clases son lo unico que utiliza CamelCase


class Estudio(object):

    # Constructor en Python
    # Los constructores son los metodos que utilizamos para crear instancias
    # a partir de una clase. Y son los que realizan la inicializacion
    # El constructor tiene como responsabilidad la inicializacion de la clase.
    def __init__(self, institution, degree, year_of_completion, completed=False):
        self.__institucion = institution
        self.__completed = completed
        self.__degree = degree
        self.__year_of_completion = year_of_completion

    def as_dictionary(self):
        return {
            "institution": self.__institucion,
            "completed": self.__completed,
            "degree": self.__degree,
            "year_of_completion": self.__year_of_completion
        }

    def set_as_imcomplete(self):
        self.__completed = False


# el valor de estudio es una instancia de la clase Estudio, por lo tanto un objeto
estudio_en_harvard = Estudio(
    institution="Harvard",
    completed=True,
    degree="Bachelor Degree in physics",
    year_of_completion=2018
)

print(estudio_en_harvard.as_dictionary())
estudio_en_harvard.set_as_imcomplete()
print(estudio_en_harvard.as_dictionary())


