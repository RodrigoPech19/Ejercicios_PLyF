from functools import reduce

jugadores = [
    {"nombre":"Alex","edad":20},
    {"nombre":"Rodrigo","edad":21},
    {"nombre":"Armando","edad":24},
    {"nombre":"Adriel","edad":25}
]

suma_edades = reduce(lambda acumulador, jugador: acumulador + jugador ["edad"], jugadores, 0)

print(suma_edades)