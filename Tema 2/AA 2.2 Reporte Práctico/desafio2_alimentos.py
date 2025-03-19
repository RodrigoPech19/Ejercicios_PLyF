def preparar_pizza():
    return "🍕"

def preparar_hamburguesa():
    return "🍔"

def preparar_hotdog():
    return "🌭"

def bonus(num_porciones):
    if(num_porciones>2):
        return"coca gratis"
    else:
        return""

def ordenar_alimento(funcion, num_porciones):
    porciones_alimentos =[funcion() for _ in range(num_porciones)]
    alimentos = bonus(num_porciones)
    return porciones_alimentos, alimentos

orden_pizzas = ordenar_alimento(preparar_pizza, 8)
orden_hamburguesas = ordenar_alimento(preparar_hamburguesa, 10)
orden_hotdog = ordenar_alimento(preparar_hotdog, 12)

print(orden_pizzas, orden_hamburguesas, orden_hotdog)