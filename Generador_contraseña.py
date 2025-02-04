# GENERADOR SEGURO DE CONTRASEÑAS 
import random
import string

# Funcion para generar una contrseña  y la logitud de la misma.
def generate_password(longitud=12):
    # se defina la cadena de caracteres que puede estar en la contraseña
    characters = string.ascii_letters + string.digits + string.punctuation
    # Se genera la contraseña con la longitud deseada utilizando randon.choice para elgir caracteres aleatorios de la cadena anterior.
    contrasena = ''.join(random.choice(characters)for _ in range(longitud))
   