from typing import List
from interfaz import *
from manejo_archivos import *

LONGITUD_PALABRA_MINIMA = 10
CANTIDAD_LETRAS_ROSCO = 10
LETRAS_SIN_TILDES = 'abcdefghijklmnñopqrstuvwxyz'
LETRAS_CON_TILDES = 'aáäbcdeéëfghiíïjklmnñoóöpqrstuúüvwxyz'


def ejecutar_partida(diccionario_como_lista: List[List[str]], cantidad_de_palabras_por_letra: dict[str]):
    """
    Esta función es la principal orquestadora de cada partida.

    Parámetros
    ----------
    diccionario_como_lista : List[List[str]]
        El diccionario con las palabras disponibles para el juego.
        Es una lista de listas de strings. Cada sublista tiene dos elementos; el primero es la palabra "aplanada" y el segundo, su definición.

    Autores
    -------
    * Armari, Valentino
    * Brizuela, Natanael Daniel
    """
    cantidad_letras_inciales = [x[0][0] for x in diccionario_como_lista]

    minimo_letras_posible = len(set(cantidad_letras_inciales))
    letras_participantes = generar_letras_participantes(
        LETRAS_SIN_TILDES, CANTIDAD_LETRAS_ROSCO, minimo_letras_posible, cantidad_de_palabras_por_letra)

    rosco = generar_rosco(diccionario_como_lista, letras_participantes)

    letras_mayuscula = [letra[0][0].upper() for letra in rosco]

    jugadas = []
    intentos = []

    for i in range(len(rosco)):
        turno_actual = rosco[i]
        turno_previo = rosco[i-1] if i > 0 else None
        palabra_actual: str = turno_actual[0]

        mostrar_interfaz_del_juego(
            letras_mayuscula, jugadas, turno_actual, turno_previo)
        ingreso_usuario = recibir_ingreso_usuario(
            palabra_actual, lambda: mostrar_interfaz_del_juego(letras_mayuscula, jugadas, turno_actual))
        intentos.append(ingreso_usuario)

        acierto = verificar_intento(ingreso_usuario, palabra_actual)
        jugadas.append(acierto)

    mostrar_resumen_de_la_partida(letras_mayuscula, jugadas, rosco, intentos)
    return calcular_puntaje_de_la_partida(jugadas)


def ejecutar_juego():
    """
    Esta función es la principal orquestadora del juego.
    Se encarga de obtener el diccionario de palabras admitidas para el juego, llevar el conteo del puntaje y permitir al usuario jugar tantas partidas como desee.

    Autores
    -------
    * Armari, Valentino
    * Brizuela, Natanael Daniel
    """
    diccionario_crudo = crear_diccionario()
    diccionario_filtrado = filtrar_diccionario(
        diccionario_crudo, LONGITUD_PALABRA_MINIMA)
    crear_csv(diccionario_filtrado)
    diccionario_como_lista = hacerlo_lista(diccionario_filtrado)

    cantidad_de_palabras_por_letra = calcular_cantidad_de_palabras_por_letra(
        diccionario_como_lista)
    cantidad_de_letras = len(cantidad_de_palabras_por_letra.keys())
    if (cantidad_de_letras < CANTIDAD_LETRAS_ROSCO):
        print("no hay tantas letras")
    mostrar_total_de_palabras(cantidad_de_palabras_por_letra)

    puntaje_total = 0
    continuar_jugando = True
    while continuar_jugando:
        puntaje_de_la_partida = ejecutar_partida(
            diccionario_como_lista, cantidad_de_palabras_por_letra)

        puntaje_total += puntaje_de_la_partida
        print()
        continuar_jugando = preguntar_seguir_jugando()

    print(f"Puntaje del juego: {puntaje_total} puntos")


# def testear_cien_veces():
#     """
#     Esta función ejecuta 100 veces las funciones que utilizamos para obtener el rosco y la lista aleatoria de letras participantes del juego.

#     Autores
#     * Galvani, Juan Ignacio
#     * Neme, Agustin Nadim
#     """
#     for i in range(100):
#         letras_participantes = generar_letras_participantes(LETRAS_SIN_TILDES, CANTIDAD_LETRAS_ROSCO)
#         diccionario_de_palabras = generar_diccionario(LONGITUD_PALABRA_MINIMA)
#         print(generar_rosco(diccionario_de_palabras, letras_participantes))


if __name__ == '__main__':
    ejecutar_juego()
    # testear_cien_veces()
