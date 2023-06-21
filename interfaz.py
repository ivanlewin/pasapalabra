import os
import doctest
from typing import Callable, List, Literal
from diccionario_palabras import *


def agregar_color(texto: str, color: Literal['rojo', 'verde']):
    """
    Esta función recibe un texto y le agrega códigos de color del estandar ANSI para que se visualicen en la consola de color rojo o verde

    Parámetros
    ----------
    texto : str
    color : Literal['rojo', 'verde']

    Retorna
    -------  
    str
        Si se pasa un color válido como argumento, la función retornará el texto modificado de forma tal que se visualizará con ese color en la consola.
        Caso contrario, la función retornará el texto original sin modificarlo.

    Autores
    -------
    * Brizuela, Natanael Daniel
    * Lewin, Iván
    """
    ROJO = "\x1b[0;31m"
    VERDE = "\x1b[0;32m"
    RESET = "\033[0;m"

    texto_con_color = texto
    if color == "verde":
        texto_con_color = VERDE + texto + RESET
    elif color == "rojo":
        texto_con_color = ROJO + texto + RESET
    return texto_con_color


def limpiar_interfaz():
    """
    Esta función limpia la consola del usuario.

    Autores
    -------
    * Brizuela, Natanael Daniel
    * Lewin, Iván
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def mostrar_tableros(letras: List[str], jugadas: List[Literal['a', 'e']]):
    """
    Esta función muestra los tableros de letras participantes del juego y jugadas realizadas.

    Parámetros
    ----------
    letras : List[str]
        Una lista de las letras que participan en este juego.
    jugadas : List[Literal['a', 'e']]
        El resultado de las jugadas realizadas.
        Debe ser una lista donde cada elemento es o bien 'a', para indicar un acierto, o bien 'e' para indicar un error.

    Autores
    -------
    * Brizuela, Natanael Daniel
    * Lewin, Iván

    Ejemplos
    --------
    >>> mostrar_tableros(['A', 'B', 'C', 'D', 'E'], [])
    [A][B][C][D][E]
    [ ][ ][ ][ ][ ]
    >>> mostrar_tableros(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'], [])
    [A][B][C][D][E][F][G][H][I][J]
    [ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
    >>> mostrar_tableros(['A', 'B', 'C', 'D', 'E'], ['a', 'a', 'e'])
    [A][B][C][D][E]
    [\x1b[0;32ma\033[0;m][\x1b[0;32ma\033[0;m][\x1b[0;31me\033[0;m][ ][ ]
    >>> mostrar_tableros(['A', 'B', 'C', 'D', 'E'], ['a', 'a', 'e', 'a', 'e'])
    [A][B][C][D][E]
    [\x1b[0;32ma\033[0;m][\x1b[0;32ma\033[0;m][\x1b[0;31me\033[0;m][\x1b[0;32ma\033[0;m][\x1b[0;31me\033[0;m]
    >>> mostrar_tableros(['A', 'B', 'C', 'D', 'E'], ['a', 'a', 'e', 'a', 'e', 'a', 'a'])
    [A][B][C][D][E]
    [\x1b[0;32ma\033[0;m][\x1b[0;32ma\033[0;m][\x1b[0;31me\033[0;m][\x1b[0;32ma\033[0;m][\x1b[0;31me\033[0;m]
    """

    tablero_letras = ''
    for letra in letras:
        celda = f'[{letra}]'
        tablero_letras += celda

    tablero_jugadas = ''
    for i in range(len(letras)):
        celda = "[ ]"
        if i < len(jugadas):
            if jugadas[i] == "a":
                celda = f"[{agregar_color(jugadas[i], 'verde')}]"
            else:
                celda = f"[{agregar_color(jugadas[i], 'rojo')}]"
        tablero_jugadas += celda

    print(tablero_letras)
    print(tablero_jugadas)


def mostrar_turno_actual(jugadas: List[Literal['a', 'e']], turno_actual: List[str]):
    """
    Esta función muestra en pantalla las indicaciones para que el usuario haga un intento.

    Parámetros
    ----------
    jugadas : List[Literal['a', 'e']]
        El resultado de las jugadas realizadas.
        Debe ser una lista donde cada elemento es o bien 'a', para indicar un acierto, o bien 'e' para indicar un error.
    turno_actual : List[str]
        Una lista con dos strings; el primero es la palabra a adivinar, y el segundo es la definición de esa palabra.

    Autores
    -------
    * Brizuela, Natanael Daniel
    * Lewin, Iván
    """
    aciertos = jugadas.count('a')
    errores = jugadas.count('e')

    palabra_actual, definicion_actual = turno_actual
    letra_actual = palabra_actual[0]

    print(f"Aciertos: {agregar_color(str(aciertos), 'verde')}")
    print(f"Errores: {agregar_color(str(errores), 'rojo')}")
    print(
        f"Turno letra {letra_actual.upper()} - Palabra de {len(palabra_actual)} letras")
    print(f"Definición: {definicion_actual}\n")


def mostrar_feedback(jugadas: List[Literal['a', 'e']], turno_previo: List[str]):
    """
    Si el intento del usuario en el turno anterior fue un error, esta función muestra la palabra correcta en pantalla.

    Parámetros
    ----------
    jugadas : List[Literal['a', 'e']]
        El resultado de las jugadas realizadas.
        Debe ser una lista donde cada elemento es o bien 'a', para indicar un acierto, o bien 'e' para indicar un error.
    turno_previo : List[str]
        Una lista con dos strings; el primero es la palabra a adivinar, y el segundo es la definición de esa palabra.

    Autores
    -------
    * Brizuela, Natanael Daniel
    * Lewin, Iván

    Ejemplos
    --------
    >>> mostrar_feedback(['a', 'a' 'e', 'e', 'a'], ["entorpecer", "1.  tr. Poner torpe U. t. c. prnl."])
    \x1b[0;32m¡Correcto!\033[0;m
    >>> mostrar_feedback(['a', 'a' 'e', 'e', 'e'], ["entorpecer", "1.  tr. Poner torpe U. t. c. prnl."])
    \x1b[0;31m¡Incorrecto!\033[0;m La palabra correcta era 'entorpecer'
    """

    ultima_jugada = jugadas[-1] if len(jugadas) > 0 else None
    palabra_correcta = turno_previo[0]
    if palabra_correcta:
        if ultima_jugada == "a":
            print(agregar_color('¡Correcto!', 'verde'))
        else:
            print(
                f"{agregar_color('¡Incorrecto!', 'rojo')} La palabra correcta era '{palabra_correcta}'")


def mostrar_interfaz_del_juego(letras: List[str], jugadas: List[Literal['a', 'e']], turno_actual: List[str], turno_previo: List[str] = None):
    """
    Esta función es la encargada de generar la interfaz del juego, que incluye el tablero de letras participantes, el tablero de jugadas realizadas, la 
    última palabra correcta (en caso de que el usuario haya tenido un error) y las indicaciones para el turno actual.

    Parámetros
    ----------
    letras : List[str]
        Una lista de las letras que participan en este juego.
    jugadas : list['a', 'e']
        El resultado de las jugadas realizadas.
        Debe ser una lista donde cada elemento es o bien 'a', para indicar un acierto, o bien 'e' para indicar un error.
    turno_actual : List[str]
        Una lista con dos strings; el primero es la palabra a adivinar, y el segundo es la definición de esa palabra.
    turno_previo : List[str], default: None
        Una lista con dos strings; el primero es la palabra a adivinar, y el segundo es la definición de esa palabra.

    Autores
    -------
    * Brizuela, Natanael Daniel
    * Lewin, Iván
    """
    limpiar_interfaz()
    mostrar_tableros(letras, jugadas)
    if turno_previo is not None:
        print()
        mostrar_feedback(jugadas, turno_previo)
    print()
    mostrar_turno_actual(jugadas, turno_actual)


def recibir_ingreso_usuario(palabra_actual: str, generar_interfaz: Callable):
    """
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
    """

    palabra_valida = None
    ingreso_del_usuario = aplanar(input("Ingrese una palabra: "))

    while palabra_valida is None:
        if len(ingreso_del_usuario) != len(palabra_actual):
            generar_interfaz()
            print(f"{agregar_color('¡Error!', 'rojo')} Su ingreso debe ser una palabra de {len(palabra_actual)} letras. ", end="")
            ingreso_del_usuario = aplanar(input("Ingrese una palabra: "))
        elif not ingreso_del_usuario.isalpha():
            generar_interfaz()
            print(
                f"{agregar_color('¡Error!', 'rojo')} Su ingreso solo debe contener letras. ", end="")
            ingreso_del_usuario = aplanar(input("Ingrese una palabra: "))
        elif palabra_actual[0] != ingreso_del_usuario[0]:
            generar_interfaz()
            print(
                f"{agregar_color('¡Error!', 'rojo')} Su ingreso debe comenzar con la letra '{palabra_actual[0].upper()}'. ", end="")
            ingreso_del_usuario = aplanar(input("Ingrese una palabra: "))
        else:
            palabra_valida = ingreso_del_usuario

    return ingreso_del_usuario


def calcular_puntaje_de_la_partida(jugadas: List[Literal['a', 'e']]):
    """
    Esta función recibe una lista de jugadas (caracteres 'a' o 'e') y retorna el puntaje obtenido. Cada acierto suma 10 puntos y cada error resta 3 puntos.

    Parámetros
    ----------
    jugadas : List[Literal['a', 'e']]
        El resultado de las jugadas realizadas.
        Debe ser una lista donde cada elemento es o bien 'a', para indicar un acierto, o bien 'e' para indicar un error.

    Retorna
    -------
        `int`. Un entero que representa el puntaje de la partida.

    Autores
    -------
    * Armari, Valentino
    * Lewin, Iván

    Ejemplos
    --------
    >>> calcular_puntaje_de_la_partida([])
    0
    >>> calcular_puntaje_de_la_partida(['a', 'a', 'a'])
    30
    >>> calcular_puntaje_de_la_partida(['a', 'e', 'a', 'e', 'e', 'e', 'e'])
    5
    >>> calcular_puntaje_de_la_partida(['a', 'e', 'z'])
    7
    >>> calcular_puntaje_de_la_partida(['e', 'e', 'e'])
    -9
    """
    aciertos = jugadas.count('a')
    errores = jugadas.count('e')
    return (aciertos * 10) + (errores * -3)


def mostrar_resumen_de_la_partida(letras: List[str], jugadas: List[Literal['a', 'e']], turnos: List[List[str]], lista_palabras_ingresadas: List[str]):
    """
    Esta función muestra el resumen luego de finalizar el juego.

    Parámetros
    ----------
    letras : List[str]
        Una lista de las letras que participan en este juego.
    jugadas : List[Literal['a', 'e']]
        El resultado de las jugadas realizadas.
        Debe ser una lista donde cada elemento es o bien 'a', para indicar un acierto, o bien 'e' para indicar un error.
    turnos : List[List[str]]
        La lista de las palabras del juego: Cada elemento es una lista de strings donde el primer elemento es la palabra a adivinar, y el segundo es la definición de esa palabra.
    lista_palabras_ingresadas : List[str]
        Una lista con los ingresos del usuario (aciertos y errores).

    Autores
    -------
    * Brizuela, Natanael Daniel
    * Lewin, Iván
    """
    limpiar_interfaz()
    mostrar_tableros(letras, jugadas)
    puntaje_partida = calcular_puntaje_de_la_partida(jugadas)

    print()
    for i in range(len(letras)):
        letra = letras[i]
        jugada = jugadas[i]
        turno = turnos[i]
        palabra = turno[0]
        ingreso = lista_palabras_ingresadas[i]
        texto = f"Turno letra {letra.upper()} - Palabra de {len(palabra)} letras - {ingreso} - "
        if jugada == "a":
            texto += (agregar_color('acierto', 'verde'))
        else:
            texto += (f"{agregar_color('error', 'rojo')} - Palabra Correcta: {palabra}")
        print(texto)

    print()
    aciertos = jugadas.count('a')
    errores = jugadas.count('e')
    print(f"Aciertos: {agregar_color(str(aciertos), 'verde')}")
    print(f"Errores: {agregar_color(str(errores), 'rojo')}")
    print()
    print(f"Puntaje de la partida: {puntaje_partida} puntos")


def mostrar_total_de_palabras(cantidad_de_palabras_por_letra, cantidad_de_letras_deseada):
    """
    Esta función muestra el total de palabras del diccionario, primero letra por letra, y luego el total de todo el diccionario.

    Parámetros
    ----------
    <-- cambiar --> 
    diccionario_de_palabras : List[List[str]]
        El diccionario de palabras participantes del juego.
        Es una lista de listas de strings. Cada sublista tiene dos elementos; el primero es la palabra "aplanada" y el segundo, su definición.

    Autores
    -------
    * Brizuela, Natanael Daniel
    * Lewin, Iván
    """
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
                f"Hay {cantidad} palabra que comienza con la letra {agregar_color(letra.upper(),'verde')}.")
        else:
            print(
                f"Hay {cantidad} palabras que comienzan con la letra {agregar_color(letra.upper(),'verde')}.")
    print()
    print(
        f"En total hay {cantidad_total_de_palabras} palabras disponibles para el rosco.")
    print()

    cantidad_de_letras = len(letras)
    if (cantidad_de_letras < cantidad_de_letras_deseada):
        print(f"Se deseaba jugar con {cantidad_de_letras_deseada} letras. \
Sin embargo, debido a las preferencias del juego sólo se pudieron obtener {cantidad_de_letras} letras.")
        print()

    input("Presione Enter (Inicio) para iniciar el juego ")

    return cantidad_de_palabras_por_letra


def preguntar_seguir_jugando():
    """
    Esta función se encarga de preguntarle al usuario si desea continuar jugando.

    Retorna
    -------
    bool
        `True` si el usuario respondió afirmativamente y `False` en caso contrario.

    Autores
    -------
    * Brizuela, Natanael Daniel
    * Lewin, Iván
    """
    ingreso_del_usuario = aplanar(input("¿Desea seguir jugando?: "))
    while ingreso_del_usuario not in ('si', 'no'):
        print(f"Por favor, ingrese 'si' o 'no'. ", end="")
        ingreso_del_usuario = aplanar(input("¿Desea seguir jugando?: "))
    return ingreso_del_usuario == 'si'


def verificar_intento(ingreso_usuario: str, palabra_a_adivinar: str):
    """
    Esta función verifica que el ingreso del usuario sea válido dada la palabra a adivinar.

    Parámetros
    ----------
    ingreso_usuario : str
    palabra_a_adivinar : str

    Retorna
    -------
    str
        Retorna la letra 'a' si es un acierto o la letra 'e' en caso contrario.

    Autores
    -------
    * Brizuela, Natanael Daniel
    * Lewin, Iván
    * Neme, Agustin Nadim

    Ejemplos
    --------
    >>> verificar_intento("AlmuÉrzo", "almuerzo")
    'a'
    >>> verificar_intento("almurso", "almuerzo")
    'e'
    """
    acierto = ""
    if aplanar(ingreso_usuario) == palabra_a_adivinar:
        acierto = "a"
    else:
        acierto = "e"
    return acierto


def mostrar_configuracion(diccionario):

    print("\n|---------> CONFIGURACION INICIAL <---------| ")
    for k, v in diccionario.items():
        print(
            f"{(k)} : {agregar_color(str(v['valor']),'verde')} -- {agregar_color(str(v['origen']),'verde')}")


if __name__ == '__main__':
    print(doctest.testmod())
