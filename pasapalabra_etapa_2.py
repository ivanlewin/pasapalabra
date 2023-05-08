from datos import obtener_lista_definiciones

MINIMO_CARACTERES_PALABRAS = 5
LETRAS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'á', 'é', 'í', 'ó', 'ú']

def ordenar_filtrar_diccionario():
    '''
    Se recibe un lista de listas desordenada con palabras y sus definiciones.
    Filtra de acuerdo a minimo de caracteres que debe tener la palabra y ordena alfabeticamente.
    Retorna lista ordenada y filtrada
    '''
    lista_sin_orden = obtener_lista_definiciones()
    lista_con5_caracteres = []

    for palabra in lista_sin_orden:
        if len(palabra[0]) >= MINIMO_CARACTERES_PALABRAS:
            lista_con5_caracteres.append(palabra)

    lista = sorted(lista_con5_caracteres, key= lambda x:x[0])

    return lista

def cantidad_palabras_por_letra(letra, lista):
    '''
    Retorna la cantidad de palabras por letra recibida por parametro dentro de la lista de listas
    '''
    palabras_con_letra = []

    for palabra in lista:
        if palabra[0][0] == letra:
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