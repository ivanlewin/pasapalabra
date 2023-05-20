from diccionario_palabras import *
from interfaz import *


def interaccion_con_usuario(lista_con_definiciones: list[list[str]]):
    """
    Esta función se encarga de interactuar con el usuario. Recibe la lista de palabras que participan del juego y lo lleva a cabo.

    Parámetros:
        * turnos `list[list[str, str]]`: La lista de las palabras del juego: Cada elemento es una lista de strings donde el primer elemento es la palabra a adivinar, y el segundo es la definición de esa palabra.

    Retorna:
        `None`

    Autores:
        * Armari, Valentino
        * Brizuela, Natanael Daniel
    """
    letras = [entrada_palabra[0][0].upper() for entrada_palabra in lista_con_definiciones]
    jugadas = []
    lista_palabras_ingresadas = []

    for i in range(len(lista_con_definiciones)):

        turno_actual = lista_con_definiciones[i]
        turno_previo = lista_con_definiciones[i-1] if i > 0 else None
        palabra_actual: str = turno_actual[0]

        mostrar_interfaz_del_juego(letras, jugadas, turno_actual, turno_previo)
        ingreso_usuario = recibir_ingreso_usuario(palabra_actual, lambda: mostrar_interfaz_del_juego(letras, jugadas, turno_actual))
        lista_palabras_ingresadas.append(ingreso_usuario)
        if ingreso_usuario.lower() == palabra_actual.lower():
            jugadas.append('a')
        else:
            jugadas.append('e')

    return (letras, jugadas, lista_palabras_ingresadas)


def jugar_partida():
    """
    Esta función se encarga de integrar todas las funciones previas para que el juego opere correctamente.

    Parámetros:
        - No admite

    Retorna:
        `None`

    Autores:
        * Armari, Valentino
        * Brizuela, Natanael Daniel
    """
    lista_letras2 = obtener_letras_participantes()
    diccionario_filtrado = ordenar_filtrar_lista_de_listas()
    lista_con_definiciones = recibir_lista_definiciones_filtrado(diccionario_filtrado, lista_letras2)

    letras, jugadas, intentos = interaccion_con_usuario(lista_con_definiciones)

    mostrar_resumen(letras, jugadas, lista_con_definiciones, intentos)
    return calcular_puntaje_de_la_partida(jugadas)


def desea_seguir_jugando():
    ingreso = sacar_tildes(input("¿Desea seguir jugando? (ingrese 'si' o 'no'): ").lower())
    while ingreso not in ('si', 'no'):
        ingreso = sacar_tildes(input("Por favor, ingrese 'si' o 'no'. ¿Desea seguir jugando?: ").lower())
    return ingreso == 'si'


def jugar_mientras_el_usuario_quiera():
    puntaje = 0
    continuar_jugando = True
    while continuar_jugando:
        puntaje += jugar_partida()
        continuar_jugando = desea_seguir_jugando()

    print(f"Puntaje del juego: {puntaje} puntos")


jugar_mientras_el_usuario_quiera()
