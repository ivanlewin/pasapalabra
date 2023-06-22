from typing import List

import tipos
from calculos import *
from interfaz import *
from interfaz_tkinter import ventana_main
from manejo_archivos import *


def ejecutar_partida(diccionario_como_lista: tipos.diccionario_como_lista, jugadores: List[tipos.jugador], cantidad_de_palabras_por_letra: dict[str, int], configuracion: tipos.configuracion) -> List[tipos.puntaje]:
    '''
    Esta función es la principal orquestadora de cada partida.

    Parámetros
    ----------
    diccionario_como_lista : tipos.diccionario_como_lista
        El diccionario con las palabras disponibles para el juego.
        Lista de tuplas donde cada tupla tiene dos elementos; el primero es la palabra 'aplanada' y el segundo, su definición.
    jugadores : List[tipos.jugador]
        Los jugadores que participaron de la partida.
    cantidad_de_palabras_por_letra : dict[str, int]
    configuracion : tipos.configuracion

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
    letras_participantes = generar_letras_participantes(
        LETRAS_SIN_TILDES, configuracion['CANTIDAD_LETRAS_ROSCO']["valor"], minimo_letras_posible, cantidad_de_palabras_por_letra)

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

        mostrar_interfaz_del_juego(
            letras_mayuscula, jugadas, jugadores, jugador_actual, turno_actual, turno_previo)
        ingreso_usuario = recibir_ingreso_usuario(palabra_actual, lambda: mostrar_interfaz_del_juego(
            letras_mayuscula, jugadas, jugadores, jugador_actual, turno_actual))
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

    puntajes_de_la_partida = calcular_puntaje_de_la_partida(jugadas, jugadores, configuracion['PUNTAJE_ACIERTO']["valor"], configuracion['PUNTAJE_DESACIERTO']["valor"])
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
    configuracion = crear_diccionario_configuracion()

    usuarios = ventana_main()
    jugadores = [{'usuario': usuario, 'turno_de_juego': i} for i, usuario in enumerate(usuarios)]
    puntajes_del_juego: List[tipos.puntaje] = [{'usuario': jugador['usuario'], 'puntaje': 0} for jugador in jugadores]

    mostrar_configuracion(configuracion)
    mostrar_jugadores(jugadores)

    diccionario_crudo = crear_diccionario()
    diccionario_filtrado = filtrar_diccionario(diccionario_crudo, configuracion['LONGITUD_PALABRA_MINIMA']["valor"])
    crear_csv(diccionario_filtrado)
    diccionario_como_lista = hacerlo_lista(diccionario_filtrado)

    cantidad_de_palabras_por_letra = calcular_cantidad_de_palabras_por_letra(diccionario_como_lista)
    mostrar_total_de_palabras(cantidad_de_palabras_por_letra, configuracion['CANTIDAD_LETRAS_ROSCO']["valor"])

    continuar_jugando = True
    jugadas_restantes_disponibles = configuracion['MAXIMO_PARTIDAS']["valor"]
    while continuar_jugando and jugadas_restantes_disponibles > 0:
        puntaje_de_la_partida = ejecutar_partida(diccionario_como_lista, jugadores, cantidad_de_palabras_por_letra, configuracion)
        sumar_puntajes(puntaje_de_la_partida, puntajes_del_juego)
        mostrar_puntajes_parciales(puntaje_de_la_partida, puntajes_del_juego, jugadas_restantes_disponibles)
        jugadas_restantes_disponibles -= 1
        if jugadas_restantes_disponibles > 0:
            print()
            continuar_jugando = preguntar_seguir_jugando(jugadas_restantes_disponibles)
            if (continuar_jugando is False):
                print()

    mostrar_resumen_juego(configuracion['MAXIMO_PARTIDAS']["valor"] - jugadas_restantes_disponibles, puntajes_del_juego)


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
