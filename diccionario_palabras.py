import doctest
import random
from typing import List

import tipos
from calculos import *

from main import LETRAS_CON_TILDES


def filtrar_diccionario(diccionario_crudo: dict[str, str], longitud_minima_palabras: int):
    '''
    Esta función genera el diccionario con todas las palabras disponibles para el juego, de acuerdo con el mínimo de caracteres
    requerido.

    Parámetros
    ----------
    diccionario_crudo : dict[str, str]
        Un diccionario cuyas claves son palabras y sus valores son las definiciones de esas palabras.
    longitud_minima_palabras : int
        La longitud mínima que se desea que tengan las palabras que participan en el juego.

    Retorna
    -------
    rosco
        El diccionario con las palabras disponibles para el juego.
        Lista de tuplas donde cada tupla tiene dos elementos; el primero es la palabra 'aplanada' y el segundo, su definición.

    Autores
    -------
    * Galvani, Juan Ignacio
    * Neme, Agustin Nadim
    '''
    diccionario_filtrado = {}
    for palabra, definicion in diccionario_crudo.items():
        if len(palabra) >= longitud_minima_palabras:
            palabra_aplanada = aplanar(palabra)
            diccionario_filtrado[palabra_aplanada] = definicion
    return diccionario_filtrado


def generar_letras_participantes(letras_permitidas: str, cantidad_de_letras: int, minimo_letras_posible: int, cantidad_de_palabras_por_letra: dict[str, int]):
    '''
    Genera una lista aleatoria a partir de las letras permitidas de forma aleatoria

    Parámetros
    ----------
    letras_permitidas : str
    cantidad_de_letras : int
    minimo_letras_posible : int
    cantidad_de_palabras_por_letra : int

    Retorna
    -------
    List[str]
        Una lista aleatoria de letras seleccionadas aleatoriamente.

    Autores
    -------
    * Galvani, Juan Ignacio
    * Neme, Agustin Nadim
    '''
    if minimo_letras_posible < cantidad_de_letras:
        seleccion = random.sample(list(cantidad_de_palabras_por_letra.keys()), minimo_letras_posible)
    else:
        seleccion = random.sample(letras_permitidas, cantidad_de_letras)
    seleccion_ordenada = ordenar_en_español(seleccion)
    return seleccion_ordenada


def generar_rosco(diccionario_como_lista: tipos.rosco, letras_participantes: List[str]) -> tipos.rosco:
    '''
    Retorna una lista de palabras seleccionadas aleatoriamente, donde cada palabra comienza con una de las letras participantes.

    Parámetros
    ----------
    diccionario_como_lista : rosco
        El diccionario de palabras participantes del juego.
        Lista de tuplas donde cada tupla tiene dos elementos; el primero es la palabra 'aplanada' y el segundo, su definición.
    letras_participantes : List[str]
        El listado de letras participantes en la partida. Deben estar ordenadas alfabéticamente.

    Retorna
    -------
    rosroscoco
        Un rosco conformado por palabras y definiciones obtenidos a partir del diccionario de palabras participantes.
        Lista de tuplas donde cada tupla tiene dos elementos; el primero es la palabra 'aplanada' y el segundo, su definición.

    Autores
    -------
    * Galvani, Juan Ignacio
    * Neme, Agustin Nadim
    '''
    lista_palabras_participantes = []

    for letra in letras_participantes:
        palabras_candidatas = []
        for palabra, definicion in diccionario_como_lista:
            palabra_aplanada = aplanar(palabra)
            if palabra_aplanada[0] == letra:
                palabras_candidatas.append([palabra, definicion])
        palabra_para_esta_letra = random.choice(
            palabras_candidatas) if len(palabras_candidatas) != 0 else None
        if palabra_para_esta_letra is not None:
            lista_palabras_participantes.append(palabra_para_esta_letra)

    return sorted(lista_palabras_participantes, key=lambda i: LETRAS_CON_TILDES.find(i[0][0]))


if __name__ == '__main__':
    print(doctest.testmod())
