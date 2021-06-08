# Elabore programa en Python que imprima la suma de los números enteros de 300 hasta 5000

def imprimir_suma():
    total = 0
    for i in range(300,5001):
        total = total +i
    return total


print("Calculando la suma de los numeros de 300 hasta 5000")
print(imprimir_suma())