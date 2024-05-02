# Declarar variables para el color y el valor de la compra
color = str(input("Digite un color:"))  # Solicita al usuario que ingrese un color (rojo o verde)
compra = float(input("Digite el valor de la compra:"))  # Solicita al usuario que ingrese el valor de la compra

# Evaluar el color y aplicar descuentos según la condición
if color == "rojo":
    descuento = compra * 0.15  # Calcula el 15% del valor de la compra como descuento
    valorPagar = compra - descuento  # Calcula el valor a pagar después del descuento
    print("El valor de la compra fue:", compra, "usted sacó la balota:", color, "con un descuento de:", descuento, "el valor a pagar es:", valorPagar)
elif color == "verde":
    descuento = compra * 0.20  # Calcula el 20% del valor de la compra como descuento
    valorPagar = compra - descuento  # Calcula el valor a pagar después del descuento
    print("El valor de la compra fue:", compra, "usted sacó la balota:", color, "con un descuento de:", descuento, "el valor a pagar es:", valorPagar)
else:
    print("No tienes descuento")  # Si el color no es rojo ni verde, imprime un mensaje indicando que no hay descuento