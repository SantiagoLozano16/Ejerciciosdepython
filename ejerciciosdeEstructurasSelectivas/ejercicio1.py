# Declarar variables para las notas
nota1 = float(input("Digite su primera nota:"))  # Solicita la primera nota al usuario y la almacena en la variable nota1
nota2 = float(input("Digite su segunda nota:"))  # Solicita la segunda nota al usuario y la almacena en la variable nota2
nota3 = float(input("Digite su tercera nota:"))  # Solicita la tercera nota al usuario y la almacena en la variable nota3

# Calcular el promedio
promedio = (nota1 + nota2 + nota3) / 3  # Calcula el promedio de las tres notas y lo almacena en la variable promedio

# Evaluar el resultado
if promedio >= 70:
    print("Aprobaste el curso")  # Si el promedio es mayor o igual a 70, imprime "Aprobaste el curso"
else:
    print("Desaprobado el curso")  # De lo contrario, imprime "Desaprobado el curso"