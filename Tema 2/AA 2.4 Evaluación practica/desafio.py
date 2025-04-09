import tkinter as tk
from tkinter import messagebox
from functools import reduce

# Lista de aspectos a evaluar
aspectos_de_evaluacion = ["Actividades de Aprendizaje", "Claridad de la Explicación", "Disponibilidad del profesor", "Relación teoría-práctica"]
materias_evaluadas = {}

# Función para calcular el promedio de las calificaciones
def calcular_promedio(calificaciones):
    valores = list(calificaciones.values())
    return reduce(lambda x, y: x + y, valores) / len(valores)

# Función para filtrar las calificaciones que son aceptables (>= 6)
def filtrar_calificaciones_aceptables(calificaciones):
    return dict(filter(lambda item: item[1] >= 6, calificaciones.items()))

# Función recursiva para crear las entradas de calificación para cada aspecto de la evaluación
def crear_entradas_de_calificacion(aspectos, i=0):
    if i < len(aspectos):
        aspecto = aspectos[i]
        frame = tk.Frame(ventana_principal)
        frame.pack(pady=2)
        tk.Label(frame, text=aspecto + ": ", width=25, anchor='w').pack(side=tk.LEFT)
        entrada = tk.Entry(frame, width=5)
        entrada.pack(side=tk.LEFT)
        entradas_calificacion[aspecto] = entrada
        crear_entradas_de_calificacion(aspectos, i + 1)

# Función recursiva para limpiar las entradas de calificación después de guardar la evaluación
def limpiar_entradas_de_calificacion(entradas, i=0):
    if i < len(entradas):
        entradas[i].delete(0, tk.END)
        limpiar_entradas_de_calificacion(entradas, i + 1)

# Acción al presionar "Guardar Evaluación"
def guardar_evaluacion():
    nombre_materia = entrada_nombre_materia.get()
    if not nombre_materia:
        messagebox.showwarning("Campo vacío", "Por favor, ingrese el nombre de la materia.")
        return

    calificaciones = {}
    try:
        for aspecto, entrada in entradas_calificacion.items():
            calificacion = int(entrada.get())
            if not (1 <= calificacion <= 10):
                raise ValueError
            calificaciones[aspecto] = calificacion
    except ValueError:
        messagebox.showerror("Error", "Todas las calificaciones deben ser números entre 1 y 10.")
        return

    promedio_materia = calcular_promedio(calificaciones)
    aspectos_aceptables = filtrar_calificaciones_aceptables(calificaciones)

    materias_evaluadas[nombre_materia] = {
        "Promedio": promedio_materia,
        "Aspectos con calificación aceptable": aspectos_aceptables
    }

    messagebox.showinfo("Éxito", f"Evaluación guardada para '{nombre_materia}'.")
    entrada_nombre_materia.delete(0, tk.END)
    limpiar_entradas_de_calificacion(list(entradas_calificacion.values()))

# Función para mostrar todos los resultados guardados
def mostrar_resultados():
    if not materias_evaluadas:
        messagebox.showinfo("Sin datos", "No hay materias evaluadas.")
        return

    resultado = ""
    for materia, datos in materias_evaluadas.items():
        resultado += f"\nMateria: {materia}\n"
        resultado += f"Promedio: {datos['Promedio']:.2f}\n"
        resultado += "Aspectos aceptables:\n"
        for aspecto, cal in datos["Aspectos con calificación aceptable"].items():
            resultado += f"  - {aspecto}: {cal}\n"
        resultado += "-"*30 + "\n"

    messagebox.showinfo("Resultados de Evaluación", resultado)

# Interfaz principal
ventana_principal = tk.Tk()
ventana_principal.title("Evaluación de Materias")
ventana_principal.geometry("400x400")

# Entrada para el nombre de la materia
tk.Label(ventana_principal, text="Nombre de la materia:").pack()
entrada_nombre_materia = tk.Entry(ventana_principal, width=30)
entrada_nombre_materia.pack(pady=5)

# Entradas para calificación de aspectos (usando recursividad)
entradas_calificacion = {}
tk.Label(ventana_principal, text="Calificaciones (1-10):").pack()
crear_entradas_de_calificacion(aspectos_de_evaluacion)

# Botones
tk.Button(ventana_principal, text="Guardar Evaluación", command=guardar_evaluacion).pack(pady=10)
tk.Button(ventana_principal, text="Mostrar Resultados", command=mostrar_resultados).pack(pady=5)
tk.Button(ventana_principal, text="Salir", command=ventana_principal.quit).pack(pady=5)

ventana_principal.mainloop()