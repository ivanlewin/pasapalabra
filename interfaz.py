import os
import doctest
from diccionario_palabras import *


def mostrar_texto_con_color(texto: str, color: str):
    """
    Esta función recibe un texto y le agrega códigos de color del estandar ANSI para que se visualicen en la consola de color verde o rojo

    Parámetros:
        * texto `str`: El texto al que se desea agregar el color.
        * color `str`: El color deseado. Los valores permitidos son "verde" o "rojo"

    Retorna:  
        `str`. Si se pasa un color válido como argumento, la función retornará el texto modificado de forma tal que se visualizará con ese color en la consola.
        Caso contrario, la función retornará el texto original sin modificarlo.

    Autores:
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

    Parámetros:
        No admite

    Retorna:
        `None`. Esta función únicamente manipula la consola para mostrar al usuario la interfaz del juego.

    Autores:
        * Brizuela, Natanael Daniel
        * Lewin, Iván
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def mostrar_tableros(letras: list[str], jugadas: list[str]):
    """
    Esta función muestra los tableros de letras participantes del juego y jugadas realizadas.

    Parámetros:
        * letras `list[str]`: Una lista de las letras que participan en este juego.
        * jugadas `list['a', 'e']`: El resultado de las jugadas ya realizadas por el usuario (debe ser una lista donde cada elemento es o bien 'a', para indicar un acierto, o bien 'e' para indicar un error).

    Retorna:  
        `None`. Esta función únicamente manipula la consola para mostrar al usuario la interfaz del juego.

    Autores:
        * Brizuela, Natanael Daniel
        * Lewin, Iván

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
                celda = f"[{mostrar_texto_con_color(jugadas[i], 'verde')}]"
            else:
                celda = f"[{mostrar_texto_con_color(jugadas[i], 'rojo')}]"
        tablero_jugadas += celda

    print(tablero_letras)
    print(tablero_jugadas)


def mostrar_turno_actual(jugadas: list[str], turno_actual: list[str]):
    """
    Esta función muestra en pantalla las indicaciones para que el usuario haga un intento.

    Parámetros:
        * jugadas `list['a', 'e']`: El resultado de las jugadas ya realizadas por el usuario (debe ser una lista donde cada elemento es o bien 'a', para indicar un acierto, o bien 'e' para indicar un error).
        * turno_actual `list[str, str]`: Una lista con dos strings; el primero es la palabra a adivinar, y el segundo es la definición de esa palabra.

    Retorna:
        `None`. Esta función únicamente manipula la consola para mostrar al usuario la interfaz del juego.

    Autores:
        * Brizuela, Natanael Daniel
        * Lewin, Iván
    """
    aciertos = jugadas.count('a')
    errores = jugadas.count('e')

    palabra_actual, definicion_actual = turno_actual
    letra_actual = palabra_actual[0]

    print(f"Aciertos: {mostrar_texto_con_color(str(aciertos), 'verde')}")
    print(f"Errores: {mostrar_texto_con_color(str(errores), 'rojo')}")
    print(f"Turno letra {letra_actual.upper()} - Palabra de {len(palabra_actual)} letras")
    print(f"Definición: {definicion_actual}\n")


def mostrar_feedback(jugadas: list[str], turno_previo: list[str]):
    """
    Si el intento del usuario en el turno anterior fue un error, esta función muestra la palabra correcta en pantalla.

    Parámetros:
        * jugadas `list['a', 'e']`: El resultado de las jugadas ya realizadas por el usuario (debe ser una lista donde cada elemento es o bien 'a', para indicar un acierto, o bien 'e' para indicar un error).
        * turno_previo `list[str, str]`: Una lista con dos strings; el primero es la palabra a adivinar, y el segundo es la definición de esa palabra.

    Retorna:
        `None`. Esta función únicamente manipula la consola para mostrar al usuario la interfaz del juego.

    Autores:
        * Brizuela, Natanael Daniel
        * Lewin, Iván

    >>> mostrar_feedback(['a', 'a' 'e', 'e', 'a'], ["entorpecer", "1.  tr. Poner torpe U. t. c. prnl."])
    \x1b[0;32m¡Correcto!\033[0;m
    >>> mostrar_feedback(['a', 'a' 'e', 'e', 'e'], ["entorpecer", "1.  tr. Poner torpe U. t. c. prnl."])
    \x1b[0;31m¡Incorrecto!\033[0;m La palabra correcta era 'entorpecer'
    """

    ultima_jugada = jugadas[-1] if len(jugadas) > 0 else None
    palabra_correcta = turno_previo[0]
    if palabra_correcta:
        if ultima_jugada == "a":
            print(mostrar_texto_con_color('¡Correcto!', 'verde'))
        else:
            print(f"{mostrar_texto_con_color('¡Incorrecto!', 'rojo')} La palabra correcta era '{palabra_correcta}'")


