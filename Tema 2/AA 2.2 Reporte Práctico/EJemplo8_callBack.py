def terminar_tarea(materia, callback):
    print(f"Tarea de {materia} completada.")
    callback()

def felicitar():
    print("¡Bien hecho!")

terminar_tarea("Programación Lógica y Funcional", felicitar)
