from datos import obtener_lista_definiciones
import random


MINIMO_CARACTERES_PALABRAS = 5
LETRAS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 

def ordenar_filtrar_diccionario():
    '''
    Se recibe un lista de listas desordenada con palabras y sus definiciones.
    Filtra de acuerdo a minimo de caracteres que debe tener la palabra y ordena alfabeticamente.
    Retorna lista ordenada y filtrada.
    '''
    lista_sin_orden = obtener_lista_definiciones()
    lista_con5_caracteres = []

    for palabra in lista_sin_orden:
        if len(palabra[0]) >= MINIMO_CARACTERES_PALABRAS:
            lista_con5_caracteres.append(palabra)

    lista = sorted(lista_con5_caracteres, key= lambda x:x[0])

    return lista

def sacar_tildes(p):
    return p.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u') 
    

def cantidad_palabras_por_letra(letra, lista):
    '''
    Retorna la cantidad de palabras por letra recibida por parametro dentro de la lista de listas
    '''
    palabras_con_letra = []

    for palabra in lista:
        primera_letra = palabra[0][0]
        primera_letra_sin_tildes = sacar_tildes(primera_letra)
        if primera_letra_sin_tildes == letra:
            palabras_con_letra.append(palabra)

    cant_palabras_con_letra = len(palabras_con_letra)

    return cant_palabras_con_letra

def total_palabras_en_diccionario():
    '''
    Llamado a funcion cantidad_palabras(), suma la cantidad de palabras que hay en total dentro del diccionario
    '''
    total = 0
    lista_ordenada = ordenar_filtrar_diccionario()
    for letra in LETRAS:
            total += cantidad_palabras_por_letra(letra, lista_ordenada)
    
    return total

def total_palabras_por_letra():
    '''
    Muestra diccionario con cantidad de palabras por letra que hay en el diccionario filtrado.
    '''

    dicc = {}
    
    lista_ordenada = ordenar_filtrar_diccionario()

    for letra in LETRAS:
        dicc[letra] = cantidad_palabras_por_letra(letra, lista_ordenada)

    return dicc

def obtener_letras_participantes():
    '''
    Crear una lista de 10 letras aleatorias de la lista de letras permitidas para el rosco.
    '''
    return random.sample(LETRAS, 10)


def recibir_lista_diccionario_filtrado(diccionario_filtrado, letras_participantes):

    letras_castellano = "aábcdeéfghiíjklmnñoópqrstuúvwxyz"
    lista_palabras_participantes = []

    for letra in letras_participantes:
        palabras_candidatas = []

        for item in diccionario_filtrado:
            palabra = item[0]

            palabra_sin_tildes = sacar_tildes(palabra)

            if palabra_sin_tildes[0] == letra:
                definicion = item[1]
                # print(definicion)
                palabras_candidatas.append([palabra, definicion])

        palabra_para_esta_letra = random.choice(palabras_candidatas)
        # print(palabra_para_esta_letra)
        lista_palabras_participantes.append(palabra_para_esta_letra)

    # sorted(lista_palabras_participantes, key=lambda i: letras_castellano.index(i[0]))
    return sorted(lista_palabras_participantes, key=lambda i: letras_castellano.index(i[0][0]))


# FUNCION QUE ITERA 100 VECES PARA PRUEBAS
"""
FUNCION QUE ITERA 100 VECES PARA PRUEBAS
for i in range(100):
    lista_letras2 = obtener_letras_participantes()
    diccionario_filtrado = ordenar_filtrar_diccionario()
    print(recibir_lista_diccionario_filtrado(diccionario_filtrado,lista_letras2))

"""