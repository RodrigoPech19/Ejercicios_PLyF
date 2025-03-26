def agregar_asignatura(lista):
    asig_nueva = input("Escribe la asignatura nueva o 'exit' para salir: ")
    if asig_nueva == "exit":
        return lista
    return agregar_asignatura(lista + [asig_nueva]) #Recursion

asignaturas = ["Quimica", "Fisica", "Matematicas"]

nueva_lista = agregar_asignatura(asignaturas)

print(nueva_lista)