from diccionario_palabras import *
from interfaz import *


def interaccion_con_usuario(turnos: list[list[str]]):
    """
    Esta función se encarga de interactuar con el usuario. Recibe la lista de palabras que participan del juego y lo lleva a cabo.

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

    mostrar_resumen(letras, jugadas, turnos, lista_palabras_ingresadas)  # -->


def integracion_de_juego():
    """
    Esta función se encarga de integrar todas las funciones previas para que el juego opere correctamente.

    Autores:
        * Armari, Valentino
        * Brizuela, Natanael Daniel
    """
    lista_letras2 = obtener_letras_participantes()
    diccionario_filtrado = ordenar_filtrar_diccionario()
    lista_con_definiciones = recibir_lista_diccionario_filtrado(diccionario_filtrado, lista_letras2)

    interaccion_con_usuario(lista_con_definiciones)


integracion_de_juego()