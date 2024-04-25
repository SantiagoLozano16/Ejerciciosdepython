#declarar variables
calificacion_de_actividades = 0.3
proyectoF = 0.5
evaluaciones_parciales = 0.2

variable1 =str(input("digite su nombre :"))
variable2 =float(input("digite la nota del promedio de sus actividades :"))
variable3 =float (input("digite el valor de la nota del parcial:"))
variable4 =float(input("digite la nota final del proyecto :"))

#declarar la nota final
notaf=(0.3*variable2)+(0.2*variable3)+(0.5*variable4)

print(f"la nota final del estudiante es {variable1}, es:{notaf}")