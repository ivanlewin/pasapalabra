import doctest
import random
from typing import List

import tipos
from main import LETRAS_CON_TILDES


def asignar_turnos(usuarios: List[str]) -> List[tipos.jugador]:
    '''
    Esta función recibe los nombres de los usuarios participantes y les asigna un turno de juego aleatoriamente.

    Parámetros
    ----------
    usuarios : List[str]

    Retorna
    -------
    List[tipos.jugador]
        Un listado de jugadores, ordenados de manera aleatoria.
        Cada jugador está representado como un diccionario con las claves 'usuario' (str) y 'turno_de_juego' (int).

    Autores
    -------
    * Lewin, Iván
    '''
    usuarios = [*usuarios]
    random.shuffle(usuarios)
    jugadores = [{'usuario': usuarios[i], 'turno_de_juego': i} for i in range(len(usuarios))]
    return jugadores


def ordenar_en_español(iterable: List[str]) -> List[str]:
    '''
    Ordena un iterable alfabéticamente, teniendo en cuenta los diacríticos del español.
    Esto significa que el elemento 'á' se ubicará luego del elemento 'a', y no luego del elemento 'z'.

    Parámetros
    ----------
    iterable : List[str]
        Idealmente, una lista de strings donde cada elemento tiene longitud 1.

    Retorna
    -------
    List[str]
        Los elementos de la lista ordenados teniendo en cuenta el alfabeto en español.

    Autores
    -------
    * Lewin, Iván

    Ejemplos
    --------
    >>> ordenar_en_español(['c', 'b', 'a'])
    ['a', 'b', 'c']
    >>> ordenar_en_español(['c', 'b', 'á'])
    ['á', 'b', 'c']
    >>> ordenar_en_español(['c', 'ä', 'b', 'á'])
    ['á', 'ä', 'b', 'c']
    >>> ordenar_en_español('dhóiséúa')
    ['a', 'd', 'é', 'h', 'i', 'ó', 's', 'ú']
    '''
    return sorted(iterable, key=lambda i: LETRAS_CON_TILDES.find(i))


def calcular_cantidad_de_palabras_por_letra(diccionario_como_lista: tipos.diccionario_como_lista) -> dict[str, int]:
    '''
    Muestra diccionario con cantidad de palabras por letra que hay en el diccionario filtrado.

    Parámetros
    ----------
    diccionario_como_lista : tipos.diccionario_como_lista
        El diccionario de palabras participantes del juego.
        Lista de tuplas donde cada tupla tiene dos elementos; el primero es la palabra 'aplanada' y el segundo, su definición.

    Retorna
    -------
    dict[str, int]
        Un diccionario con la cantidad de palabras que comienzan por cada letra.
        Las claves del diccionario son cada una de las letras iniciales de las palabras presentes en `diccionario_como_lista`
        y los valores son la cantidad de palabras que comienzan por cada una de esas letras.

    Autores
    -------
    * Galvani, Juan Ignacio
    * Neme, Agustin Nadim

    Ejemplos
    --------
    >>> calcular_cantidad_de_palabras_por_letra([['arbol', '...'], ['barco', '...'], ['caballo', '...']])
    {'a': 1, 'b': 1, 'c': 1}
    >>> calcular_cantidad_de_palabras_por_letra([['arbol', '...'], ['barco', '...'], ['caballo', '...'], ['abeja', '...']])
    {'a': 2, 'b': 1, 'c': 1}
    '''
    cantidad_de_palabras_por_letra = {}

    for palabra, definicion in diccionario_como_lista:
        letra_inicial = palabra[0]
        if letra_inicial in cantidad_de_palabras_por_letra:
            cantidad_de_palabras_por_letra[letra_inicial] = cantidad_de_palabras_por_letra[letra_inicial] + 1
        else:
            cantidad_de_palabras_por_letra[letra_inicial] = 1

    return cantidad_de_palabras_por_letra


def sumar_puntajes(puntajes_de_la_partida: List[tipos.puntaje], puntajes_acumulados: List[tipos.puntaje]):
    '''
    Recibe los puntajes de una partida y los puntajes del juego y agrega los primeros a los últimos.
    No retorna ningún valor. Modifica el listado de puntajes acumulados.

    Parámetros
    ----------
    puntajes_de_la_partida : List[tipos.puntaje]
        Los puntajes de la partida en curso.
    puntajes_acumulados : List[tipos.puntaje]
        Los puntajes acumulados del juego.

    Autores
    -------
    * Lewin, Iván

    Ejemplos
    --------
    >>> puntajes_de_la_partida = [{'usuario': 'Pedro', 'puntaje': 10}]
    >>> puntajes_acumulados = [{'usuario': 'Pedro', 'puntaje': 20}]
    >>> sumar_puntajes(puntajes_de_la_partida, puntajes_acumulados)
    >>> print(puntajes_acumulados)
    [{'usuario': 'Pedro', 'puntaje': 30}]

    >>> puntajes_de_la_partida = [{'usuario': 'María', 'puntaje': 4}, {'usuario': 'Juan', 'puntaje': 10}]
    >>> puntajes_acumulados = [{'usuario': 'María', 'puntaje': -4}, {'usuario': 'Juan', 'puntaje': 10}]
    >>> sumar_puntajes(puntajes_de_la_partida, puntajes_acumulados)
    >>> print(puntajes_acumulados)
    [{'usuario': 'María', 'puntaje': 0}, {'usuario': 'Juan', 'puntaje': 20}]
    '''
    for i in range(len(puntajes_de_la_partida)):
        puntaje_partida = puntajes_de_la_partida[i]['puntaje']
        puntajes_acumulados[i]['puntaje'] = puntajes_acumulados[i]['puntaje'] + puntaje_partida


