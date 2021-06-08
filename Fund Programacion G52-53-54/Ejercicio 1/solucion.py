# Elabore un programa en Python que lea una temperatura en grados Celsius, 
# la convierta a grados Kelvin y muestre el resultado con un mensaje bien explicativo.
# No use aproximaciones


def convertir_temperatura(celsius):
    kelvin = celsius + 273.15
    print("La temperatura ingresada en grados Celsius: ",celsius,"C, convertida a grados Kelvin es: ",kelvin,"K")
    
convertir_temperatura(float(input("Por favor ingrese temperatura en grados Celsius: ")))
