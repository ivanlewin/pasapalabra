import doctest
CORTE = ""


def abrir_linea(archivo):
    """
    Esta funcion lee linea por linea el archivo especificado

    Parámetros
    ----------
    archivo : TextIOWrapper
        El archivo que se quiere leer

    Retorna
    -------
    linea : list[str]
        Lista con la linea actual del archivo, si no hay mas lineas retorna vacio

    Autores
    -------
    * Brizuela, Natanael Daniel
    """
    linea = archivo.readline().rstrip()

    if not linea:
        linea = CORTE
    return linea


def crear_diccionario() -> dict:
    """
    Funcion encargada de crear el diccionario en base a los archivos "definiciones.txt" y "palabras.txt".

    Parámetros
    ----------
        No admite.

    Retorna
    -------
    diciconario: dict
        El diccionario con palabras y definiciones a utilizar durante el juego.

    Autores
    -------
    * Brizuela, Natanael Daniel
    """
    definiciones = open("./archivos/definiciones.txt", "r", encoding='utf-8')
    palabras = open("./archivos/palabras.txt", "r", encoding='utf-8')

    definicion = abrir_linea(definiciones)
    palabra = abrir_linea(palabras)
    diccionario = {}

    while definicion != CORTE:
        diccionario[palabra] = definicion

        definicion = abrir_linea(definiciones)
        palabra = abrir_linea(palabras)

    definiciones.close()
    palabras.close()

    return diccionario


def crear_csv(dicc_palabras_y_def: dict) -> None:
    """
    Funcion que se encarga de crear un archivo ordenado .scv en base al diccionario de palabras armado previamente.

    Parámetros
    ----------
    dicionario : dict.
        Diccionario de palabaras y definiciones.

    Retorna
    -------
    diciconario: dict
        El diccionario con palabras y definiciones a utilizar durante el juego.

    Autores
    -------
    * Brizuela, Natanael Daniel
    """
    archivo_csv = open("./archivos/diccionario.csv", "w", encoding="utf-8")
    diccionario_ordenado = dict(
        sorted(dicc_palabras_y_def.items(), key=lambda x: x[0]))

    for palabra, definicion in diccionario_ordenado.items():
        linea_escribir = f"{palabra},{definicion}\n"
        archivo_csv.write(linea_escribir)

    archivo_csv.close()


def hacerlo_lista(diccionario: dict) -> list:
    """
    Funcion que crea una lista de listas a partir de un diccionario de palabras y definciones

    Parámetros
    ----------
    dicionario : dict.
        Diccionario de palabaras y definiciones.

    Retorna
    -------
    lista : list[list[str]]
        lista de lista con palabras y definiciones.

    Autores
    -------
    * Brizuela, Natanael Daniel

    Ejemplos
    --------
    >>> hacerlo_lista({'circuito': 'm. Terreno comprendido dentro de un perímetro cualquiera'})
    [['circuito', 'm. Terreno comprendido dentro de un perímetro cualquiera']]
    >>> hacerlo_lista({'iluminar': 'tr. Alumbrar dar luz o bañar de resplandor'})
    [['iluminar', 'tr. Alumbrar dar luz o bañar de resplandor']]
    """
    lista = [[k, v] for k, v in diccionario.items()]
    lista = sorted(lista, key=lambda x: x[0])
    return lista


def validar_linea(diccionario: dict, linea: str):
    """
    Funcion que verifica que no haya error en la linea donde esta la configuracion y lo carga en el diccionario, si hay error no modifica el diccionario. 

    Parámetros
    ----------
    dicionario : dict.
        Diccionario de configuraciones.

    Retorna
    -------
    diccionario : dict.
        El diccionario con la configuracion del archivo dependiendo si es por defecto o por eleccion.

    Autores
    -------
    * Brizuela, Natanael Daniel

    Ejemplos
    --------
    >>> validar_linea({"LONGITUD_PALABRA_MINIMA": {"valor": 10, "origen": "Defecto"}},"LONGITUD_PALABRA_MINIMA,4")
    {'LONGITUD_PALABRA_MINIMA': {'valor': 4, 'origen': 'Eleccion'}}
    >>> validar_linea({"LONGITUD_PALABRA_MINIMA": {"valor": 10, "origen": "Defecto"}},"LONGITUD_PALABRA_MINIMA,d")
    {'LONGITUD_PALABRA_MINIMA': {'valor': 10, 'origen': 'Defecto'}}
    """
    nombre, valor = linea.split(",")

    try:
        if nombre in diccionario.keys():
            diccionario[nombre] = {"valor": int(
                valor), "origen": "Eleccion"}

    except ValueError:
        pass

    return diccionario


def crear_diccionario_configuracion() -> dict:
    """
    Funcion que crea el diccionario con la configuracion que se utilizara durante el juego. 

    Parámetros
    ----------
    arch_config : TextIOWrapper.
        Archivo de configuracion.

    Retorna
    -------
    diccionario : dict.
        El diccionario con la configuracion del archivo dependiendo si es por defecto o por eleccion.

    Autores
    -------
    * Brizuela, Natanael Daniel
    """
    arch_config = open("./archivos/configuracion.csv")

    linea = abrir_linea(arch_config)
    dicc_configuracion = {
        "LONGITUD_PALABRA_MINIMA": {"valor": 10, "origen": "Defecto"},
        "CANTIDAD_LETRAS_ROSCO": {"valor": 10, "origen": "Defecto"},
        "MAXIMO_PARTIDAS": {"valor": 5, "origen": "Defecto"},
        "PUNTAJE_ACIERTO": {"valor": 10, "origen": "Defecto"},
        "PUNTAJE_DESACIERTO": {"valor": 3, "origen": "Defecto"}
    }

    while linea != CORTE:

        dicc_configuracion = validar_linea(dicc_configuracion, linea)

        linea = abrir_linea(arch_config)

    arch_config.close()
    return dicc_configuracion


if __name__ == '__main__':
    print(doctest.testmod())
