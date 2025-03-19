def preparar_cafe_a():
    return "Cafe americano"

def preparar_cafe_o():
    return "Cafe de olla"

def ordenar_cafe(funcion, num_tazas):
    tazas_cafe =[funcion() for _ in range(num_tazas)]
    return tazas_cafe

cafe_grupo_a = ordenar_cafe(preparar_cafe_a, 10)
cafe_grupo_b = ordenar_cafe(preparar_cafe_o, 12)

print(cafe_grupo_a, cafe_grupo_b)