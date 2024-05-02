# Declarar variables para el préstamo del banco, el monto total de la compra y otras variables
prestamoBanco = 0
montoTotal = int(input("Digite el monto total de la compra:"))

# Calcular la inversión propia y el crédito solicitado al fabricante
if montoTotal > 500000:
    dineroPropio = montoTotal * 0.55  # Calcula el 55% del monto total como inversión propia
    prestamoBanco = montoTotal * 0.30  # Calcula el 30% del monto total como préstamo del banco
    creditoFabricante = (montoTotal * 0.15) + (montoTotal * 0.20)  # Calcula el crédito solicitado al fabricante
else:
    dineroPropio = montoTotal * 0.70  # Calcula el 70% del monto total como inversión propia
    creditoFabricante = (montoTotal * 0.30) + (montoTotal * 0.20)  # Calcula el crédito solicitado al fabricante

# Imprimir los resultados
print("La empresa invirtió:", dineroPropio, "le solicitó prestado al banco:", prestamoBanco, "y el valor del crédito solicitado al fabricante fue de:", creditoFabricante)