import doctest
import os
from typing import Callable, List

import tipos
from calculos import *
from diccionario_palabras import *


def agregar_color(texto: str, color: tipos.color) -> str:
    '''
    Esta función recibe un texto y le agrega códigos de color del estandar ANSI para que se visualicen en la consola de color rojo o verde

    Parámetros
    ----------
    texto : str
    color : tipos.color

    Retorna
    -------  
    str
        Si se pasa un color válido como argumento, la función retornará el texto modificado de forma tal que se visualizará con ese color en la consola.
        Caso contrario, la función retornará el texto original sin modificarlo.

    Autores
    -------
    * Brizuela, Natanael Daniel
    * Lewin, Iván
    '''
    ROJO = '\x1b[0;31m'
    VERDE = '\x1b[0;32m'
    RESET = '\033[0;m'

    texto_con_color = texto
    if color == 'verde':
        texto_con_color = VERDE + texto + RESET
    elif color == 'rojo':
        texto_con_color = ROJO + texto + RESET
    return texto_con_color


def limpiar_interfaz() -> None:
    '''
    Esta función limpia la consola del usuario.

    Autores
    -------
    * Brizuela, Natanael Daniel
    * Lewin, Iván
    '''
    os.system('cls' if os.name == 'nt' else 'clear')


def mostrar_tableros(letras: List[str], jugadas: List[tipos.jugada]) -> None:
    '''
    Esta función muestra los tableros de letras participantes del juego y jugadas realizadas.

    Parámetros
    ----------
    letras : List[str]
        Una lista de las letras que participan en este juego.
    jugadas : List[tipos.jugada]
        Las jugadas de la partida.

    Autores
    -------
    * Brizuela, Natanael Daniel
    * Lewin, Iván

    Ejemplos
    --------
    # >>> mostrar_tableros(['A', 'B', 'C', 'D', 'E'], [])
    # [A][B][C][D][E]
    # [ ][ ][ ][ ][ ]
    # >>> mostrar_tableros(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'], [])
    # [A][B][C][D][E][F][G][H][I][J]
    # [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
    # >>> mostrar_tableros(['A', 'B', 'C', 'D', 'E'], ['a', 'a', 'e'])
    # [A][B][C][D][E]
    # [\x1b[0;32ma\033[0;m][\x1b[0;32ma\033[0;m][\x1b[0;31me\033[0;m][ ][ ]
    # >>> mostrar_tableros(['A', 'B', 'C', 'D', 'E'], ['a', 'a', 'e', 'a', 'e'])
    # [A][B][C][D][E]
    # [\x1b[0;32ma\033[0;m][\x1b[0;32ma\033[0;m][\x1b[0;31me\033[0;m][\x1b[0;32ma\033[0;m][\x1b[0;31me\033[0;m]
    # >>> mostrar_tableros(['A', 'B', 'C', 'D', 'E'], ['a', 'a', 'e', 'a', 'e', 'a', 'a'])
    # [A][B][C][D][E]
    # [\x1b[0;32ma\033[0;m][\x1b[0;32ma\033[0;m][\x1b[0;31me\033[0;m][\x1b[0;32ma\033[0;m][\x1b[0;31me\033[0;m]
    '''

    tablero_letras = ''
    for letra in letras:
        celda = f'[{letra}]'
        tablero_letras += celda

    tablero_turnos_de_juego = ''
    tablero_resultados = ''
    for i in range(len(letras)):
        celda_turnos = '[ ]'
        celda_resultados = '[ ]'
        if i < len(jugadas):
            celda_turnos = f'[{jugadas[i]["jugador"]["turno_de_juego"] + 1}]'
            if jugadas[i]['resultado'] == 'a':
                celda_resultados = f'[{agregar_color(jugadas[i]["resultado"], "verde")}]'
            else:
                celda_resultados = f'[{agregar_color(jugadas[i]["resultado"], "rojo")}]'
        tablero_turnos_de_juego += celda_turnos
        tablero_resultados += celda_resultados

    print(tablero_letras)
    print(tablero_turnos_de_juego)
    print(tablero_resultados)


