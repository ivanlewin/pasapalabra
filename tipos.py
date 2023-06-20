from typing import List, Literal, Tuple, TypedDict

jugador = TypedDict('jugador', {'usuario': str, 'turno_de_juego': int})
resultado_jugada = Literal['a', 'e']
jugada = TypedDict('jugada', {'intento': str, 'jugador': jugador, 'palabra': str, 'resultado': resultado_jugada})
rosco = List[Tuple[str, str]]
puntaje = TypedDict('puntaje', {'usuario': str, 'puntaje': int})
turno = TypedDict('turno', {'palabra': str, 'intento': str, 'jugador': jugador})
color = Literal['a', 'e']
estadisticas = TypedDict('estadisticas', {'jugador': jugador, 'aciertos': int, 'errores': int})
