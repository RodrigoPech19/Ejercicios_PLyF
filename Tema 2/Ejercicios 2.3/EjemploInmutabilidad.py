#ejemplo 1 inmutabilidad, funcion pura y sin efectos secundarios
variable_global = 10 #variable global

def aumentar_variable ():
    return variable_global + 1 #no se modifica la varaible global, se retorna un nuevo valor

print(aumentar_variable())

#ejemplo 2
def contar_palabras(texto):
    return len(texto.split()) #separa el texto en palabras y cuenta la cantidad

oracion = "El tema de hoy es la inmutabilidad en Python"
print(contar_palabras(oracion))

#ejemplo 3 uso incorrecto de la funcion pura
contador_global = 0 #variable global

def contar_palabras_no_funcional(texto):
    global contador_global #se accede a la variable global
    contador_global = len(texto.split()) #se reasigna la variable global
    
#uso
texto_ejemplo = "Este es un ejemplo"
contar_palabras_no_funcional(texto_ejemplo)
print(contador_global)

#mutable
contar_palabras_no_funcional("Otro texto de ejemplo")
print(contador_global) #Ahora imprime: 4(pero cambio la variable)