def mostrar_turno_actual(turno_actual: List[str], jugadas: List[tipos.jugada], jugadores: List[tipos.jugador], jugador_actual: tipos.jugador) -> None:
    '''
    Esta función muestra en pantalla las indicaciones para que el usuario haga un intento.

    Parámetros
    ----------
    turno_actual : List[str]
        Una lista con dos strings; el primero es la palabra a adivinar, y el segundo es la definición de esa palabra.
    jugadas : List[tipos.jugada]
        Las jugadas de la partida.
    jugadores : List[tipos.jugador]
        Los jugadores que participaron de la partida.
    jugador_actual : tipos.jugador
        El jugador que está jugando actualmente.

    Autores
    -------
    * Brizuela, Natanael Daniel
    * Lewin, Iván
    '''
    estadisticas_jugadores = calcular_estadisticas(jugadas, jugadores)
    padding = max(map(lambda j: len(j['usuario']), jugadores))

    print('Jugadores:')
    for i in range(len(estadisticas_jugadores)):
        usuario = estadisticas_jugadores[i]['jugador']['usuario']
        aciertos = estadisticas_jugadores[i]['aciertos']
        errores = estadisticas_jugadores[i]['errores']
        indicador_actual = '* ' if usuario == jugador_actual['usuario'] else '  '
        print(f'{indicador_actual}{i + 1}. {usuario:<{padding}} - Aciertos: {agregar_color(str(aciertos), "verde")} - Errores: {agregar_color(str(errores), "rojo")}')
    print()

    palabra_actual, definicion_actual = turno_actual
    letra_actual = palabra_actual[0]

    print(f'Es el turno de {jugador_actual["usuario"]}')
    print()
    print(
        f'Turno letra {letra_actual.upper()} - Palabra de {len(palabra_actual)} letras')
    print(f'Definición: {definicion_actual}\n')


def mostrar_feedback(jugadas: List[tipos.jugada], turno_previo: List[str]) -> None:
    '''
    Si el intento del usuario en el turno anterior fue un error, esta función muestra la palabra correcta en pantalla.

    Parámetros
    ----------
    jugadas : List[tipos.jugada]
        Las jugadas de la partida.
    turno_previo : List[str]
        Una lista con dos strings; el primero es la palabra a adivinar, y el segundo es la definición de esa palabra.

    Autores
    -------
    * Brizuela, Natanael Daniel
    * Lewin, Iván

    Ejemplos
    --------
    >>> mostrar_feedback([{'resultado': 'a'}, {'resultado': 'a'}, {'resultado': 'e'}, {'resultado': 'e'}, {'resultado': 'a'}], ['entorpecer', '1.  tr. Poner torpe U. t. c. prnl.'])
    \x1b[0;32m¡Correcto!\033[0;m
    >>> mostrar_feedback([{'resultado': 'a'}, {'resultado': 'a'}, {'resultado': 'e'}, {'resultado': 'e'}, {'resultado': 'e'}], ['entorpecer', '1.  tr. Poner torpe U. t. c. prnl.'])
    \x1b[0;31m¡Incorrecto!\033[0;m La palabra correcta era "entorpecer"
    '''

    ultima_jugada = jugadas[-1] if len(jugadas) > 0 else None
    palabra_correcta = turno_previo[0]
    if palabra_correcta:
        if ultima_jugada['resultado'] == 'a':
            print(agregar_color('¡Correcto!', 'verde'))
        else:
            print(
                f"{agregar_color('¡Incorrecto!', 'rojo')} La palabra correcta era '{palabra_correcta}'")


def mostrar_interfaz_del_juego(letras: List[str], jugadas: List[tipos.jugada], jugadores: List[tipos.jugador], jugador_actual: tipos.jugador, turno_actual: List[str], turno_previo: List[str] = None) -> None:
    '''
    Esta función es la encargada de generar la interfaz del juego, que incluye el tablero de letras participantes, el tablero de jugadas realizadas, la 
    última palabra correcta (en caso de que el usuario haya tenido un error) y las indicaciones para el turno actual.

    Parámetros
    ----------
    letras : List[str]
        Una lista de las letras que participan en este juego.
    jugadas : List[tipos.jugada]
        Las jugadas de la partida.
    jugadores : List[tipos.jugador]
        Los jugadores que participaron de la partida.
    jugador_actual : tipos.jugador
        El jugador que está jugando actualmente.
    turno_actual : List[str]
        Una lista con dos strings; el primero es la palabra a adivinar, y el segundo es la definición de esa palabra.
    turno_previo : List[str], default: None
        Una lista con dos strings; el primero es la palabra a adivinar, y el segundo es la definición de esa palabra.

    Autores
    -------
    * Brizuela, Natanael Daniel
    * Lewin, Iván
    '''
    limpiar_interfaz()
    mostrar_tableros(letras, jugadas)
    if turno_previo is not None:
        print()
        mostrar_feedback(jugadas, turno_previo)
    print()
    mostrar_turno_actual(turno_actual, jugadas, jugadores, jugador_actual)