def calcular_estadisticas(jugadas: List[tipos.jugada], jugadores: List[tipos.jugador]) -> List[tipos.estadisticas]:
    '''
    Calcula la cantidad de aciertos y errores que obtuvo cada jugador en una partida.

    Parámetros
    ----------
    jugadas : List[tipos.jugada]
        Las jugadas de la partida.
    jugadores : List[tipos.jugador]
        Los jugadores que participaron de la partida.

    Retorna
    -------
    List[tipos.estadisticas]
        Un listado ordenado (según el orden de los jugadores) con las estadísticas de cada jugador.

    Autores
    -------
    * Lewin, Iván
    '''
    estadisticas_jugadores: List[tipos.estadisticas] = [{'jugador': jugador, 'aciertos': 0, 'errores': 0} for jugador in jugadores]
    for i in range(len(jugadas)):
        jugada = jugadas[i]
        jugador = jugada['jugador']
        if jugada['resultado'] == 'a':
            estadisticas_jugadores[jugador['turno_de_juego']]['aciertos'] += 1
        else:
            estadisticas_jugadores[jugador['turno_de_juego']]['errores'] += 1

    return estadisticas_jugadores


def calcular_puntaje_de_la_partida(jugadas: List[tipos.jugada], jugadores: List[tipos.jugador], valor_acierto: int, valor_desacierto: int) -> List[tipos.puntaje]:
    '''
    Esta función recibe una lista de jugadas (caracteres 'a' o 'e') y retorna el puntaje obtenido.
    Cada acierto suma 10 puntos y cada error resta 3 puntos.

    Parámetros
    ----------
    jugadas : List[tipos.jugada]
        Las jugadas de la partida.
    jugadores : List[tipos.jugador]
        Los jugadores que participaron de la partida.
    valor_acierto : int
        El valor de puntos a sumar por cada palabra acertada.
    valor_desacierto : int
        El valor de puntos a restar por cada palabra errada. El valor debe estar expresado como un número positivo.

    Retorna
    -------
    tipos.Tipo_puntajes

    Autores
    -------
    * Armari, Valentino
    * Lewin, Iván
    '''
    puntajes: List[tipos.puntaje] = [{'usuario': jugador['usuario'], 'puntaje': 0} for jugador in jugadores]
    estadisticas_jugadores = calcular_estadisticas(jugadas, jugadores)
    for i in range(len(estadisticas_jugadores)):
        aciertos = estadisticas_jugadores[i]['aciertos']
        errores = estadisticas_jugadores[i]['errores']
        jugador = estadisticas_jugadores[i]['jugador']
        puntajes[jugador['turno_de_juego']]['puntaje'] = (aciertos * valor_acierto) + (errores * valor_desacierto * -1)
    return puntajes


def aplanar(texto: str) -> str:
    '''
    Convierte el texto provisto a minúscula y elimina diéresis y tildes de las vocales.

    Parámetros
    ----------
    texto : str
        El texto que se desea aplanar.

    Retorna
    -------  
    str
        El texto aplanado.

    Autores
    -------
    * Galvani, Juan Ignacio
    * Neme, Agustin Nadim

    Ejemplos
    --------
    >>> aplanar('néctar')
    'nectar'
    >>> aplanar('vaivén')
    'vaiven'
    >>> aplanar('yesería')
    'yeseria'
    >>> aplanar('vacilación')
    'vacilacion'
    >>> aplanar('búho')
    'buho'
    >>> aplanar('PERRO')
    'perro'
    >>> aplanar('PiNgüInO')
    'pinguino'
    '''

    return (
        texto
        .lower()
        .replace('á', 'a')
        .replace('é', 'e')
        .replace('í', 'i')
        .replace('ó', 'o')
        .replace('ú', 'u')
        .replace('ä', 'a')
        .replace('ë', 'e')
        .replace('ï', 'i')
        .replace('ö', 'o')
        .replace('ü', 'u')
    )


def verificar_intento(ingreso_usuario: str, palabra_a_adivinar: str) -> tipos.resultado_jugada:
    '''
    Esta función verifica que el ingreso del usuario sea válido dada la palabra a adivinar.

    Parámetros
    ----------
    ingreso_usuario : str
    palabra_a_adivinar : str

    Retorna
    -------
    str
        Retorna la letra 'a' si es un acierto o la letra 'e' en caso contrario.

    Autores
    -------
    * Brizuela, Natanael Daniel
    * Lewin, Iván
    * Neme, Agustin Nadim

    Ejemplos
    --------
    >>> verificar_intento('AlmuÉrzo', 'almuerzo')
    'a'
    >>> verificar_intento('almurso', 'almuerzo')
    'e'
    '''
    acierto = ''
    if aplanar(ingreso_usuario) == palabra_a_adivinar:
        acierto = 'a'
    else:
        acierto = 'e'
    return acierto


if __name__ == '__main__':
    print(doctest.testmod())
