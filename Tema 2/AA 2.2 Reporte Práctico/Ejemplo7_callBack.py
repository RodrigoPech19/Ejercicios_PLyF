import time

def tarea(callback):
    print("Iniciando tarea...")
    time.sleep(5)
    callback()

def tarea_completada():
    print("Tarea completada.")

tarea(tarea_completada)