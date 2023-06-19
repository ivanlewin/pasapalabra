import tkinter as tk
from tkinter import ttk
import csv
import random
MAX_JUGADORES = 4

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

    if not validar_nombre(nombre):
        resultado_label.config(text= "Nombre de usuario invalido.")
        return
    
    if verificar_usuario_existente(nombre):
        resultado_label.config(text= "Nombre de usuario ya existe.")
        return

    if contrasenia != repetir_contrasenia:
        resultado_label.config(text= "Las claves no coinciden.")
        return

    if not validar_contrasenia(contrasenia):
        resultado_label.config(text= "Clave invalida.")
        return
    
    escribir_usuario_en_csv(nombre, contrasenia)
    resultado_label.config(text="Jugador resgistrado con exito")

def verificar_datos(nombre, contrasenia):
    datos_validos = False
    with open("usuarios.csv", "r") as usuario_csv:
        lector_csv = csv.reader(usuario_csv)
        for fila in lector_csv:
            if fila[0] == nombre and fila[1] == contrasenia:
                datos_validos = True
    return datos_validos

jugadores = []

def listar_jugadores(lista_jugadores):
    random.shuffle(jugadores)
    #lista_jugadores.delete(0, tk.END)  # Limpiar la lista de jugadores existente
    
    for i, jugador in enumerate(jugadores, start=1):
        lista_jugadores.insert(tk.END, f"{i}. {jugador}")

def cerrar_ventana(ventana):
    ventana.destroy()

def iniciar_sesion(nombre_login_entry, contrasenia_login_entry, resultado_label):
    nombre = nombre_login_entry.get()
    contrasenia = contrasenia_login_entry.get()

    if not verificar_usuario_existente(nombre):
        resultado_label.config(text="Nombre de usuario no existe.")
        return

    if verificar_datos(nombre, contrasenia):
        resultado_label.config(text="Inicio de sesión exitoso.")
        resultado_label.pack()
        jugadores.append(nombre)
        listar_jugadores()  
    else:
        resultado_label.config(text="Datos incorrectos.")
        resultado_label.pack()

    return jugadores


def ventana_registro(ventana_principal):
    ventana_registro = tk.Toplevel(ventana_principal)
    ventana_registro.title("Registro de Jugadores")
    ventana_registro.geometry("600x300")

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

    separador = tk.Frame(ventana_registro, height=1, bd=1, relief=tk.SUNKEN)
    separador.pack(fill=tk.X, padx=10, pady=5)

    resultado_label = tk.Label(ventana_registro, text="")
    resultado_label.pack()

    registrar = tk.Button(ventana_registro, text= "Registrarse", command=lambda: registrar_jugador(nombre_entry, contrasenia_entry, repetir_contrasenia_entry, resultado_label))
    registrar.pack()

    boton_cerrar = tk.Button(ventana_registro, text="Volver a inicio", command=lambda: cerrar_ventana(ventana_registro))
    boton_cerrar.pack()

    
def ventana_login(ventana_principal):
    
    ventana_login = tk.Toplevel(ventana_principal)
    ventana_login.title("Login de jugadores")
    ventana_login.geometry("600x300")

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
    
    login_boton = tk.Button(ventana_login, text="Login", command=lambda: iniciar_sesion(nombre_login_entry, contrasenia_login_entry, resultado_label))
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
    lista_jugadores = tk.Listbox(ventana_principal)
    lista_jugadores.pack()

    registrar_boton = ttk.Button(ventana_principal, text= "Registrarse",  command=lambda: ventana_registro(ventana_principal))
    registrar_boton.pack()

    login_boton = ttk.Button(ventana_principal, text= "Login", command=lambda: ventana_login(ventana_principal))
    login_boton.pack()

    listar_jugadores(jugadores)
    ventana_principal.mainloop()

ventana_main()