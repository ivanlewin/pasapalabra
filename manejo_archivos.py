from diccionario_palabras import *
CORTE = ""


def abrir_linea(archivo, es_csv=False):

    linea = archivo.readline().rstrip() if not es_csv else archivo.readline().rstrip().split(",")

    if not linea:
        linea = CORTE
    return linea


def crear_diccionario():
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


def escribir_diccionario(diccionario):
    archivo_csv = open("./archivos/diccionario.csv", "w", encoding="utf-8")
    diccionario_ordenado = dict(sorted(diccionario.items(), key=lambda x: x[0]))

    for palabra, definicion in diccionario_ordenado.items():
        linea_escribir = f"{palabra},{definicion}\n"
        archivo_csv.write(linea_escribir)

    archivo_csv.close()


def hacerlo_lista(diccionario):
    lista = [[k, v] for k, v in diccionario.items()]
    lista = sorted(lista, key=lambda x: x[0])
    return lista
