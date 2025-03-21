def elegir_operacion(tipo):
    def suma(x, y):
        return x + y
    def resta(x, y):
        return x - y
    
    if tipo == "suma":
        return suma
    else:
        return resta

operacion = elegir_operacion("suma")
print(operacion(85, 15))