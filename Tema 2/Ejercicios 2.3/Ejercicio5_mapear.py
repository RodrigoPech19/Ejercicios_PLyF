#Ejemplo:
# Lista de jugadores
jugadores = [
    {"nombre":"Alex","edad":20},
    {"nombre":"Rodrigo","edad":21},
    {"nombre":"Armando","edad":23},
    {"nombre":"Adriel","edad":23}
]
#Usar map
nombres_jugadores = list(map(lambda jugador: jugador["nombre"], jugadores))
print(nombres_jugadores)