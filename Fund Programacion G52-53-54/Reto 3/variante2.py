#NO ELIMINAR LA SIGUIENTE IMPORTACIÓN, sirve para probar tu código en consola
#from pruebas import pruebas_codigo_estudiante

#NOTA: PARA ESTE RETO PUEDES PROBAR TU PROGRAMA, DANDO CLICK EN LA NAVE ESPACIAL
#LA CONSOLA TE DARÁ INSTRUCCIONES SI PUEDES EVALUAR O NO TU CÓDIGO

#En este espacio podrás programar las funciones que deseas usar en la función solución (NO ES OBLIGATORIO CREAR OTRAS FUNCIONES)
"""Inicio espacio para programar funciones propias"""

def traducir_letras(letra):
    if letra == ".-":
        return "A"
    elif letra == "-...":
        return "B"
    elif letra == "-.-.":
        return "C"
    elif letra == "-..":
        return "D"
    elif letra == ".":
        return "E"    
    elif letra == "..-.":
        return "F"
    elif letra == "--.":
        return "G"
    elif letra == "....":
        return "H"
    elif letra == "..":
        return "I"
    elif letra == ".---":
        return "J"
    elif letra == "-.-":
        return "K"
    elif letra == ".-..":
        return "L"
    elif letra == "--":
        return "M"
    elif letra == "-.":
        return "N"
    elif letra == "---":
        return "O"
    elif letra == ".--.":
        return "P"
    elif letra == "--.-":
        return "Q"
    elif letra == ".-.":
        return "R"
    elif letra == "...":
        return "S"
    elif letra == "-":
        return "T"
    elif letra == "..-":
        return "U"
    elif letra == "...-":
        return "V"
    elif letra == ".--":
        return "W"
    elif letra == "-..-":
        return "X"
    elif letra == "-.--":
        return "Y"
    elif letra == "--..":
        return "Z"


def traducir_palabras(palabra):
    letras_traducidas = ""
    letras_mensaje = palabra.split(" ")
    for i in range(len(letras_mensaje)):
        letras_traducidas += str(traducir_letras(str(letras_mensaje[i])))
    palabra_traducida = letras_traducidas
    return palabra_traducida


#PUEDES PROGRAMAR CUANTAS FUNCIONES DESEES 


"""Fin espacio para programar funciones propias"""

def traductor_a_espanol(mensaje_a_traducir):
    palabras_traducidas = ""
    palabras_mensaje = mensaje_a_traducir.split(" / ")
    for i in range(len(palabras_mensaje)):
        palabras_traducidas += traducir_palabras(palabras_mensaje[i])+" "
    mensaje_traducido = palabras_traducidas
    return mensaje_traducido

"""
Esta línea de código que sigue, permite probar si su ejercicio es correcto
"""
#NO ELIMINAR LA SIGUIENTE LÍNEA DE CÓDIGO


#pruebas_codigo_estudiante(traductor_a_espanol)
print(traductor_a_espanol('-. --- ... / .... .- -. / .--. .. -.-. .- -.. --- / -.. --- ... / -- --- ... --.- ..- .. - --- ...'))