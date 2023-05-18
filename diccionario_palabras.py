import doctest
import random

from datos import obtener_lista_definiciones

MINIMO_CARACTERES_PALABRAS = 5
LETRAS_SIN_TILDES = 'abcdefghijklmnñopqrstuvwxyz'
LETRAS_CON_TILDES = 'aábcdeéfghiíjklmnñoópqrstuúvwxyz'


def ordenar_filtrar_lista_de_listas():
    """
    Filtra de acuerdo a minimo de caracteres que debe tener la palabra y ordena alfabeticamente.

    Parámetros:
        No recibe ningun parametro, manipula la lista de listas provista en la consigna.

    Retorna:
        Lista de listas con aquellas palabras que tengan una longitud mayor o igual a 5 caracteres.

    Autores:
        * Galvani, Juan Ignacio
        * Neme, Agustin Nadim
    """
    lista_sin_orden = obtener_lista_definiciones()
    lista_con5_caracteres = []

    for palabra in lista_sin_orden:
        if len(palabra[0]) >= MINIMO_CARACTERES_PALABRAS:
            lista_con5_caracteres.append(palabra)

    lista = sorted(lista_con5_caracteres, key=lambda x: x[0])

    return lista


def sacar_tildes(texto):
    """
    Reemplaza las vocales acentuadas por mismas vocales no acentuadas en el texto ingresado.

    Parámetros:
        * texto `str`: El texto que se desea obtener sin tildes.

    Retorna:  
        `str`. En caso de que el texto sea una vocal, lo retorna sin tildes. Caso contrario, retorna el mismo texto ingresada.

    Autores:
        * Galvani, Juan Ignacio
        * Neme, Agustin Nadim

    >>> sacar_tildes("néctar")
    'nectar'
    >>> sacar_tildes("vaivén")
    'vaiven'
    >>> sacar_tildes("yesería")
    'yeseria'
    >>> sacar_tildes("vacilación")
    'vacilacion'
    >>> sacar_tildes("búho")
    'buho'
    """
    return texto.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')


def cantidad_palabras_por_letra(letra: str, lista: list[list[str]]):
    """
    Retorna la cantidad de palabras que empiezan con la letra provista. No tiene en cuenta las tildes.

    Parámetros:
        * letra `str`: Una cadena de longitud 1. Debe ser una letra del alfabeto en español.
        * lista `list[list[str]]`: Una lista de listas. En cada lista anidada, el primer elemento es una palabara y el segundo, la definición de la misma.

    Retorna:
        `int`. El número de palabras que comienzan con la letra provista, sin tener en cuenta las tildes.

    Autores:
        * Galvani, Juan Ignacio
        * Neme, Agustin Nadim

    >>> cantidad_palabras_por_letra('a', [['arbol', '...'], ['barro', '....'], ['árbitro', '...'], ['araña', '...']])
    3
    >>> cantidad_palabras_por_letra('b', [['arbol', '...'], ['barro', '....'], ['árbitro', '...'], ['araña', '...']])
    1
    >>> cantidad_palabras_por_letra('c', [['arbol', '...'], ['barro', '....'], ['árbitro', '...'], ['araña', '...']])
    0
    """
    palabras_con_letra = []

    for palabra in lista:
        primera_letra = palabra[0][0]
        primera_letra_sin_tildes = sacar_tildes(primera_letra)
        if primera_letra_sin_tildes == letra:
            palabras_con_letra.append(palabra)

    cant_palabras_con_letra = len(palabras_con_letra)

    return cant_palabras_con_letra


def total_palabras_en_diccionario():
    """
    Llamado a funcion cantidad_palabras_por_letra(), suma la cantidad de palabras que hay en total dentro de la lista de listas.

    Parámetros:
        No recibe

    Retorna:
        `int`. El número total de palabras que se encuentran a lo largo de toda la lista de listas, de longitud igual o mayor a 5.

    Autores:
        * Galvani, Juan Ignacio
        * Neme, Agustin Nadim
    """
    total = 0
    lista_ordenada = ordenar_filtrar_lista_de_listas()
    for letra in LETRAS_CON_TILDES:
        total += cantidad_palabras_por_letra(letra, lista_ordenada)

    return total


def total_palabras_por_letra():
    """
    Muestra diccionario con cantidad de palabras por letra que hay en el diccionario filtrado.

    Parámetros:
        No recibe

    Retorna:
        `dict`. Diccionario con clave 'letra' y valor : 'cantidad de veces que una palabra comienza con la letra'

    Autores:
        * Galvani, Juan Ignacio
        * Neme, Agustin Nadim
    """

    dicc = {}
    lista_ordenada = ordenar_filtrar_lista_de_listas()

    for letra in LETRAS_SIN_TILDES:
        dicc[letra] = cantidad_palabras_por_letra(letra, lista_ordenada)

    return dicc


def obtener_letras_participantes():
    """
    Crear una lista de 10 letras aleatorias de la lista de letras permitidas para el rosco.

    Parámetros:
        No recibe

    Retorna:
        Lista de 10 letras aleatorias permitidas para el rosco

    Autores:
        * Galvani, Juan Ignacio
        * Neme, Agustin Nadim
    """

    return random.sample(LETRAS_SIN_TILDES, 10)


def recibir_lista_definiciones_filtrado(lista_definiciones_filtrada: list[list[str]], letras_participantes: list[str]):
    """
    Retorna una lista de palabras seleccionadas aleatoriamente, donde cada palabra comienza con una de las letras participantes.

    Parámetros:
        lista_definiciones_filtrada 'list[str]': 
        letras_participantes 'list[str]' : Una lista que contiene letras aleatorias permitidas para usar en el rosco.

    Retorna:
        'list' : Una lista de definiciones validas para jugar ordenadas de forma alfabetica, unicamente con aquellas palabras dentro 'letras_parcipantes'.

    Autores:
        * Galvani, Juan Ignacio
        * Neme, Agustin Nadim
    """

    lista_palabras_participantes = []

    for letra in letras_participantes:
        palabras_candidatas = []

        for item in lista_definiciones_filtrada:

            palabra = item[0]
            palabra_sin_tildes = sacar_tildes(palabra)

            if palabra_sin_tildes[0] == letra:
                definicion = item[1]
                palabras_candidatas.append([palabra, definicion])

        palabra_para_esta_letra = random.choice(palabras_candidatas)
        lista_palabras_participantes.append(palabra_para_esta_letra)

    return sorted(lista_palabras_participantes, key=lambda i: LETRAS_CON_TILDES.index(i[0][0]))


# FUNCION QUE ITERA 100 VECES PARA PRUEBAS
"""
FUNCION QUE ITERA 100 VECES PARA PRUEBAS
for i in range(100):
    lista_letras2 = obtener_letras_participantes()
    diccionario_filtrado = ordenar_filtrar_diccionario()
    print(recibir_lista_diccionario_filtrado(diccionario_filtrado,lista_letras2))

"""

if __name__ == '__main__':
    print(doctest.testmod())
