def main():

    estudiantes = {
        "Adriel": [85, 92, 78],
        "Lenier": [90, 88, 91],
        "Rodrigo": [85, 75, 80],
        "Andres": [95, 100, 98]
    }

    buscar_calificaciones = lambda nombre: estudiantes.get(nombre, "Estudiante no encontrado.")

    while True:
        entrada = input("Ingresa el nombre del estudiante (o 'fin' para terminar): ")
        if entrada.lower() == 'fin':
            break

        calificaciones = buscar_calificaciones(entrada)
        if isinstance(calificaciones, list):
            print(f"Calificaciones de {entrada}: {calificaciones}")
        else:
            print(calificaciones)

if __name__ == "__main__":
    main()