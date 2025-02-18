# GENERADOR SEGURO DE CONTRASEÑAS 
import random
import string

print('\n')
print('***GENERADOR SEGURO DE CONTRASEÑAS***')
print('\n')

# Función para generar una contrseña  y la logitud de la misma.
def generate_contrasena_opcion(clase):
    #Si el usuario escoge la opción 1 generará su propia contraseña:
    if clase == 1:
        return input("Genera tu propia contrasena: ")
    #Si el usuario escoge la opción 2 generará automáticamente una contraseña fácil de decir de 12 caracteres:
    elif clase == 2:
        return generar_contrasena_aleatoria(facil_de_decir=True)
    #Si el usuario escoge la opción 3 generará automáticamente una contraseña facil de leer de 12 caracteres:
    elif clase == 3:
        return generar_contrasena_aleatoria(facil_de_leer=False)
    #Si el usuario escoge la opción 4 generará automáticamente una contraseña con una longitud de 12 caracteres especiales:
    elif clase == 4:
        return generar_contrasena_aleatoria()
   
def  generar_contrasena_aleatoria(facil_de_decir=False, facil_de_leer=False):
# esta función genera una contraseña aleatoria: facil_de_decir si es True, genera una contraseña facil de decir decir facil_de_leer: si es True, genera una contraseña facil de leer
    if facil_de_decir:
        #Si es el parametro facil_de_decir es True, define una lista de palabras faciles de pronunciar.
        palabras_faciles = [
            'azul', 'fuego','pato','gato','sol', 
            'luz', 'casa', 'lago','cisne', 'negro',
            'ciencia', 'nuevo', 'canto', 'maestro', 'hola',
            'adios','amiga', 'perro', 'computadora', 'telefono',
            'llave', 'papelera', 'cuaderno', 'cuadro', 'dibujo',
            'estado', 'papel', 'libro', 'mono'
        ]
        return ''.join(random.choice(palabras_faciles) for _ in range(3))
        #devuelve una cadena compuesta por 3 palabras seleccionadas aleatoriamente
        #de la lista de palabras_faciles concatenadas sin espacios entre ellas. 
    elif facil_de_leer:
        caracteres = string.ascii_letters + string.digits 
        #si facil de leer es True se utiliza letras y números para generar la contraseña. 
    else:
        caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(12))
    # si facil_decir y facil_leer son falsos, se utilizan letras números y caractéres especiales para generar la contraseña
    # Genera contraseña con 12 caracteres al azar del conjunto de caracteres especificado anteriormente
    
def mostrar_menu_generar_contrasena():
    #Función que muestra el manú principal del Generador de Contraseñas
    print('\n')
    print("*SELECCIONE UNA OPCIÓN: *")
    print('1. Yo genero mi propia contraseña: ')
     # Si es la opcion 1 el usuario genera si propia contraseña
    print('2. Generar una contraseña automática fácil de decir:')
    #si es la opción 2 se genera contraseña facil de decir 
    print('3. Generar una contraseña automática fácil de leer:')
    #si es la opción 3 genera contraseña facil de leer
    print('4. Generar una contraseña aleatoria de de todos los caracteres de longitud 12 digitos:')
    # Si es la opción 4 genera contraseña con todos los caracteres
    print('\n')


def reglas_generador_contrasena():
    #Función de reglas para las contraseñas
    print('\n')
    print("***REGLAS DEL GENERADOR DE CONTRASEÑAS SEGURAS***")
    print('\n')
    print("1. La contraseña debe tener al menos 12 caracteres de longitud.")
     #imprime la primera regla: debe tener al menos 12 caracteres
    print("2. Debe incluir letras mayúsculas y minúsculas.")
     #imprime la segunda regla: debe incluir letras mayúsculas y minúsculas
    print("3. La contraseña no debe incluir números.")
    #imprime la tercera regla: debe incluir números
    print("4. La contraseña no debe incluir caracteres especiales (?¡#/*, etc.).")
    #imprime la cuarta regla: debe incluir caracteres especiales)
    print('\n')
def menu_principal():
    #Función del menú principal
    while True: #Bucle infinito hasta que el usuario decida salir  
        print("SELECCIONE UNA OPCIÓN:")#Muestra el menú principal
        print("1. Generar una contraseña.")
        print("2. Reglas del generador de contraseñas.")
        print("3. Salir.")  
        print('\n')
        opcion = int(input("Opción: "))
          # Solicita al usuario que ingrese una opción

        if opcion == 1: # si la opci+on es 1 muestra el menú de generación de contraseña
            mostrar_menu_generar_contrasena()
            sub_opción= int(input("Opción: "))
            #Solicita al usuario que ingrese una sub-opción para generar la contraseña
            contrasena = generate_contrasena_opcion(sub_opción)
             #Muestra la contraseña generada al usuario
            print('\n')
            print(f"SU CONTRASEÑA ES : {contrasena}")
        elif opcion == 2: #si la opción es 2 muestra las reglas del generador de contraseñas
            reglas_generador_contrasena()
        elif opcion == 3: #Si la opción es 3 sale del bucle y termina el programa
            print("***¡Hasta Luego!***")
            break
        else:
            print("Opción incorrecta. Intente de nuevo.")

menu_principal()
