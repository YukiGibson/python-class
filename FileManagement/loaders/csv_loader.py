import csv


class CsvLoader(object):

    # ------------------------------------------------------
    # Constructor de la clase
    # ------------------------------------------------------

    def __init__(self, file_name):

        # Guardamos el nombre del archivo para que este disponible para
        # que los metodos esten dispobibles para los que lo requieran en esta clase
        self.__file_name = file_name

        # inicializamos una lista vacia como atributo
        # porque necesitamos un lugar para colocar los diccionarios que
        # representan cada una de las filas de archivo CSV
        self.__rows = []

        # Ahora leemos el archivo y lo convertimos en una lista de diccionarios.
        self.__read_csv_file(self.__file_name)

    # ------------------------------------------------------
    # read csv file
    # ------------------------------------------------------
    def __read_csv_file(self, file_name):

        # Using with always ends with a name (f in this case)
        # with this you are opening a stream of data
        # and f will be available inside this with:

        with open('file_path') as file:

            # esta expresion generadora llena un diccionario y luego
            # llena una lista y el diccionario de dentro hacia afuera.

            parsed_data = [{k: v for k, v in row.items()} # Expresion generadora
                           for row in csv.DictReader(file, skipinitialspace=True)]

    # Esto es un decorator
    # El output de rows() va a property() y el resultado de esta
    # metodo sera devuelta
    # La razon de esto es que Python manda las funciones por referencia
    # entonces con property acceden una copia de esta funcion, por seguridad.
    @property
    def rows(self):
        return self.__rows