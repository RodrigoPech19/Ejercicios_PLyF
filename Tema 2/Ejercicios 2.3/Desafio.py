from functools import reduce

def cuadradosLista(arreglo):
    return list(map(lambda x: x**2, filter(lambda x: isinstance(x, int) and x > 0, arreglo)))

cuadrados_enteros = cuadradosLista([-3, 4.8, 5, 3, -3.2])
print(cuadrados_enteros)
