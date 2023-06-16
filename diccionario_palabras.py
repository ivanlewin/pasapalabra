import doctest
import random
from typing import List

from archivos.datos import obtener_lista_definiciones
from main import LETRAS_CON_TILDES

def generar_diccionario(longitud_minima_palabras: int):
    """
    Esta función genera el diccionario con todas las palabras disponibles para el juego, de acuerdo con el mínimo de caracteres
    requerido.

    Parámetros
    ----------
    longitud_minima_palabras : int
        La mínima longitud que deben tener las palabras para que puedan ser incluidas en el diccionario.

    Retorna
    -------
    List[List[str]]
        El diccionario con las palabras disponibles para el juego.
        Es una lista de listas de strings. Cada sublista tiene dos elementos; el primero es la palabra "aplanada" y el segundo, su definición.

    Autores
    -------
    * Galvani, Juan Ignacio
    * Neme, Agustin Nadim
    """
    lista_definiciones = obtener_lista_definiciones()

    lista_aplanada = []
    for palabra, definicion in lista_definiciones:
        if len(palabra) >= longitud_minima_palabras:
            palabra_aplanada = aplanar(palabra)
            lista_aplanada.append([palabra_aplanada, definicion])

    lista = sorted(lista_aplanada, key=lambda x: x[0])

    return lista


def aplanar(texto: str):
    """
    Convierte el texto provisto a minúscula y elimina diéresis y tildes de las vocales.

    Parámetros
    ----------
    texto : str
        El texto que se desea aplanar.

    Retorna
    -------  
    str
        El texto aplanado.

    Autores
    -------
    * Galvani, Juan Ignacio
    * Neme, Agustin Nadim

    Ejemplos
    --------
    >>> aplanar("néctar")
    'nectar'
    >>> aplanar("vaivén")
    'vaiven'
    >>> aplanar("yesería")
    'yeseria'
    >>> aplanar("vacilación")
    'vacilacion'
    >>> aplanar("búho")
    'buho'
    >>> aplanar("PERRO")
    'perro'
    >>> aplanar("PiNgüInO")
    'pinguino'
    """

    return (
        texto
        .lower()
        .replace("á", "a")
        .replace("é", "e")
        .replace("í", "i")
        .replace("ó", "o")
        .replace("ú", "u")
        .replace("ä", "a")
        .replace("ë", "e")
        .replace("ï", "i")
        .replace("ö", "o")
        .replace("ü", "u")
    )


def calcular_cantidad_de_palabras_por_letra(diccionario_de_palabras: List[List[str]]):
    """
    Muestra diccionario con cantidad de palabras por letra que hay en el diccionario filtrado.

    Parámetros
    ----------
    diccionario_de_palabras : List[List[str]]
        El diccionario de palabras participantes del juego.
        Es una lista de listas de strings. Cada sublista tiene dos elementos; el primero es la palabra "aplanada" y el segundo, su definición.

    Retorna
    -------
    dict
        Un diccionario con la cantidad de palabras que comienzan por cada letra.
        Las claves del diccionario son cada una de las letras iniciales de las palabras presentes en `diccionario_de_palabras`
        y los valores son la cantidad de palabras que comienzan por cada una de esas letras.

    Autores
    -------
    * Galvani, Juan Ignacio
    * Neme, Agustin Nadim
    """

    cantidad_de_palabras_por_letra = {}

    for palabra, definicion in diccionario_de_palabras:
        letra_inicial = palabra[0]
        if letra_inicial in cantidad_de_palabras_por_letra:
            cantidad_de_palabras_por_letra[letra_inicial] = cantidad_de_palabras_por_letra[letra_inicial] + 1
        else:
            cantidad_de_palabras_por_letra[letra_inicial] = 1

    return cantidad_de_palabras_por_letra


def generar_letras_participantes(letras_permitidas: str, cantidad_de_letras: int):
    """
    Genera una lista aleatoria a partir de las letras permitidas de forma aleatoria

    Parámetros
    ----------
    letras_permitidas : str
        El listado de letras permitidas
    cantidad_de_letras : int
        El número de letras a obtener

    Retorna
    -------
    List[str]
        Una lista aleatoria de letras seleccionadas aleatoriamente.

    Autores
    -------
    * Galvani, Juan Ignacio
    * Neme, Agustin Nadim
    """
    seleccion = random.sample(letras_permitidas, cantidad_de_letras)
    return ordenar_en_español(seleccion)


def generar_rosco(diccionario_de_palabras: List[List[str]], letras_participantes: List[str]):
    """
    Retorna una lista de palabras seleccionadas aleatoriamente, donde cada palabra comienza con una de las letras participantes.

    Parámetros
    ----------
    diccionario_de_palabras : List[List[str]]
        El diccionario de palabras participantes del juego.
        Es una lista de listas de strings. Cada sublista tiene dos elementos; el primero es la palabra "aplanada" y el segundo, su definición.
    letras_participantes : List[str]
        El listado de letras participantes en la partida. Deben estar ordenadas alfabéticamente.

    Retorna
    -------
    List[List[str]]
        Un rosco conformado por palabras y definiciones obtenidos a partir del diccionario de palabras participantes.
        Es una lista de listas de strings. Cada sublista tiene dos elementos; el primero es la palabra "aplanada" y el segundo, su definición.

    Autores
    -------
    * Galvani, Juan Ignacio
    * Neme, Agustin Nadim
    """
    lista_palabras_participantes = []

    for letra in letras_participantes:
        palabras_candidatas = []
        for palabra, definicion in diccionario_de_palabras:
            palabra_aplanada = aplanar(palabra)
            if palabra_aplanada[0] == letra:
                palabras_candidatas.append([palabra, definicion])
        palabra_seleccionada = random.choice(palabras_candidatas)
        lista_palabras_participantes.append(palabra_seleccionada)

        palabra_para_esta_letra = random.choice(
            palabras_candidatas) if len(palabras_candidatas) != 0 else None
        if palabra_para_esta_letra is not None:
            lista_palabras_participantes.append(palabra_para_esta_letra)

    return sorted(lista_palabras_participantes, key=lambda i: LETRAS_CON_TILDES.find(i[0][0]))


def ordenar_en_español(iterable: str | List[str]):
    """
    Ordena un iterable alfabéticamente, teniendo en cuenta los diacríticos del español.
    Esto significa que el elemento "á" se ubicará luego del elemento "a", y no luego del elemento "z".

    Parámetros
    ----------
    iterable : str | List[str]

    Retorna
    -------
    str | List[str]
        El iterable ordenado teniendo en cuenta el alfabeto en español.

    Autores
    -------
    * Lewin, Iván
    """
    return sorted(iterable, key=lambda i: LETRAS_CON_TILDES.find(i))


if __name__ == "__main__":
    print(doctest.testmod())
