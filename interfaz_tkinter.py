import tkinter as tk
from tkinter import ttk
import csv
import random
import os

MAX_JUGADORES = 4
jugadores = []

def cerrar_ventana(ventana):
    ventana.destroy()
    return

def validar_nombre(nombre_usuario):
    '''
    >>> validar_nombre("usuario_123")
    False
    >>> validar_nombre("nombre-de-usuario")
    True
    >>> validar_nombre("nombre-muy-largo-1234")
    False
    '''
    validador = True
    if len(nombre_usuario) < 4 or len(nombre_usuario) >20:
        validador = False

    if not nombre_usuario.replace("-", "").isalnum():
        validador = False

    with open("usuarios.csv", "r") as archivo_csv:
    
        lector_csv = csv.reader(archivo_csv)

        for fila in lector_csv:
            if fila[0] == nombre_usuario:
                validador = False
    return validador

def validar_contrasenia(contrasenia):
    '''
    >>> validar_contrasenia("Abc123!")
    True
    >>> validar_contrasenia("contrasenia")
    False
    >>> validar_contrasenia("MiContrasenia1")
    False
    >>> validar_contrasenia("abc123")
    False
    '''
    validador = True
    tiene_longitud_correcta = True
    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_numero = False
    tiene_caracter_especial = False

    if len(contrasenia) < 6 or len(contrasenia) > 12:
        validador = False
    
    caracteres_permitidos = set("#!")
    for caracter in contrasenia:
        if caracter.isupper():
            tiene_mayuscula = True
        elif caracter.islower():
            tiene_minuscula = True
        elif caracter.isdigit():
            tiene_numero = True
        elif caracter in caracteres_permitidos:
            tiene_caracter_especial = True

    validador = tiene_caracter_especial and tiene_mayuscula and tiene_minuscula and tiene_longitud_correcta and tiene_numero

    return validador

def verificar_usuario_existente(nombre):
    nombre_existente = False
    with open("usuarios.csv", "r", newline="") as usuario_csv:
        lector_csv = csv.reader(usuario_csv)
        for fila in lector_csv:
            if fila[0] == nombre:
                nombre_existente = True
    return nombre_existente

def escribir_usuario_en_csv(nombre, contrasenia):
    with open("usuarios.csv", "a", newline="") as usuario_csv:
        escritor_csv = csv.writer(usuario_csv)
        escritor_csv.writerow([nombre, contrasenia])
    return

def registrar_jugador(nombre_entry, contrasenia_entry, repetir_contrasenia_entry, resultado_label):
    nombre = nombre_entry.get()
    contrasenia = contrasenia_entry.get()
    repetir_contrasenia = repetir_contrasenia_entry.get()
    mensaje = ""

    if not validar_nombre(nombre):
        mensaje = "Nombre de usuario invalido."
    elif verificar_usuario_existente(nombre):
        mensaje = "Nombre de usuario ya existe."  
    elif contrasenia != repetir_contrasenia:
        mensaje = "Las claves no coinciden."       
    elif not validar_contrasenia(contrasenia):
        mensaje = "Clave invalida."
    else:
        escribir_usuario_en_csv(nombre, contrasenia)
        mensaje = "Jugador resgistrado con exito"

    resultado_label.config(text=mensaje)
    
    return



def verificar_datos(nombre, contrasenia):
    datos_validos = False
    with open("usuarios.csv", "r") as usuario_csv:
        lector_csv = csv.reader(usuario_csv)
        for fila in lector_csv:
            if fila[0] == nombre and fila[1] == contrasenia:
                datos_validos = True
    return datos_validos

def agregar_jugador(nombre_jugador):

    global jugadores
    if nombre_jugador not in jugadores:
        jugadores.append(nombre_jugador)
    random.shuffle(jugadores)
    return jugadores

def listar_jugadores(jugadores_actuales, listbox):
    listbox.delete(0, tk.END)

    if jugadores_actuales:
        for i, jugador in enumerate(jugadores_actuales,1):
            listbox.insert(tk.END, f"{i}. {jugador}")
    else:
       listbox.insert(tk.END, "No hay jugadores registrados.")

    return jugadores_actuales


