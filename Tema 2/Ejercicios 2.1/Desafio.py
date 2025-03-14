print("===============================")
print("Sombrero Seleccionador ISC 🔍 ")
print("===============================")

# Inicializar puntajes para cada rama
redes = 0
bases_datos = 0
desarrollo_software = 0
programacion_hardware = 0
modelado_3d = 0
gestion_proyectos = 0

# Pregunta 1
print("\n1) ¿Qué tipo de problemas disfrutas resolver más?")
print("   1) Configurar dispositivos y conexiones de red")
print("   2) Organizar y estructurar grandes volúmenes de datos")
print("   3) Diseñar aplicaciones y escribir código")
print("   4) Programar microcontroladores y hardware")
print("   5) Crear gráficos y animaciones en 3D")
print("   6) Planificar y coordinar proyectos de software")
respuesta = int(input("Tu respuesta (1-6): "))
if respuesta == 1:
    redes += 2
elif respuesta == 2:
    bases_datos += 2
elif respuesta == 3:
    desarrollo_software += 2
elif respuesta == 4:
    programacion_hardware += 2
elif respuesta == 5:
    modelado_3d += 2
elif respuesta == 6:
    gestion_proyectos += 2

# Pregunta 2
print("\n2) ¿Cuál de estos cursos te interesa más?")
print("   1) Seguridad y administración de redes")
print("   2) Minería de datos y Big Data")
print("   3) Desarrollo web y móvil")
print("   4) Electrónica y arquitectura de computadoras")
print("   5) Animación digital y realidad virtual")
print("   6) Gestión de equipos y metodologías ágiles")
respuesta = int(input("Tu respuesta (1-6): "))
if respuesta == 1:
    redes += 2
elif respuesta == 2:
    bases_datos += 2
elif respuesta == 3:
    desarrollo_software += 2
elif respuesta == 4:
    programacion_hardware += 2
elif respuesta == 5:
    modelado_3d += 2
elif respuesta == 6:
    gestion_proyectos += 2

# Pregunta 3
print("\n3) ¿Qué tipo de herramientas disfrutas usar más?")
print("   1) Routers, switches y herramientas de análisis de redes")
print("   2) SQL, NoSQL y herramientas de administración de bases de datos")
print("   3) Frameworks de desarrollo como React o Django")
print("   4) Microcontroladores, circuitos y Arduino")
print("   5) Software de modelado 3D como Blender o Maya")
print("   6) Herramientas de gestión de proyectos como Jira o Trello")
respuesta = int(input("Tu respuesta (1-6): "))
if respuesta == 1:
    redes += 2
elif respuesta == 2:
    bases_datos += 2
elif respuesta == 3:
    desarrollo_software += 2
elif respuesta == 4:
    programacion_hardware += 2
elif respuesta == 5:
    modelado_3d += 2
elif respuesta == 6:
    gestion_proyectos += 2

# Pregunta 4
print("\n4) ¿En qué tipo de empresa te gustaría trabajar?")
print("   1) Proveedor de servicios de internet o telecomunicaciones")
print("   2) Empresa enfocada en almacenamiento y análisis de datos")
print("   3) Startup de desarrollo de aplicaciones y software")
print("   4) Industria tecnológica que fabrique hardware y dispositivos")
print("   5) Estudio de videojuegos o animación digital")
print("   6) Empresa de consultoría en TI y gestión de proyectos")
respuesta = int(input("Tu respuesta (1-6): "))
if respuesta == 1:
    redes += 2
elif respuesta == 2:
    bases_datos += 2
elif respuesta == 3:
    desarrollo_software += 2
elif respuesta == 4:
    programacion_hardware += 2
elif respuesta == 5:
    modelado_3d += 2
elif respuesta == 6:
    gestion_proyectos += 2

# Pregunta 5
print("\n5) ¿Cuál de estas frases se acerca más a tu forma de pensar?")
print("   1) Mantener las conexiones y la comunicación segura es clave.")
print("   2) La información bien organizada es poder.")
print("   3) Resolver problemas mediante código es mi pasión.")
print("   4) La tecnología comienza en el hardware.")
print("   5) La creatividad y el diseño son esenciales.")
print("   6) Liderar y coordinar equipos es lo mío.")
respuesta = int(input("Tu respuesta (1-6): "))
if respuesta == 1:
    redes += 2
elif respuesta == 2:
    bases_datos += 2
elif respuesta == 3:
    desarrollo_software += 2
elif respuesta == 4:
    programacion_hardware += 2
elif respuesta == 5:
    modelado_3d += 2
elif respuesta == 6:
    gestion_proyectos += 2

# Determinar la rama con mayor puntaje
resultados = {
    "Redes": redes,
    "Bases de Datos": bases_datos,
    "Desarrollo de Software": desarrollo_software,
    "Programación Hardware": programacion_hardware,
    "Modelado 3D": modelado_3d,
    "Gestión de Proyectos": gestion_proyectos
}

rama_recomendada = max(resultados, key=resultados.get)

# Mostrar resultados
print("\n===================================")
print("Resultado: La rama recomendada para ti es:")
print(f" {rama_recomendada} 🔍")
print("===================================")
