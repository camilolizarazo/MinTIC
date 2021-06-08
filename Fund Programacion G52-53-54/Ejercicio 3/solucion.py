# Elabore un programa en Python que lea el código de un artículo, el precio unitario del artículo y la cantidad vendida. 
# Su programa en Python debe calcular e imprimir el total de la venta, el IVA y el total a pagar, sabiendo que el porcentaje del impuesto es dieciséis por ciento.


def calcular_total(precio,cantidad):
    return precio*cantidad

def calcular_iva(venta):
    return venta*0.16


codigo = input("Ingrese codigo del articulo: ")
precio = float(input("Ingrese precio unitario del articulo: "))
cantidad = int(input("Ingrese la cantidad vendida: "))

venta = calcular_total(precio,cantidad)
iva = calcular_iva(venta) 
total = venta + iva

print("El total vendido es: ",venta)
print("El iva total es: ",iva)
print("El total a pagar es: ",total)