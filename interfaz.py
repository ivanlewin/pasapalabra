import os
ROJO="\x1b[0;31m"
VERDE="\x1b[0;32m"
RESET="\033[0;m"

def limpiar_interfaz():
    """
    Esta función limpia la consola del usuario.

    Parámetros:
        No admite

    Retorna:
        `None`. Esta función únicamente manipula la consola para mostrar al usuario la interfaz del juego.
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
    """
    tablero_letras = ''
    for letra in letras:
        celda = f'[{letra}]'
        tablero_letras += celda

    tablero_jugadas = ''
    for i in range(len(letras)):
        if i < len(jugadas) and jugadas[i] == "a":
            # if i < len(jugadas) else '[ ]'
            celda = f"[{VERDE}{jugadas[i]}{RESET}]"

        elif i < len(jugadas) and jugadas[i] == "e":
            celda = f"[{ROJO}{jugadas[i]}{RESET}]"

        else:
            celda = "[ ]"
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
    """
    aciertos = jugadas.count('a')
    errores = jugadas.count('e')

    palabra_actual, definicion_actual = turno_actual
    letra_actual = palabra_actual[0]

    print(f'Aciertos: {VERDE}{aciertos}{RESET}')
    print(f'Errores: {ROJO}{errores}{RESET}')
    print(
        f'Turno letra {VERDE}{letra_actual.upper()}{RESET} - Palabra de {VERDE}{len(palabra_actual)}{RESET} letras')
    print(f'\x1b[4;37mDefinición\033[0;m: {definicion_actual}\n') 

def mostrar_palabra_correcta(jugadas: list[str], turno_previo: list[str]):
    """
    Si el intento del usuario en el turno anterior fue un error, esta función muestra la palabra correcta en pantalla.

    Parámetros:
        * jugadas `list['a', 'e']`: El resultado de las jugadas ya realizadas por el usuario (debe ser una lista donde cada elemento es o bien 'a', para indicar un acierto, o bien 'e' para indicar un error).
        * turno_previo `list[str, str]`: Una lista con dos strings; el primero es la palabra a adivinar, y el segundo es la definición de esa palabra.

    Retorna:
        `None`. Esta función únicamente manipula la consola para mostrar al usuario la interfaz del juego.
    """

    ultima_jugada = jugadas[-1] if len(jugadas) > 0 else None
    palabra_correcta = turno_previo[0]
    if ultima_jugada == "e" and palabra_correcta:
        print(
            f"{ROJO}Incorrecto{RESET}, la palabra correcta es: {palabra_correcta}")


# =None hace que sea un parametro opcional
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
    """
    limpiar_interfaz()
    mostrar_tableros(letras, jugadas)
    print()
    if turno_previo is not None:
        mostrar_palabra_correcta(jugadas, turno_previo)
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
    """

    palabra_valida = None
    ingreso_del_usuario = input("Ingrese palabra: ")

    while palabra_valida is None:
        if not ingreso_del_usuario.isalpha():
            generar_interfaz()
            print()
            print(
                f"{ROJO}Error{RESET}: por favor ingrese solo {ROJO}letras{RESET}")
            ingreso_del_usuario = input("Ingrese palabra: ")
        elif len(ingreso_del_usuario) != len(palabra_actual):
            generar_interfaz()
            print()
            print(
                f"{ROJO}Error{RESET}: por favor ingrese palabras de {ROJO}{len(palabra_actual)}{RESET} letras")
            ingreso_del_usuario = input("Ingrese palabra: ")
        else:
            palabra_valida = ingreso_del_usuario

    return ingreso_del_usuario


def mostrar_resumen(letras: list[str], jugadas: list[str], turnos: list[list[str]], lista_palabras_ingresadas: list[str]):
    """
    Esta función muestra el resumen luego de finalizar el juego.

    Parámetros:
        * letras `list[str]`: Una lista de las letras que participan en este juego.
        * jugadas `list['a', 'e']`: El resultado de las jugadas ya realizadas por el usuario (debe ser una lista donde cada elemento es o bien 'a', para indicar un acierto, o bien 'e' para indicar un error).
        * turnos `list[list[str, str]]`: La lista de las palabras del juego: Cada elemento es una lista de strings donde el primer elemento es la palabra a adivinar, y el segundo es la definición de esa palabra.
        * lista_palabras_ingresadas `list[str]`: Una lista con los ingresos del usuario (aciertos y errores).

    Retorna:
        `None`. Esta función únicamente manipula la consola para mostrar al usuario la interfaz del juego.
    """
    limpiar_interfaz()
    mostrar_tableros(letras, jugadas)

    print()
    for i in range(len(letras)):
        letra = letras[i]
        jugada = jugadas[i]
        turno = turnos[i]
        palabra = turno[0]
        ingreso = lista_palabras_ingresadas[i]
        if jugada == "e":
            print(
                f"Turno letra {ROJO}{letra.upper()}{RESET} - Palabra de {len(palabra)} letras - {ingreso} - {ROJO} error {RESET}- Palabra Correcta: {VERDE}{palabra}{RESET}")
        else:
            print(
                f"Turno letra {VERDE}{letra.upper()}{RESET} - Palabra de {len(palabra)} letras - {ingreso} -{VERDE} acierto{RESET} ")

    print()
    print(f"Puntaje final:{VERDE} 100{RESET} ganaste!!")



