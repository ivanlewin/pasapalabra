
from diccionario_palabras import *
from interfaz import *
from manejo_archivos import *


def generar_letras(lista_con_definiciones: list[list[str]]):
    """
    Esta función genera una lista de letras participantes.

    Parámetros:
        * lista_con_definiciones: list[list[str]]

    Retorna:
        `list[str]`

    Autores:
        * Armari, Valentino
        * Brizuela, Natanael Daniel
    """
    letras = [entrada_palabra[0][0].upper()
              for entrada_palabra in lista_con_definiciones]

    return letras


def ejecutar_partida(diccionario_de_palabras):
    """
    Esta función se encarga de integrar todas las funciones previas para que el juego opere correctamente.

    Parámetros:
        - No recibe

    Retorna:
        `None`

    Autores:
        * Armari, Valentino
        * Brizuela, Natanael Daniel
    """
    letras_participantes = obtener_letras_participantes()
    lista_con_definiciones = recibir_lista_definiciones_filtrado(
        diccionario_de_palabras, letras_participantes)

    letras = generar_letras(lista_con_definiciones)

    jugadas = []
    intentos = []

    for i in range(len(lista_con_definiciones)):
        turno_actual = lista_con_definiciones[i]
        turno_previo = lista_con_definiciones[i-1] if i > 0 else None
        palabra_actual: str = turno_actual[0]

        mostrar_interfaz_del_juego(letras, jugadas, turno_actual, turno_previo)
        ingreso_usuario = recibir_ingreso_usuario(
            palabra_actual, lambda: mostrar_interfaz_del_juego(letras, jugadas, turno_actual))
        intentos.append(ingreso_usuario)

        acierto = verificar_intento(ingreso_usuario, palabra_actual)
        jugadas.append(acierto)

    mostrar_resumen_de_la_partida(
        letras, jugadas, lista_con_definiciones, intentos)
    return calcular_puntaje_de_la_partida(jugadas)


def ejecutar_juego():
    """
    Esta función es la principal orquestadora del juego. Se encarga de obtener el rosco, llevar el conteo del puntaje y permitir al usuario juegue tantas partidas como desee.

    Parámetros:
        - No recibe

    Retorna:
        `None`

    Autores:
        * Armari, Valentino
        * Brizuela, Natanael Daniel
    """

    # creo el diccionario de palabras
    diccionario_de_palabras = devolver_diccionario()
    # para poder usarlo sin modificar nuestra estructura lo convierto a una lista
    lista_del_diccionario = hacerlo_lista(diccionario_de_palabras)

    diccionario_de_palabras = ordenar_filtrar_lista_de_listas(
        lista_del_diccionario)
    mostrar_total_de_palabras(lista_del_diccionario)

    puntaje_total = 0
    continuar_jugando = True
    while continuar_jugando:
        puntaje_de_la_partida = ejecutar_partida(diccionario_de_palabras)
        puntaje_total += puntaje_de_la_partida
        print()
        continuar_jugando = preguntar_seguir_jugando()

    print(f"Puntaje del juego: {puntaje_total} puntos")


if __name__ == '__main__':
    ejecutar_juego()
