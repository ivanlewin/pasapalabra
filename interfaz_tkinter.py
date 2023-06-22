import csv
import doctest
import random
import tkinter as tk

UBICACION_USUARIOS = './archivos/usuarios.csv'
UBICACION_ICONO = './archivos/herencia.ico'

MAX_JUGADORES = 4

jugadores = []


def cerrar_ventana(ventana):
    '''
    Cierra la ventana actual.

    Parámetros
    ----------

    ventana : tk.TK
        Ventana que se quiera cerrar.

    Autores
    -------
    * Neme, Agustin Nadim
    '''
    ventana.destroy()


def validar_nombre(nombre_usuario):
    '''
    Esta funcion valida el nombre de usuario ingresado por el usuario para el registro de jugadores.
    Parámetros
    ----------
    nombre_usuario : str
        Nombre de usuario ingresado por la persona.

    Retorna
    -------
    bool
        'True' en caso de cumplir los requisitos, 'False' en caso contrario.

    Autores
    -------
    * Neme, Agustin Nadim

    Ejemplos
    --------
    >>> validar_nombre('usuario_123')
    False
    >>> validar_nombre('nombre-de-usuario')
    True
    >>> validar_nombre('nombre-muy-largo-1234')
    False
    '''
    validador = True
    if len(nombre_usuario) < 4 or len(nombre_usuario) > 20:
        validador = False

    if not nombre_usuario.replace('-', '').isalnum():
        validador = False

    with open(UBICACION_USUARIOS, 'a+') as archivo_csv:

        lector_csv = csv.reader(archivo_csv)

        for fila in lector_csv:
            if fila[0] == nombre_usuario:
                validador = False
    return validador


def validar_contrasenia(contrasenia, requisitos_label):
    '''
    Esta funcion valida contraseña ingresada por el usuario para el registro de jugadores.
    Parámetros
    ----------
    contrasenia : str
        Nombre de usuario ingresado por la persona.

    Retorna
    -------
    bool
        'True' en caso de cumplir los requisitos, 'False' en caso contrario.

    Autores
    -------
    * Neme, Agustin Nadim
    '''
    validador = True
    requisitos = []

    if len(contrasenia) < 6 or len(contrasenia) > 12:
        requisitos.append('- Debe tener entre 6 y 12 caracteres.')
        validador = False

    if not any(char.isupper() for char in contrasenia):
        requisitos.append('- Debe contener al menos una letra mayúscula.')
        validador = False

    if not any(char.islower() for char in contrasenia):
        requisitos.append('- Debe contener al menos una letra minúscula.')
        validador = False

    if not any(char.isdigit() for char in contrasenia):
        requisitos.append('- Debe contener al menos un número.')
        validador = False

    if not any(char in '#!' for char in contrasenia):
        requisitos.append('- Debe contener al menos uno de los caracteres especiales # o !.')
        validador = False

    requisitos_label.config(text='\n'.join(requisitos))

    return validador


def verificar_usuario_existente(nombre):
    '''
    Esta funcion verifica si el usuario ya fue creado anteriormente en el archivo csv.

    Parámetros
    ----------
    nombre : str
        Nombre de usuario ingresado por la persona.

    Retorna
    -------
    bool
        'True' en caso de estar registrado, 'False' en caso contrario.

    Autores
    -------
    * Neme, Agustin Nadim
    '''
    nombre_existente = False
    with open(UBICACION_USUARIOS, 'r', newline='') as usuario_csv:
        lector_csv = csv.reader(usuario_csv)
        for fila in lector_csv:
            if fila[0] == nombre:
                nombre_existente = True
    return nombre_existente


def escribir_usuario_en_csv(nombre, contrasenia):
    '''
    Esta funcion escribe el nombre y contrasenia del jugador dentro del archivo csv
    Parámetros
    ----------
    nombre : str
        Nombre de usuario ingresado por la persona.
    contrasenia : str
        Contraseña del usuario ingresado por la persona

    Autores
    -------
    * Neme, Agustin Nadim
    '''
    with open(UBICACION_USUARIOS, 'a', newline='') as usuario_csv:
        escritor_csv = csv.writer(usuario_csv)
        escritor_csv.writerow([nombre, contrasenia])
    return


def registrar_jugador(nombre_entry, contrasenia_entry, repetir_contrasenia_entry, resultado_label):
    '''
    Esta funcion registra al jugador dentro del archivo csv en caso de cumplir todos los requisitos solicitados por el programa.

    Parámetros
    ----------
    nombre_entry : str
        Nombre que dio el usuario al momento de iniciar sesion.
    contrasenia_entry : str
        Contrasenia que dio el usuario al momento de iniciar sesion.
    repetir_contrasenia_entry : str
        Misma contrasenia que dio el usuario al momento de iniciar sesion, debe coincidir con contrasenia_entry.
    resultado_label: label
        Etiqueta que da informacion al usuario.

    Autores
    -------
    * Neme, Agustin Nadim
    '''
    nombre = nombre_entry.get()
    contrasenia = contrasenia_entry.get()
    repetir_contrasenia = repetir_contrasenia_entry.get()
    mensaje = ''

    if not validar_nombre(nombre):
        mensaje = 'Nombre de usuario inválido.'
    elif verificar_usuario_existente(nombre):
        mensaje = 'Nombre de usuario ya existe.'
    elif contrasenia != repetir_contrasenia:
        mensaje = 'Las claves no coinciden.'
    elif not validar_contrasenia(contrasenia, resultado_label):
        mensaje = 'Clave inválida.'
    else:
        escribir_usuario_en_csv(nombre, contrasenia)
        mensaje = 'Jugador resgistrado con exito'

    resultado_label.config(text=mensaje)


