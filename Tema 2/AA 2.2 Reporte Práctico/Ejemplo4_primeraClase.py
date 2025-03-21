def crear_saludo(nombre):
    def saludo():
        return f"¡Hola, {nombre}!"
    return saludo

saludo_personalizado = crear_saludo("Rodrigo")
print(saludo_personalizado()) 