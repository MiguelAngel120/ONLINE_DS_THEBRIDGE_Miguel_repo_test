# variables.py

# IDs predeterminados de los jugadores (pueden ser modificados al inicio del juego)
JUGADOR_ID_DEFAULT = 'Jugador_1'
OPONENTE_ID_DEFAULT = 'Oponente_1'

# Dimensiones del tablero
BOARD_SIZE = 10

# Barcos y sus tamaños (longitudes)
BARCOS = {
    'lancha': {'cantidad': 4, 'longitud': 1},      # 4 barcos de 1 casilla
    'submarino': {'cantidad': 3, 'longitud': 2},   # 3 barcos de 2 casillas
    'destructor': {'cantidad': 2, 'longitud': 3},  # 2 barcos de 3 casillas
    'portaviones': {'cantidad': 1, 'longitud': 4}  # 1 barco de 4 casillas
}

# Representaciones en el tablero
EMPTY = 0  # Espacio vacío
SHIP = 1   # Barco
HIT = 2    # Impacto
MISS = 3   # Agua