def recibir_ingreso_usuario(palabra_actual: str, generar_interfaz: Callable) -> str:
    '''
    Esta función recibe el ingreso de datos del usuario y realiza validaciones para asegurarse de que es correcto.

    Parámetros
    ----------
    palabra_actual : str
        La palabra a adivinar en el turno actual.
    generar_interfaz : Callable
        Función que permite generar la interfaz de usuario.

    Retorna
    -------
    str
        Un string de la longitud de la palabra a adivinar en el turno actual formado por caracteres alfabéticos.

    Autores
    -------
    * Brizuela, Natanael Daniel
    * Lewin, Iván
    '''

    palabra_valida = None
    ingreso_del_usuario = aplanar(input('Ingrese una palabra: '))

    while palabra_valida is None:
        if len(ingreso_del_usuario) != len(palabra_actual):
            generar_interfaz()
            print(f'{agregar_color("¡Error!", "rojo")} Su ingreso debe ser una palabra de {len(palabra_actual)} letras. ', end='')
            ingreso_del_usuario = aplanar(input('Ingrese una palabra: '))
        elif not ingreso_del_usuario.isalpha():
            generar_interfaz()
            print(
                f'{agregar_color("¡Error!", "rojo")} Su ingreso solo debe contener letras. ', end='')
            ingreso_del_usuario = aplanar(input('Ingrese una palabra: '))
        elif palabra_actual[0] != ingreso_del_usuario[0]:
            generar_interfaz()
            print(
                f'{agregar_color("¡Error!", "rojo")} Su ingreso debe comenzar con la letra "{palabra_actual[0].upper()}". ', end='')
            ingreso_del_usuario = aplanar(input('Ingrese una palabra: '))
        else:
            palabra_valida = ingreso_del_usuario

    return ingreso_del_usuario


def mostrar_resumen_de_la_partida(letras: List[str], jugadas: List[tipos.jugada]) -> None:
    '''
    Esta función muestra el resumen luego de finalizar el juego.

    Parámetros
    ----------
    letras : List[str]
        Una lista de las letras que participan en este juego.
    jugadas : List[tipos.jugada]
        Las jugadas de la partida.

    Autores
    -------
    * Brizuela, Natanael Daniel
    * Lewin, Iván
    '''
    limpiar_interfaz()
    mostrar_tableros(letras, jugadas)

    print()
    for i in range(len(jugadas)):
        jugada = jugadas[i]
        intento = jugada['intento']
        jugador = jugada['jugador']
        resultado = jugada['resultado']
        palabra = jugada['palabra']
        letra = palabra[0].upper()
        texto = f'Turno letra {letra} - jugador {jugador["turno_de_juego"] + 1} {jugador["usuario"]} - Palabra de {len(palabra)} letras - {intento} - '
        if resultado == 'a':
            texto += (agregar_color('acierto', 'verde'))
        else:
            texto += (f'{agregar_color("error", "rojo")} - Palabra correcta: {palabra}')
        print(texto)
    print()


def mostrar_total_de_palabras(cantidad_de_palabras_por_letra: dict[str, int], cantidad_de_letras_deseada: int):
    '''
    Esta función muestra el total de palabras del diccionario, primero letra por letra, y luego el total de todo el diccionario.

    Parámetros
    ----------
    cantidad_de_palabras_por_letra : dict[str, int]
        Un diccionario con la cantidad de palabras que comienzan por cada letra.
    cantidad_de_letras_deseada : int
        El número de letras que se desea que participen del juego.

    Autores
    -------
    * Brizuela, Natanael Daniel
    * Lewin, Iván
    '''
    letras = cantidad_de_palabras_por_letra.keys()
    letras = ordenar_en_español(list(letras))
    cantidad_total_de_palabras = sum(cantidad_de_palabras_por_letra.values())

    for letra in letras:
        cantidad = cantidad_de_palabras_por_letra[letra] if letra in cantidad_de_palabras_por_letra.keys(
        ) else None
        if cantidad is None or cantidad == 0:
            print(
                f"No hay palabras que comienzan con la letra {agregar_color(letra.upper(),'rojo')}.")
        elif cantidad == 1:
            print(
                f"Hay {cantidad:<2} palabra que comienza con la letra {agregar_color(letra.upper(),'verde')}.")
        else:
            print(
                f"Hay {cantidad:<2} palabras que comienzan con la letra {agregar_color(letra.upper(),'verde')}.")
    print()
    print(
        f"En total hay {cantidad_total_de_palabras} palabras disponibles para el rosco.")
    print()

    cantidad_de_letras = len(letras)
    if (cantidad_de_letras < cantidad_de_letras_deseada):
        print(
            f'Se deseaba jugar con {cantidad_de_letras_deseada} letras. Sin embargo, debido a las preferencias del juego sólo se pudieron obtener {cantidad_de_letras} letras.')
        print()

    input('Presione Enter (Inicio) para iniciar el juego ')

    return cantidad_de_palabras_por_letra


