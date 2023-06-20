CORTE = ""


def abrir_linea(archivo, es_csv=False):
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
    linea = archivo.readline().rstrip() if not es_csv else archivo.readline().rstrip().split(",")

    if not linea:
        linea = CORTE
    return linea


def crear_diccionario():
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


def crear_csv(diccionario):
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
    diccionario_ordenado = dict(sorted(diccionario.items(), key=lambda x: x[0]))

    for palabra, definicion in diccionario_ordenado.items():
        linea_escribir = f"{palabra},{definicion}\n"
        archivo_csv.write(linea_escribir)

    archivo_csv.close()


def hacerlo_lista(diccionario):
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
    """
    lista = [[k, v] for k, v in diccionario.items()]
    lista = sorted(lista, key=lambda x: x[0])

    return lista
