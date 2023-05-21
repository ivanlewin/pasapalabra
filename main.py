from datos import obtener_lista_definiciones
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
        if aplanar_texto(ingreso_usuario) == palabra_actual:
            jugadas.append('a')
        else:
            jugadas.append('e')

    return (letras, jugadas, lista_palabras_ingresadas)


def ejecutar_partida(diccionario_de_palabras):
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
    listas_participantes = obtener_letras_participantes()
    lista_con_definiciones = recibir_lista_definiciones_filtrado(diccionario_de_palabras, listas_participantes)

    letras, jugadas, intentos = interaccion_con_usuario(lista_con_definiciones)

    mostrar_resumen(letras, jugadas, lista_con_definiciones, intentos)
    return calcular_puntaje_de_la_partida(jugadas)


def ejecutar_juego():
    diccionario_de_palabras = obtener_lista_definiciones()
    diccionario_de_palabras = ordenar_filtrar_lista_de_listas(diccionario_de_palabras)
    mostrar_total_de_palabras(diccionario_de_palabras)

    puntaje_total = 0
    continuar_jugando = True
    while continuar_jugando:
        puntaje_de_la_partida = ejecutar_partida(diccionario_de_palabras)
        puntaje_total += puntaje_de_la_partida
        continuar_jugando = preguntar_seguir_jugando()

    print(f"Puntaje del juego: {puntaje_total} puntos")


if __name__ == '__main__':
    ejecutar_juego()
