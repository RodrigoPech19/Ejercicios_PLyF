# Lista de jugadores
jugadores = [
    {"nombre":"Alex","edad":20},
    {"nombre":"Rodrigo","edad":21},
    {"nombre":"Armando","edad":24},
    {"nombre":"Adriel","edad":25}
]

jugadores_mayores = list(filter(lambda jugador: jugador["edad"]>23, jugadores))

print(jugadores_mayores)