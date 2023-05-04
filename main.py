import os


def limpiar_interfaz():
    """
    Esta función limpia la consola del usuario.

    Parámetros:
        No admite

    Retorna:
        `None`. Esta función únicamente manipula la consola para mostrar al usuario la interfaz del juego.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def mostrar_interfaz(letras: list[str], jugadas: list[str], turno_actual: list[str]):
    """
    Esta función muestra el progreso del juego en pantalla.

    Parámetros:
        * letras `list[str]`: Una lista de las letras que participan en este juego.
        * jugadas `list['a', 'e']`: El resultado de las jugadas ya realizadas por el usuario (debe ser una lista donde cada elemento es o bien 'a', para indicar un acierto, o bien 'e' para indicar un error).
        * turno_actual `list[str, str]`: Una lista con dos strings; el primero es la palabra a adivinar, y el segundo es la definición de esa palabra.

    Retorna:
        `None`. Esta función únicamente manipula la consola para mostrar al usuario la interfaz del juego.
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
        f'Turno letra {letra_actual.upper()} - Palabra de {len(palabra_actual)} letras')
    print(f'Definición: {definicion_actual}')


def recibir_ingreso_usuario(turno_actual,reiniciar_interfaz):
    """
    Esta función recibe el input del usuario y realiza las validaciones para asegurarse de que es correcto.
    """
    palabra_validad=None

    palabra=input("Ingrese palabra: ")
    while palabra_validad is None:

        if not palabra.isalpha():
            reiniciar_interfaz()
            palabra=input("error, por favor ingrese solo letras: ")

        elif len(palabra)!= len(turno_actual[0]):
            reiniciar_interfaz()
            palabra=input(f"error, por favor ingrese palbras con {len(turno_actual[0])} letras: ")
        
        else:
            palabra_validad=palabra
        

    return palabra







letras = ['A', 'C', 'D', 'G', 'I', 'L', 'M', 'P', 'S', 'V']
jugadas = ['a', 'e', 'a', 'a']
turno_actual = ["Jardín", "1.  m. Terreno donde se cultivan plantas con fines ornamentales"]

mostrar_interfaz(letras,jugadas,turno_actual)
ingreso_usuario=recibir_ingreso_usuario(turno_actual,lambda: mostrar_interfaz(letras,jugadas,turno_actual))

print(f"el usuario ingreso {ingreso_usuario} ")