def verificar_datos(nombre, contrasenia):
    '''
    Esta funcion verifica si hay coincidencia de nombre y contrasenia dentro del archivo csv.
    Parámetros
    ----------
    nombre : str
        Nombre de usuario ingresado por la persona.
    contrsenia : str
        Contrasenia de usuario ingresado por la persona.

    Retorna
    -------
    bool
        'True' en caso de estar registrado, 'False' en caso contrario.

    Autores
    -------
    * Neme, Agustin Nadim

    '''
    datos_validos = False
    with open(UBICACION_USUARIOS, 'r') as usuario_csv:
        lector_csv = csv.reader(usuario_csv)
        for fila in lector_csv:
            if fila[0] == nombre and fila[1] == contrasenia:
                datos_validos = True
    return datos_validos


def agregar_jugador(nombre_jugador):
    '''
    Esta funcion agrega los jugadores, si no estan, a una lista luego de iniciar sesion 
    Parámetros
    ----------
    nombre_jugador : str
        Nombre de usuario ingresado por la persona.

    Retorna
    -------
    jugadores: [list]
        Lista con todos los jugadores que hayan iniciado sesion.

    Autores
    -------
    * Neme, Agustin Nadim
    '''
    global jugadores
    if nombre_jugador not in jugadores:
        jugadores.append(nombre_jugador)
    random.shuffle(jugadores)
    return jugadores


def listar_jugadores(jugadores_actuales, listbox):
    '''
    Esta funcion verifica lista los jugadores dentro de una listbox para mostrar dentro de la interfaz.
    Parámetros
    ----------
    jugadores_actuales : [list]
        Lista con todos los jugadores que hayan iniciado sesion.
    listbox : listbox
        Lista con todos los jugadores que inicien sesion para mostrarlos en la interfaz.

    Autores
    -------
    * Neme, Agustin Nadim
    '''
    listbox.delete(0, tk.END)

    if jugadores_actuales:
        for i, jugador in enumerate(jugadores_actuales, 1):
            listbox.insert(tk.END, f'{i}. {jugador}')
    else:
        listbox.insert(tk.END, 'No hay jugadores registrados.')
    return


def iniciar_sesion(nombre_login_entry, contrasenia_login_entry, resultado_label, jugadores_listbox):
    '''
    Esta funcion inicia sesion con los datos brindados, si coinciden inicia sesion en el programa.

    Parámetros
    ----------
    nombre_login_entry : str
        Nombre que dio el usuario al momento de iniciar sesion.

    contrasenia_login_entry : str
        Contrasenia que dio el usuario al momento de iniciar sesion.

    resultado_label: label
        Etiqueta que da informacion al usuario.

    jugadores_listbox : listbox
        Lista con todos los jugadores que inicien sesion para mostrarlos en la interfaz.

    Autores
    -------
    * Neme, Agustin Nadim
    '''

    nombre = nombre_login_entry.get()
    contrasenia = contrasenia_login_entry.get()
    mensaje = ''

    if len(jugadores) >= MAX_JUGADORES:
        mensaje = 'Se alcanzo el limite de jugadores por partida'
    elif not verificar_usuario_existente(nombre):
        mensaje = 'Nombre de usuario no existe.'
    elif verificar_datos(nombre, contrasenia):
        mensaje = 'Inicio de sesión exitoso.'
        jugadores_actuales = agregar_jugador(nombre)
        listar_jugadores(jugadores_actuales, jugadores_listbox)

    else:
        mensaje = 'Datos incorrectos.'
        resultado_label.pack()

    resultado_label.config(text=mensaje)
    resultado_label.pack()

def comenzar_juego(ventana):
    if len(jugadores) < 1:
        messagebox.showerror("Error de jugadores", "Para comenzar el juego debe haber al menos un jugador.")
    else:
        ventana.destroy()

def formatear_ventanas(ventana, titulo):
    '''
    Esta funcion formatea las ventanas del programa .

    Parámetros
    ----------
    ventana: 
        Aquella ventana a la que se le quiera aplicar un formato
    titulo:
        Titulo que se le quiera aplicar a la ventana

    Autores
    -------
    * Neme, Agustin Nadim
    '''
    separador = tk.Frame(ventana, height=1, bd=1, relief=tk.SUNKEN)
    separador.pack(fill=tk.X, padx=10, pady=5)
    ventana.resizable(0, 0)
    ventana.title(titulo)
    ventana.iconbitmap(UBICACION_ICONO)
    ventana.geometry('700x400')