def mostrar_interfaz_del_juego(letras: list[str], jugadas: list[str], turno_actual: list[str], turno_previo: list[str] = None):
    """
    Esta función es la encargada de generar la interfaz del juego, que incluye el tablero de letras participantes, el tablero de jugadas realizadas, la 
    última palabra correcta (en caso de que el usuario haya tenido un error) y las indicaciones para el turno actual.

    Parámetros:
        * letras `list[str]`: Una lista de las letras que participan en este juego.
        * jugadas `list['a', 'e']`: El resultado de las jugadas ya realizadas por el usuario (debe ser una lista donde cada elemento es o bien 'a', para indicar un acierto, o bien 'e' para indicar un error).
        * turno_actual `list[str, str]`: Una lista con dos strings; el primero es la palabra a adivinar, y el segundo es la definición de esa palabra.
        * turno_previo `list[str, str]`: Una lista con dos strings; el primero es la palabra a adivinar, y el segundo es la definición de esa palabra.

    Retorna:
        `None`. Esta función únicamente manipula la consola para mostrar al usuario la interfaz del juego.

    Autores:
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


def recibir_ingreso_usuario(palabra_actual: str, generar_interfaz: any):
    """
    Esta función recibe el input del usuario y realiza las validaciones para asegurarse de que es correcto.

    Parámetros:
        * palabra_actual `str``: La palabra a adivinar en el turno actual.
        * generar_interfaz `function`: Función que permite generar la interfaz de usuario.

    Retorna:
        `str`. Retorna un string con caracteres alfabéticos de la longitud de la palabra a adivinar en el turno actual.

    Autores:
        * Brizuela, Natanael Daniel
        * Lewin, Iván
    """

    palabra_valida = None
    ingreso_del_usuario = aplanar_texto(input("Ingrese una palabra: "))

    while palabra_valida is None:
        if len(ingreso_del_usuario) != len(palabra_actual):
            generar_interfaz()
            print(f"{mostrar_texto_con_color('¡Error!', 'rojo')} Su ingreso debe ser una palabra de {len(palabra_actual)} letras. ", end="")
            ingreso_del_usuario = aplanar_texto(input("Ingrese una palabra: "))
        elif not ingreso_del_usuario.isalpha():
            generar_interfaz()
            print(f"{mostrar_texto_con_color('¡Error!', 'rojo')} Su ingreso solo debe contener letras. ", end="")
            ingreso_del_usuario = aplanar_texto(input("Ingrese una palabra: "))
        elif palabra_actual[0] != ingreso_del_usuario[0]:
            generar_interfaz()
            print(f"{mostrar_texto_con_color('¡Error!', 'rojo')} Su ingreso debe comenzar con la letra '{palabra_actual[0].upper()}'. ", end="")
            ingreso_del_usuario = aplanar_texto(input("Ingrese una palabra: "))
        else:
            palabra_valida = ingreso_del_usuario

    return ingreso_del_usuario


def calcular_puntaje_de_la_partida(jugadas):
    """
    Esta función recibe una lista de jugadas (caracteres 'a' o 'e') y retorna el puntaje obtenido. Cada acierto suma 10 puntos y cada error resta 3 puntos.

    Parámetros:
        * jugadas `list['a', 'e']`: El resultado de las jugadas ya realizadas por el usuario (debe ser una lista donde cada elemento es o bien 'a', para indicar un acierto, o bien 'e' para indicar un error).

    Retorna:
        `int`. Un entero que representa el puntaje de la partida.

    Autores:
        * Armari, Valentino
        * Lewin, Iván

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


def mostrar_resumen_de_la_partida(letras: list[str], jugadas: list[str], turnos: list[list[str]], lista_palabras_ingresadas: list[str]):
    """
    Esta función muestra el resumen luego de finalizar el juego.

    Parámetros:
        * letras `list[str]`: Una lista de las letras que participan en este juego.
        * jugadas `list['a', 'e']`: El resultado de las jugadas ya realizadas por el usuario (debe ser una lista donde cada elemento es o bien 'a', para indicar un acierto, o bien 'e' para indicar un error).
        * turnos `list[list[str, str]]`: La lista de las palabras del juego: Cada elemento es una lista de strings donde el primer elemento es la palabra a adivinar, y el segundo es la definición de esa palabra.
        * lista_palabras_ingresadas `list[str]`: Una lista con los ingresos del usuario (aciertos y errores).

    Retorna:
        `None`. Esta función únicamente manipula la consola para mostrar al usuario la interfaz del juego.

    Autores:
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
            texto += (mostrar_texto_con_color('acierto', 'verde'))
        else:
            texto += (f"{mostrar_texto_con_color('error', 'rojo')} - Palabra Correcta: {palabra}")
        print(texto)

    print()
    aciertos = jugadas.count('a')
    errores = jugadas.count('e')
    print(f"Aciertos: {mostrar_texto_con_color(str(aciertos), 'verde')}")
    print(f"Errores: {mostrar_texto_con_color(str(errores), 'rojo')}")
    print()
    print(f"Puntaje de la partida: {puntaje_partida} puntos")


def mostrar_total_de_palabras(diccionario_de_palabras):
    """
    Esta función muestra el total de palabras del diccionario, primero letra por letra, y luego el total de todo el diccionario.

    Parámetros:
        - No admite.

    Retorna:
        `None`. Esta función únicamente manipula la consola para mostrar al la información.

    Autores:
        * Brizuela, Natanael Daniel
        * Lewin, Iván
    """
    total_por_letra = total_palabras_por_letra(diccionario_de_palabras)
    total_en_diccionario = sum(total_por_letra.values())

    for letra in total_por_letra:
        cantidad = total_por_letra[letra]
        if cantidad != 1:
            print(f"Hay {cantidad} palabras que comienzan con la letra '{letra}'.")
        else:
            print(f"Hay {cantidad} palabra que comienza con la letra '{letra}'.")
    print()
    print(f"En total hay {total_en_diccionario} palabras.")
    print()
    input("Presione Enter (Inicio) para iniciar el juego ")


def preguntar_seguir_jugando():
    ingreso_del_usuario = aplanar_texto(input("¿Desea seguir jugando?: "))
    while ingreso_del_usuario not in ('si', 'no'):
        print(f"Por favor, ingrese 'si' o 'no'. ", end="")
        ingreso_del_usuario = aplanar_texto(input("¿Desea seguir jugando?: "))
    return ingreso_del_usuario == 'si'


def verificar_intento(ingreso_usuario:str,palabra_actual:str):
    """
    Esta funcion verifica que el ingreso del usuario se corresponda con la palabra a adivinar

    Parámetros:
        - ingreso_usuario:str
        - palabra_actual:str

    Retorna:
        `str`. Retorna la letra 'a' si es acertada o 'e' en caso contrario

    Autores:
        * Brizuela, Natanael Daniel
        * Lewin, Iván

    Esta funcion re

    >>> verificar_intento("AlmuÉrzo","almuerzo")
    'a'
    >>> verificar_intento("almurso","almuerzo")
    'e'
    """
    acierto=""

    if aplanar_texto(ingreso_usuario) == palabra_actual:
        acierto="a"

    else: 
        acierto="e"

    return acierto



if __name__ == '__main__':
    print(doctest.testmod())