def mostrar_puntajes_parciales(puntajes_de_la_partida: List[tipos.puntaje], puntajes_acumulados: List[tipos.puntaje], jugadas_restantes_disponibles: int) -> None:
    '''
    Esta función muestra el puntaje de la partida en curso y el puntaje acumulado del juego.

    Parámetros
    ----------
    puntajes_de_la_partida : List[tipos.puntaje]
        El puntaje de la partida en curso.
    puntajes_acumulados : List[tipos.puntaje]
        El puntaje acumulado a lo largo de todas las partidas del juego.
    jugadas_restantes_disponibles : int

    Autores
    -------
    * Lewin, Iván
    '''
    print(f'Puntaje de la partida:')
    for i in range(len(puntajes_de_la_partida)):
        usuario = puntajes_de_la_partida[i]['usuario']
        puntaje = puntajes_de_la_partida[i]['puntaje']
        print(f'{i + 1}. {usuario} - {puntaje} puntos')
    print()
    if (jugadas_restantes_disponibles > 1):
        print(f'Puntaje parcial:')
        for i in range(len(puntajes_acumulados)):
            usuario = puntajes_acumulados[i]['usuario']
            puntaje = puntajes_acumulados[i]['puntaje']
            print(f'{i + 1}. {usuario} - {puntaje} puntos')


def mostrar_resumen_juego(partidas_jugadas: int, puntajes_finales: List[tipos.puntaje]) -> None:
    '''
    Esta función muestra el puntaje final del juego.

    Parámetros
    ----------
    partidas_jugadas : int
        La cantidad de partidas jugadas en el juego.
    puntajes_finales : List[tipos.puntaje]
        Los puntajes acumulados del juego.

    Autores
    -------
    * Lewin, Iván
    '''
    limpiar_interfaz()
    print('Reporte final:')
    print(f'Partidas jugadas: {partidas_jugadas}')
    print()
    print('Reporte final:')
    for i in range(len(puntajes_finales)):
        usuario = puntajes_finales[i]['usuario']
        puntaje = puntajes_finales[i]['puntaje']
        print(f'{i + 1}. {usuario} - {puntaje} puntos')


def preguntar_seguir_jugando(jugadas_restantes_disponibles: int) -> bool:
    '''
    Esta función se encarga de preguntarle al usuario si desea continuar jugando.

    Parámetros
    ----------
    jugadas_restantes_disponibles : int

    Retorna
    -------
    bool
        `True` si el usuario respondió afirmativamente y `False` en caso contrario.

    Autores
    -------
    * Brizuela, Natanael Daniel
    * Lewin, Iván
    '''
    if jugadas_restantes_disponibles == 1:
        print(f'Si lo desea, puede jugar una última partida más.', end=' ')
    else:
        print(
            f'Si lo desea, puede continuar jugando hasta {jugadas_restantes_disponibles} partidas más.', end=' ')
    ingreso_del_usuario = aplanar(input('¿Desea seguir jugando?: '))
    while ingreso_del_usuario not in ('si', 'no'):
        print(f'Por favor, ingrese "si" o "no". ', end='')
        ingreso_del_usuario = aplanar(input('¿Desea seguir jugando?: '))
    return ingreso_del_usuario == 'si'


def mostrar_configuracion(diccionario_configuracion: dict) -> None:
    """
    Esta funcion se encarga de mostrar la configuracion inicial del juego.

    Parámetros
    ----------
    diccionario_configuracion : dict

    Retorna
    -------
    None 

    Autores
    -------
    * Brizuela, Natanael Daniel
    --------
    """
    print("\n|---------> CONFIGURACION INICIAL <---------| ")
    for k, v in diccionario_configuracion.items():
        print(
            f"{(k)} : {v['valor']} -- {v['origen']}")
    print("|---------> CONFIGURACION INICIAL <---------| ")
    stop_momentaneo = input("\nPresione Enter (Inicio) para continuar. \n\n")


if __name__ == '__main__':
    print(doctest.testmod())
