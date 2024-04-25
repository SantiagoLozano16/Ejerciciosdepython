sueldo=2500000
tcomisiones= 0
comisiones= 600
ventas =0
total =0

nombre =str(input("digite su nombre de vendedor :"))
ventas =int(input("Digite cantidad de ventas"))

tcomisiones = ventas*comisiones
total  = tcomisiones+sueldo 

print(f"el vendedor {nombre}, tiene un sueldo de {sueldo}, durante el mes obtuvo una comision de {tcomisiones}")