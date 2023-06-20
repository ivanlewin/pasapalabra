from typing import List

import tipos
from calculos import *
from diccionario_palabras import *
from interfaz import *
from manejo_archivos import *
from interfaz_tkinter import ventana_main

LONGITUD_PALABRA_MINIMA = 5
CANTIDAD_LETRAS_ROSCO = 4
LETRAS_SIN_TILDES = 'abcdefghijklmnñopqrstuvwxyz'
MAXIMO_PARTIDAS = 5
PUNTAJE_ACIERTO = 10
PUNTAJE_DESACIERTO = 3


def ejecutar_partida(diccionario_como_lista: tipos.rosco, jugadores: List[tipos.jugador], cantidad_de_palabras_por_letra: dict[str, int]) -> List[tipos.puntaje]:
    '''
    Esta función es la principal orquestadora de cada partida.

    Parámetros
    ----------
    diccionario_como_lista : tipos.rosco
        El diccionario con las palabras disponibles para el juego.
        Lista de tuplas donde cada tupla tiene dos elementos; el primero es la palabra 'aplanada' y el segundo, su definición.
    usuarios : List[str]
        El listado de los usuarios que juegan al juego.
    usuarios : List[str]
        El listado de los usuarios que juegan al juego.

    Retorna
    -------
    tipos.Tipo_puntajes
        El puntaje obtenido en la partida.

    Autores
    -------
    * Armari, Valentino
    * Brizuela, Natanael Daniel
    * Lewin, Iván
    '''
    cantidad_letras_inciales = [x[0][0] for x in diccionario_como_lista]
    minimo_letras_posible = len(set(cantidad_letras_inciales))
    letras_participantes = generar_letras_participantes(LETRAS_SIN_TILDES, CANTIDAD_LETRAS_ROSCO, minimo_letras_posible, cantidad_de_palabras_por_letra)

    rosco = generar_rosco(diccionario_como_lista, letras_participantes)

    letras_mayuscula = [letra[0][0].upper() for letra in rosco]

    jugadas: List[tipos.jugada] = []
    intentos: List[str] = []
    turno_del_jugador_actual = 0

    for i in range(len(rosco)):
        turno_actual = rosco[i]
        turno_previo = rosco[i-1] if i > 0 else None
        palabra_actual: str = turno_actual[0]
        jugador_actual = jugadores[turno_del_jugador_actual]

        mostrar_interfaz_del_juego(letras_mayuscula, jugadas, jugadores, jugador_actual, turno_actual, turno_previo)
        ingreso_usuario = recibir_ingreso_usuario(palabra_actual, lambda: mostrar_interfaz_del_juego(letras_mayuscula, jugadas, jugadores, jugador_actual, turno_actual))
        intentos.append(ingreso_usuario)

        resultado = verificar_intento(ingreso_usuario, palabra_actual)
        jugadas.append({
            'intento': ingreso_usuario,
            'jugador': jugador_actual,
            'palabra': palabra_actual,
            'resultado': resultado,
        })

        if resultado == 'e':
            turno_del_jugador_actual = (turno_del_jugador_actual + 1) % len(jugadores)

    puntajes_de_la_partida = calcular_puntaje_de_la_partida(jugadas, jugadores, PUNTAJE_ACIERTO, PUNTAJE_DESACIERTO)
    mostrar_resumen_de_la_partida(letras_mayuscula, jugadas)
    return puntajes_de_la_partida


def ejecutar_juego() -> None:
    '''
    Esta función es la principal orquestadora del juego.
    Se encarga de obtener el diccionario de palabras admitidas para el juego, llevar el conteo del puntaje y permitir al usuario jugar tantas partidas como desee.

    Autores
    ------- 
    * Armari, Valentino
    * Brizuela, Natanael Daniel
    * Lewin, Iván
    '''
    usuarios = ventana_main()
    jugadores = asignar_turnos(usuarios)
    puntajes_del_juego: List[tipos.puntaje] = [{'usuario': jugador['usuario'], 'puntaje': 0} for jugador in jugadores]

    diccionario_crudo = crear_diccionario()
    diccionario_filtrado = filtrar_diccionario(diccionario_crudo, LONGITUD_PALABRA_MINIMA)
    crear_csv(diccionario_filtrado)
    diccionario_como_lista = hacerlo_lista(diccionario_filtrado)

    cantidad_de_palabras_por_letra = calcular_cantidad_de_palabras_por_letra(diccionario_como_lista)
    mostrar_total_de_palabras(cantidad_de_palabras_por_letra, CANTIDAD_LETRAS_ROSCO)

    continuar_jugando = True
    jugadas_restantes_disponibles = MAXIMO_PARTIDAS
    while continuar_jugando and jugadas_restantes_disponibles > 0:
        puntaje_de_la_partida = ejecutar_partida(diccionario_como_lista, jugadores, cantidad_de_palabras_por_letra)
        sumar_puntajes(puntaje_de_la_partida, puntajes_del_juego)
        mostrar_puntajes_parciales(puntaje_de_la_partida, puntajes_del_juego, jugadas_restantes_disponibles)
        jugadas_restantes_disponibles -= 1
        if jugadas_restantes_disponibles > 0:
            print()
            continuar_jugando = preguntar_seguir_jugando(jugadas_restantes_disponibles)
            if (continuar_jugando is False):
                print()

    mostrar_resumen_juego(MAXIMO_PARTIDAS - jugadas_restantes_disponibles, puntajes_del_juego)


# def testear_cien_veces():
#     '''
#     Esta función ejecuta 100 veces las funciones que utilizamos para obtener el rosco y la lista aleatoria de letras participantes del juego.

#     Autores
#     * Galvani, Juan Ignacio
#     * Neme, Agustin Nadim
#     '''
#     for i in range(100):
#         letras_participantes = generar_letras_participantes(LETRAS_SIN_TILDES, CANTIDAD_LETRAS_ROSCO)
#         diccionario_de_palabras = generar_diccionario(LONGITUD_PALABRA_MINIMA)
#         print(generar_rosco(diccionario_de_palabras, letras_participantes))


if __name__ == '__main__':
    ejecutar_juego()
