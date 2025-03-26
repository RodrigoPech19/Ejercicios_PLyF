
# Ejercicio 3

asignatura_vii= ["Programacion logica"]
print(asignatura_vii)

asignatura_nueva = asignatura_vii+ ["Programacion Web"]
print(asignatura_nueva)


def agregar_asignatura(lista, asignatura):
    return lista + asignatura

print (agregar_asignatura (asignatura_vii,["Programacion para dispositivos moviles"]))