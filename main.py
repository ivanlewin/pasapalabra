from diccionario_palabras import *
from interfaz import *


def interaccion_con_usuario(turnos: list[list[str]]):
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
    letras = [turno[0][0].upper() for turno in turnos]
    jugadas = []
    lista_palabras_ingresadas = []

    for i in range(len(turnos)):
        turno_actual = turnos[i]
        turno_previo = turnos[i-1] if i > 0 else None
        palabra_actual: str = turno_actual[0]

        mostrar_interfaz_del_juego(letras, jugadas, turno_actual, turno_previo)
        ingreso_usuario = recibir_ingreso_usuario(palabra_actual, lambda: mostrar_interfaz_del_juego(letras, jugadas, turno_actual))
        lista_palabras_ingresadas.append(ingreso_usuario)
        if ingreso_usuario.lower() == palabra_actual.lower():
            jugadas.append('a')
        else:
            jugadas.append('e')

    mostrar_resumen(letras, jugadas, turnos, lista_palabras_ingresadas)


def integracion_de_juego():
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
    definiciones_filtradas = ordenar_filtrar_lista_de_listas()
    lista_con_definiciones = recibir_lista_definiciones_filtrado(definiciones_filtradas, lista_letras2)

    interaccion_con_usuario(lista_con_definiciones)


integracion_de_juego()
