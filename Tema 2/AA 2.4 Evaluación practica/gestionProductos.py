productos = [
    "Frijoles Refritos",
    "Coca Cola",
    "Zumo de Naranja",
    "Cafe de Olla",
    "Gorditas de Chicharron",
    "Huevos Motuleños"
]

#Ordena los productos alfabeticamente
productos_ordenados = sorted(productos)

#Convierte la lista ordenada a cadena de nombres
cadena_nombres = ', '.join(productos_ordenados)

#Convierte cada nombre en un slug de URL
slugs = list(map(lambda x: x.lower().replace(' ', '-'), productos_ordenados))

#imprime resultados
print("Lista de slugs: ", slugs)
print("Cadena de nombres ordenados: ", cadena_nombres)

