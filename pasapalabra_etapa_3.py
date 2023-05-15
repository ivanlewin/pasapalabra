import random
from pasapalabra_etapa_2 import ordenar_filtrar_diccionario, LETRAS, sacar_tildes


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