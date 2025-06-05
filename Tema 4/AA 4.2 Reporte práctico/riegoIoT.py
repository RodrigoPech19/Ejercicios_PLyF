# Estado de sensores como funciones puras
def humedad_suelo() -> str:
    return "baja"

def temperatura() -> int:
    return 35

def hora() -> int:
    return 20

def pronostico_lluvia() -> bool:
    return False

# Regla: ¿Es una hora adecuada para regar?
def hora_adecuada(h: int) -> bool:
    return h < 10 or h > 18

# Regla principal: ¿Cuándo se debe activar el sistema de riego?
def activar_riego(humedad: str, lluvia: bool, hora_val: int) -> bool:
    return humedad == "baja" and not lluvia and hora_adecuada(hora_val)

# Diagnóstico del sistema
def estado_riego() -> str:
    if activar_riego(humedad_suelo(), pronostico_lluvia(), hora()):
        return "Activado"
    else:
        return "No activado"

# Alerta de temperatura extrema
def alerta_calor(temp: int) -> bool:
    return temp >= 32

# Recomendación basada en las condiciones actuales
def recomendacion() -> str:
    if activar_riego(humedad_suelo(), pronostico_lluvia(), hora()) and alerta_calor(temperatura()):
        return "Alerta: Riego activado con temperatura alta. Considere riego nocturno o por goteo."
    else:
        return "Sin recomendaciones especiales para el riego."

# --- Prueba del sistema ---
if __name__ == "__main__":
    print("Estado del sistema de riego:", estado_riego())
    print("Recomendación:", recomendacion())
