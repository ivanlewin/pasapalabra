from diccionario_palabras import *
CORTE = ""


def abrir_linea(archivo, es_csv=False):
    
    linea = archivo.readline().rstrip() if not es_csv else archivo.readline().rstrip().split(",")

    if not linea:
        linea = CORTE
    return linea


def cumple_criterio(palabra):

    criterio = False
    if len(palabra) >= MINIMO_CARACTERES_PALABRAS:
        criterio = True
        
    return criterio


def crear_diccionario(definiciones, palabras):

    definicion = abrir_linea(definiciones)
    palabra = abrir_linea(palabras)
    diccionario = {}

    while definicion != CORTE:

        if cumple_criterio(palabra):
            diccionario[palabra] = definicion

        definicion = abrir_linea(definiciones)
        palabra = abrir_linea(palabras)

    return diccionario


def armar_csv(diccionario, archivo_csv):

    diccionario=dict(sorted(diccionario.items(),key=lambda x:x[0]))

    for palabra, definicion in diccionario.items():
        linea_escribir = f"{palabra},{definicion}\n"
        archivo_csv.write(linea_escribir)




def devolver_diccionario():

    definiciones = open("./archivos/definiciones.txt", "r", encoding='utf-8')
    palabras = open("./archivos/palabras.txt", "r", encoding='utf-8')
    archivo_csv = open("./archivos/diccionario.csv", "w", encoding="utf-8")

    diccionario = crear_diccionario(definiciones, palabras)
    armar_csv(diccionario, archivo_csv)
    


    archivo_csv.close()
    definiciones.close()
    palabras.close()

    return diccionario



def hacerlo_lista(diccionario):
    lista=[[k,v] for k,v in diccionario.items()]

    #print(lista)
    return lista

def main():

    diccionario=devolver_diccionario()
    hacerlo_lista(diccionario)

