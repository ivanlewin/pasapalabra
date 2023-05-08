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


def mostrar_tableros(letras: list[str], jugadas: list[str]):
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
    for i in range(len(letras)):
        celda = f'[{jugadas[i]}]' if i < len(jugadas) else '[ ]'
        tablero_jugadas += celda



    
    print(tablero_letras)
    print(tablero_jugadas)
    


def mostrar_turno_actual(jugadas: list[str], turno_actual: list[str]):
    """
    Esta función muestra el progreso del juego en pantalla.

    Parámetros:
        * letras `list[str]`: Una lista de las letras que participan en este juego.
        * jugadas `list['a', 'e']`: El resultado de las jugadas ya realizadas por el usuario (debe ser una lista donde cada elemento es o bien 'a', para indicar un acierto, o bien 'e' para indicar un error).
        * turno_actual `list[str, str]`: Una lista con dos strings; el primero es la palabra a adivinar, y el segundo es la definición de esa palabra.

    Retorna:
        `None`. Esta función únicamente manipula la consola para mostrar al usuario la interfaz del juego.
    """
    

    aciertos = jugadas.count('a')
    errores = jugadas.count('e')

    palabra_actual, definicion_actual = turno_actual
    letra_actual = palabra_actual[0]


    print(f'Aciertos: {aciertos}')
    print(f'Errores: {errores}')
    print(
        f'Turno letra {letra_actual.upper()} - Palabra de {len(palabra_actual)} letras')
    print(f'Definición: {definicion_actual}')


def mostrar_palabra_correcta(jugadas,turno_previo):
    
    palabra_correcta=turno_previo[0] 

    ultima_jugada=jugadas[-1] if len(jugadas)>0 else None

    if ultima_jugada == "e" and palabra_correcta is not None:
        print(f"Incorrecto, la palabra correcta es: {palabra_correcta}")



def mostrar_interfaz(letras: list[str], jugadas: list[str], turno_actual: list[str]=None,turno_previo:list[str]=None): #=None hace que sea un parametro opcional 

    limpiar_interfaz()
    mostrar_tableros(letras,jugadas)
    print()
    if turno_previo is not None:
        mostrar_palabra_correcta(jugadas,turno_previo)
    print()
    if turno_actual is not None:
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
            print("\nError: por favor ingrese solo letras")
            ingreso_del_usuario = input("Ingrese palabra: ")

        elif len(ingreso_del_usuario) != len(palabra_actual):
            generar_interfaz()
            print(f"\nError: por favor ingrese palabras de {len(palabra_actual)} letras")

            ingreso_del_usuario = input("Ingrese palabra: ")
        else:
            palabra_valida = ingreso_del_usuario

    return ingreso_del_usuario


def mostrar_resumen(letras,jugadas,turnos,lista_palabras_ingresadas):



    limpiar_interfaz()
    mostrar_tableros(letras,jugadas)
    
    print()
    for i in range(len(letras)):
        
        letra=letras[i]
        jugada=jugadas[i]
        turno=turnos[i]
        palabra= turno[0]
        ingreso=lista_palabras_ingresadas[i]

        if jugada=="e":
            print(f"Truno letra {letra} - palabra de {len(palabra)} letras -{ingreso} - error - Palabra Correcta: {palabra}")
        else:
            print(f"Truno letra {letra} - palabra de {len(palabra)} letras -{ingreso} - acierto ")   

    
    print("\nPuntaje Final: 100 ganaste!!")


def interaccion_con_usuario(turnos):
    """
    Esta función se encarga de interactuar con el usuario. Recibe la lista de palabras que participan del juego y lo lleva a cabo.
    """
    letras = [turno[0][0].upper() for turno in turnos]
    jugadas = []
    lista_palabras_ingresadas=[]

    for i in range(len(turnos)):

        turno_actual=turnos[i]
        turno_previo=turnos[i-1] if i>0 else None
        palabra_actual: str = turno_actual[0]

        mostrar_interfaz(letras, jugadas, turno_actual,turno_previo)
        ingreso_usuario = recibir_ingreso_usuario(
            palabra_actual, lambda: mostrar_interfaz(letras, jugadas, turno_actual))

        lista_palabras_ingresadas.append(ingreso_usuario)

        if ingreso_usuario.lower() == palabra_actual.lower():
            jugadas.append("a")
            

        else:
            jugadas.append("e")
            print(f"Incorrecto, la palabra correcta es: {palabra_actual}")
            
    mostrar_resumen(letras,jugadas,turnos,lista_palabras_ingresadas)  ##-->

    


palabras = [
    ["araña", "1.  f. Arácnido con tráqueas ..."],
    ["balanza", "1.  f. Aparato que sirve para pesar"],
    ["deambular", "1.  intr. Andar caminar sin dirección determinada"],
    ["jardín", "1.  m. Terreno donde se cultivan plantas con fines ornamentales"],
    ["naipe", "1.  m. Carta de la baraja"],
    ["yen", "1.  m. Unidad monetaria del"],
]

interaccion_con_usuario(palabras)
