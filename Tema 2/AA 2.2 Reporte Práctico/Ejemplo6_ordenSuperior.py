def obtener_estado_servidor(estado):
    def Servidor_activo():
        return "El servidor está en línea y activo"
    
    def servidor_inactvo():
        return "El servidor está fuera de línea"
    
    return Servidor_activo if estado == "activo" else servidor_inactvo

estado_servidor = "inactivo"
mensaje_estado = obtener_estado_servidor(estado_servidor)
print(mensaje_estado())
