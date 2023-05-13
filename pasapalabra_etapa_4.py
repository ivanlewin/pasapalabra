from  pasapalabra_etapa_1  import interaccion_con_usuario
from  pasapalabra_etapa_2 import ordenar_filtrar_diccionario
from  pasapalabra_etapa_3 import obtener_letras_participantes, recibir_lista_diccionario_filtrado


def integracion_de_juego():
    lista_letras2 = obtener_letras_participantes()
    diccionario_filtrado = ordenar_filtrar_diccionario()
    lista_con_definiciones = recibir_lista_diccionario_filtrado(
        diccionario_filtrado, lista_letras2)

    interaccion_con_usuario(lista_con_definiciones)


integracion_de_juego()