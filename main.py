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


def recibir_ingreso_usuario(turno_actual: list[str], generar_interfaz: any):
    """
    Esta función recibe el input del usuario y realiza las validaciones para asegurarse de que es correcto.

    Parámetros:
        * turno_actual `list[str, str]`: Una lista con dos strings; el primero es la palabra a adivinar, y el segundo es la definición de esa palabra.
        * generar_interfaz `function`: Función que permite generar la interfaz de usuario.

    Retorna:
        `str`. Retorna un string con caracteres alfabéticos de la longitud de la palabra a adivinar en el turno actual.
    """
    palabra_valida = None
    ingreso_del_usuario = input("Ingrese palabra: ")
    while palabra_valida is None:
        if not ingreso_del_usuario.isalpha():
            generar_interfaz()
            print("Error: por favor ingrese solo letras")
            ingreso_del_usuario = input("Ingrese palabra: ")
        elif len(ingreso_del_usuario) != len(turno_actual[0]):
            generar_interfaz()
            print(f"Error: por favor ingrese palabras de {len(turno_actual[0])} letras")
            ingreso_del_usuario = input("Ingrese palabra: ")
        else:
            palabra_valida = ingreso_del_usuario
    return ingreso_del_usuario



def interaccion_con_usuario(turnos):
    """
    Esta función se encarga de interactuar con el usuario. Recibe la lista de palabras que participan del juego y lo lleva a cabo.
    """
    letras = [turno[0][0].upper() for turno in turnos] # ['A', 'J']
    jugadas=[]
    
    for turno in turnos: 
        

        mostrar_interfaz(letras, jugadas, turno)# turno paramatero opcional
        ingreso_usuario = recibir_ingreso_usuario(turno, lambda: mostrar_interfaz(letras, jugadas, turno))
        
        if ingreso_usuario.lower()==turno[0]:
            jugadas.append("a")
        else:
            jugadas.append("e")


palabras = [
    ['araña', "1.  f. Arácnido con tráqueas ..."],
    ['jardín', "1.  m. Terreno donde se cultivan plantas con fines ornamentales"],
    ]

interaccion_con_usuario(palabras)




