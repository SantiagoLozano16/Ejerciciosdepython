# Declarar variable para la cantidad de llantas compradas
llanta = int(input("Llantas compradas: "))  # Solicita al usuario que ingrese la cantidad de llantas compradas

# Evaluar la cantidad de llantas y calcular el valor total a pagar según la condición
if llanta < 5:
    llanta = llanta * 300  # Si la cantidad es menor a 5, calcula el valor total a pagar con un precio unitario de 300
    print(f"El valor total a pagar es de: {llanta}")
elif llanta >= 5 and llanta <= 10:
    llanta = llanta * 250  # Si la cantidad está entre 5 y 10 (inclusive), calcula el valor total a pagar con un precio unitario de 250
    print(f"El valor total a pagar es de: {llanta}")
elif llanta > 10:
    llanta = llanta * 200  # Si la cantidad es mayor a 10, calcula el valor total a pagar con un precio unitario de 200
    print(f"El valor total a pagar es de: {llanta}")