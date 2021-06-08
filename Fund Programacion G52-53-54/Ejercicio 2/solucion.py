def imprimir_numero(numero):
    if len(numero)!=3 :
        print("El numero no tiene 3 digitos.")
    else:
        for i in range(3):
            print(numero[i])
    

imprimir_numero(input("Ingrese un numero de 3 digitos: "))
