import random

from datos import obtener_lista_definiciones

MINIMO_CARACTERES_PALABRAS = 5
LETRAS_SIN_TILDES = 'abcdefghijklmnñopqrstuvwxyz'
LETRAS_CON_TILDES = 'aábcdeéfghiíjklmnñoópqrstuúvwxyz'


def ordenar_filtrar_lista_de_listas():
    """
    Filtra de acuerdo a minimo de caracteres que debe tener la palabra y ordena alfabeticamente.

    Parametro:
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


def sacar_tildes(letra):
    '''
    Reemplaza las vocales acentuadas por mismas vocales no acentuadas
    '''
    return letra.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')


def cantidad_palabras_por_letra(letra : chr, lista : list[list[str]]):
    """
    Retorna la cantidad de palabras por letra recibida por parametro dentro de la lista de listas

    Parametro:
        letra : 'chr' Aquella letra que se solicite saber que la cantidad que hay
        lista : 'list[str]' Una lista con dos strings, el primero es la palabara y el segundo la definicion de la palabra.

    Retorna:
        En un int, el numero de veces que se ha encontrado la palabra comenzada con el parametro 'letra' que se envio.

    Autores:
        * Galvani, Juan Ignacio
        * Neme, Agustin Nadim
    """
    palabras_con_letra = []

    for palabra in lista:
        primera_letra = palabra[0][0]
        primera_letra_sin_tildes = sacar_tildes(primera_letra)
        if primera_letra_sin_tildes == letra:
            palabras_con_letra.append(palabra)

    cant_palabras_con_letra = len(palabras_con_letra)

    return cant_palabras_con_letra


def total_palabras_en_lista_de_listas():
    """
    Llamado a funcion cantidad_palabras_por_letra(), suma la cantidad de palabras que hay en total dentro de la lista de listas.
    Parametros:
        No recibe
    Retorna:
        En un int, el numero total de palabras que se encuentran a lo largo de toda la lista de listas, luego de ser filtrada por caracteres mayores o iguales a 5 caracteres.

    Autores:
        * Galvani, Juan Ignacio
        * Neme, Agustin Nadim
    """

    total = 0
    lista_ordenada = ordenar_filtrar_lista_de_listas()
    for letra in LETRAS_SIN_TILDES:
        total += cantidad_palabras_por_letra(letra, lista_ordenada)

    return total


def total_palabras_por_letra():
    """
    Muestra diccionario con cantidad de palabras por letra que hay en el diccionario filtrado.
    Parametros:
        No recibe
    Retorna:
        Diccionario con clave : letra y valor : cantidad de veces que una palabra comienza con la letra

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

    Parametros:
        No recibe

    Retorna:
        Lista de 10 letras aleatorias permitidas para el rosco

    Autores:
        * Galvani, Juan Ignacio
        * Neme, Agustin Nadim
    """
    
    return random.sample(LETRAS_SIN_TILDES, 10)


def recibir_lista_definiciones_filtrado(lista_definiciones_filtrada : list[list[str]], letras_participantes : list[str]):
    '''
    Parametro:
        lista_definiciones_filtrada 'list[str]': 
        letras_participantes 'list[str]' : Una lista que contiene letras aleatorias permitidas para usar en el rosco.
    Retorna:
        'list' : Una lista de definiciones validas para jugar ordenadas de forma alfabetica, unicamente con aquellas palabras dentro 'letras_parcipantes'.

    Autores:
        * Galvani, Juan Ignacio
        * Neme, Agustin Nadim
    '''

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