def iniciar_sesion(nombre_login_entry, contrasenia_login_entry, resultado_label, jugadores_listbox):
    nombre = nombre_login_entry.get()
    contrasenia = contrasenia_login_entry.get()
    mensaje = ""

    if len(jugadores) >= MAX_JUGADORES:
        mensaje = "Se alcanzo el limite de jugadores por partida"
    elif not verificar_usuario_existente(nombre):
        mensaje = "Nombre de usuario no existe."
    elif verificar_datos(nombre, contrasenia):
        mensaje = "Inicio de sesión exitoso."
        jugadores_actuales = agregar_jugador(nombre)

    else:
        mensaje = "Datos incorrectos."
        resultado_label.pack()
    
    resultado_label.config(text= mensaje)
    resultado_label.pack()

    listar_jugadores(jugadores_actuales, jugadores_listbox)

    return


def ventana_registro(ventana_principal):
    ventana_registro = tk.Toplevel(ventana_principal)
    ventana_registro.title("Registro de Jugadores")
    ventana_registro.geometry("600x300")

    separador = tk.Frame(ventana_registro, height=1, bd=1, relief=tk.SUNKEN)
    separador.pack(fill=tk.X, padx=10, pady=5)

    nombre_label = tk.Label(ventana_registro, text=f"Nombre de usuario:")
    nombre_label.pack()
    nombre_entry = tk.Entry(ventana_registro)
    nombre_entry.pack()

    contrasenia_label = tk.Label(ventana_registro, text="Contraseña:")
    contrasenia_label.pack()
    contrasenia_entry = tk.Entry(ventana_registro, show="*")
    contrasenia_entry.pack()

    repetir_contrasenia_label = tk.Label(ventana_registro, text="Repetir contraseña:")
    repetir_contrasenia_label.pack()
    repetir_contrasenia_entry = tk.Entry(ventana_registro, show="*")
    repetir_contrasenia_entry.pack()

    resultado_label = tk.Label(ventana_registro, text="")
    resultado_label.pack()

    registrar = tk.Button(ventana_registro, text= "Registrarse", command=lambda: registrar_jugador(nombre_entry, contrasenia_entry, repetir_contrasenia_entry, resultado_label))
    registrar.pack()

    boton_cerrar = tk.Button(ventana_registro, text="Volver a inicio", command=lambda: cerrar_ventana(ventana_registro))
    boton_cerrar.pack()

    
def ventana_login(ventana_principal, jugadores_listbox):
    
    ventana_login = tk.Toplevel(ventana_principal)
    ventana_login.title("Login de jugadores")
    ventana_login.geometry("600x300")

    separador = tk.Frame(ventana_login, height=1, bd=1, relief=tk.SUNKEN)
    separador.pack(fill=tk.X, padx=10, pady=5)

    nombre_login_label = tk.Label(ventana_login, text="Nombre de usuario:")
    nombre_login_label.pack()
    nombre_login_entry = tk.Entry(ventana_login)
    nombre_login_entry.pack()

    contrasenia_login_label = tk.Label(ventana_login, text="Contraseña:")
    contrasenia_login_label.pack()
    contrasenia_login_entry = tk.Entry(ventana_login, show="*")
    contrasenia_login_entry.pack()

    resultado_label = tk.Label(ventana_login, text="")
    resultado_label.pack()


    registrar_boton = tk.Button(ventana_login, text="Registrarse", command=lambda: ventana_registro(ventana_principal))
    registrar_boton.pack()
    
    login_boton = tk.Button(ventana_login, text="Login", command=lambda: iniciar_sesion(nombre_login_entry, contrasenia_login_entry, resultado_label, jugadores_listbox))
    login_boton.pack()

    boton_cerrar = tk.Button(ventana_login, text="Volver a inicio", command=lambda: cerrar_ventana(ventana_login))
    boton_cerrar.pack()


#Creacion de ventana principal
def ventana_main():
    ventana_principal = tk.Tk()
    ventana_principal.title("Login Jugadores")
    ventana_principal.geometry("600x300")
    ventana_principal.configure(bg="#FE4A49")

    jugadores_label = ttk.Label(ventana_principal, text="Jugadores: ")
    jugadores_label.pack()

    jugadores_listbox = tk.Listbox(ventana_principal)
    jugadores_listbox.pack()

    registrar_boton = ttk.Button(ventana_principal, text= "Registrarse",  command=lambda: ventana_registro(ventana_principal))
    registrar_boton.pack()

    login_boton = ttk.Button(ventana_principal, text= "Login", command=lambda: ventana_login(ventana_principal, jugadores_listbox))
    login_boton.pack()

    boton_cerrar = tk.Button(ventana_principal, text="Cerrar programa", command=lambda: cerrar_ventana(ventana_principal))
    boton_cerrar.pack()

    ventana_principal.mainloop()

ventana_main()