def ventana_registro(ventana_principal):
    '''
    Interfaz grafica que muestra una ventana para que el usuario pueda registrarse e iniciar sesion dentro de la plataforma.

    Parámetros
    ----------
    ventana_principal :
        Interfaz principal del programa.

    Autores
    -------
    * Neme, Agustin Nadim
    '''

    ventana_registro = tk.Toplevel(ventana_principal)

    formatear_ventanas(ventana_registro, 'Registro de jugadores')

    nombre_label = tk.Label(ventana_registro, text=f'Nombre de usuario:')
    nombre_label.pack()
    nombre_entry = tk.Entry(ventana_registro)
    nombre_entry.pack()

    contrasenia_label = tk.Label(ventana_registro, text='Contraseña:')
    contrasenia_label.pack()
    contrasenia_entry = tk.Entry(ventana_registro, show='*')
    contrasenia_entry.pack()

    contrasenia_entry.bind('<Button-1>',lambda event: validar_contrasenia(contrasenia_entry.get(), resultado_label))
    contrasenia_entry.bind('<KeyRelease>',lambda event: validar_contrasenia(contrasenia_entry.get(), resultado_label))

    repetir_contrasenia_label = tk.Label(ventana_registro, text='Repetir contraseña:')
    repetir_contrasenia_label.pack()
    repetir_contrasenia_entry = tk.Entry(ventana_registro, show='*')
    repetir_contrasenia_entry.pack()

    resultado_label = tk.Label(ventana_registro, text='')
    resultado_label.pack()

    registrar = tk.Button(ventana_registro, text='Registrarse', command=lambda: registrar_jugador(nombre_entry, contrasenia_entry, repetir_contrasenia_entry, resultado_label))
    registrar.pack()

    boton_cerrar = tk.Button(ventana_registro, text='Volver a inicio', command=lambda: cerrar_ventana(ventana_registro))
    boton_cerrar.pack()


def ventana_login(ventana_principal, jugadores_listbox):
    '''
    Interfaz grafica que muestra una ventana para que el usuario pueda iniciar sesion dentro de la plataforma.

    Parámetros
    ----------
    ventana_principal :
        Interfaz principal del programa.

    jugadores_listbox : listbox
        Lista con todos los jugadores que inicien sesion para mostrarlos en la interfaz.

    Autores
    -------
    * Neme, Agustin Nadim
    '''
    ventana_login = tk.Toplevel(ventana_principal)

    formatear_ventanas(ventana_login, 'Iniciar sesion')

    nombre_login_label = tk.Label(ventana_login, text='Nombre de usuario:')
    nombre_login_label.pack()
    nombre_login_entry = tk.Entry(ventana_login)
    nombre_login_entry.pack()

    contrasenia_login_label = tk.Label(ventana_login, text='Contraseña:')
    contrasenia_login_label.pack()
    contrasenia_login_entry = tk.Entry(ventana_login, show='*')
    contrasenia_login_entry.pack()

    resultado_label = tk.Label(ventana_login, text='')
    resultado_label.pack()

    registrar_boton = tk.Button(ventana_login, text='Registrarse', command=lambda: ventana_registro(ventana_principal))
    registrar_boton.pack()

    login_boton = tk.Button(ventana_login, text='Login', command=lambda: iniciar_sesion(nombre_login_entry, contrasenia_login_entry, resultado_label, jugadores_listbox))
    login_boton.pack()

    boton_cerrar = tk.Button(ventana_login, text='Volver a inicio', command=lambda: cerrar_ventana(ventana_login))
    boton_cerrar.pack()


from tkinter import messagebox
def ventana_main():
    '''
    Ventana main que muestra toda la informacion al jugador. Puede registrarse, iniciar sesion o cerrar el programa en caso necesario.

    Autores
    -------
    * Neme, Agustin Nadim
    '''
    ventana_principal = tk.Tk()
    formatear_ventanas(ventana_principal, 'Bienvenido al juego pasapalabra - Heredero')

    imagen = tk.PhotoImage(file="archivos/rosco_pasapalabra.png").subsample(2)
    mostrar_imagen = tk.Label(ventana_principal, image= imagen)
    mostrar_imagen.place(x=0, y=0, width=700, height=400)

    jugadores_label = tk.Label(ventana_principal, text='Jugadores: ')
    jugadores_label.pack()

    jugadores_listbox = tk.Listbox(ventana_principal)
    jugadores_listbox.pack()

    registrar_boton = tk.Button(ventana_principal, text='Registrarse', command=lambda: ventana_registro(ventana_principal))
    registrar_boton.pack()

    login_boton = tk.Button(ventana_principal, text='Login', command=lambda: ventana_login(ventana_principal, jugadores_listbox))
    login_boton.pack()

    comenzar_juego_boton = tk.Button(ventana_principal, text='Comenzar juego', command=lambda: comenzar_juego(ventana_principal))
    comenzar_juego_boton.pack()

    ventana_principal.mainloop()

    return jugadores


if __name__ == '__main__':
    print(doctest.testmod())
