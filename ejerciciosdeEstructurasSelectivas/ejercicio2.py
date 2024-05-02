# Declarar variables para la cantidad y el precio de la compra
cantidad = int(input("Digite la cantidad de la compra:"))  # Solicita la cantidad de productos al usuario
precio = int(input("Digite el valor de la compra:"))  # Solicita el precio unitario al usuario

# Calcular el descuento
if cantidad >= 3:
    descuento = 0.2  # Si la cantidad es mayor o igual a 3, se aplica un descuento del 20%
else:
    descuento = 0.1  # De lo contrario, se aplica un descuento del 10%

# Calcular el valor con descuento
valor = descuento * precio  # Calcula el valor del descuento
valor_con_descuento = precio - valor  # Calcula el valor total con descuento

# Imprimir el resultado
print("El valor a pagar:", valor_con_descuento)  # Imprime el valor total con descuento