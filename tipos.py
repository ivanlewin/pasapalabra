from typing import List, Literal, Tuple, TypedDict

jugador = TypedDict('jugador', {'usuario': str, 'turno_de_juego': int})
resultado_jugada = Literal['a', 'e']
jugada = TypedDict('jugada', {'intento': str, 'jugador': jugador, 'palabra': str, 'resultado': resultado_jugada})
diccionario_como_lista = List[Tuple[str, str]]
puntaje = TypedDict('puntaje', {'usuario': str, 'puntaje': int})
turno = TypedDict('turno', {'palabra': str, 'intento': str, 'jugador': jugador})
color = Literal['a', 'e']
estadisticas = TypedDict('estadisticas', {'jugador': jugador, 'aciertos': int, 'errores': int})
clave_configuracion = TypedDict('clave_configuracion', {'valor': int, 'origen': Literal['Defecto', 'Elección']})
configuracion = TypedDict('configuracion', {
    'LONGITUD_PALABRA_MINIMA': clave_configuracion,
    'CANTIDAD_LETRAS_ROSCO': clave_configuracion,
    'MAXIMO_PARTIDAS': clave_configuracion,
    'PUNTAJE_ACIERTO': clave_configuracion,
    'PUNTAJE_DESACIERTO': clave_configuracion,
})
