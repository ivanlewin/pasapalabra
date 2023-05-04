import os


def limpiar_interfaz():
    """
    Esta función limpia la consola del usuario
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def mostrar_interfaz(letras, jugadas, turno_actual):
    """
    Esta función muestra el progreso del juego en pantalla.

    letras : list[str]
        Las letras que participan en este juego
    jugadas : list['a', 'e']:
        El resultado de las jugadas ya realizadas por el usuario
    turno_actual : list[str, str]:
        Una lista con dos strings; el primero es la palabra a adivinar, y el segundo es la definición de esa palabra
    """
    tablero_letras = ''
    for letra in letras:
        celda = f'[{letra}]'
        tablero_letras += celda

    tablero_jugadas = ''
    for i in range(10):
        celda = f'[{jugadas[i]}]' if i < len(jugadas) else '[ ]'
        tablero_jugadas += celda

    aciertos = jugadas.count('a')
    errores = jugadas.count('e')

    palabra_actual, definicion_actual = turno_actual
    letra_actual = palabra_actual[0]

    limpiar_interfaz()
    print(tablero_letras)
    print(tablero_jugadas)
    print()
    print()
    print(f'Aciertos: {aciertos}')
    print(f'Errores: {errores}')
    print(
        f'Turno letra {letra_actual} - Palabra de {len(palabra_actual)} letras')
    print(f'Definición: {definicion_actual}')


# # palabras = [
# #     {'Araña': "1.  f. Arácnido con tráqueas ..."},
# #     {'Jardín': "1.  m. Terreno donde se cultivan plantas con fines ornamentales"},
# # ]
# def interaccion_con_usuario(palabras):
#     """
#     Esta función se encarga de interactuar con el usuario. Recibe la lista de palabras que participan del juego y lo lleva a cabo.
#     """
#     # turno_actual = None
#     letras = [palabra[0] for palabra in palabras.keys()]  # ['A', 'J']
#     jugadas = ['a', 'e', 'a', 'a']
#     mostrar_interfaz(letras, jugadas)
