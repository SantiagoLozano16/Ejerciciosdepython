edad_meses = float(input("Por favor, introduce tu edad en meses: "))  # Se solicita al usuario que ingrese su edad en meses y se almacena como un número de punto flotante.

nivel_hemoglobina = float(input("Por favor, introduce tu nivel de hemoglobina en g%: "))  # Se solicita al usuario que ingrese su nivel de hemoglobina en g% y se almacena como un número de punto flotante.

sexo = input("Por favor, introduce tu sexo (femenino/masculino): ")  # Se solicita al usuario que ingrese su sexo (femenino/masculino) y se almacena como una cadena de texto.

if edad_meses <= 1:  # Se verifica si la edad en meses es menor o igual a 1.
    rango = (13, 26)  # Si la condición es verdadera, se asigna el rango de hemoglobina correspondiente.
elif edad_meses <= 6:  # Se verifica si la edad en meses es menor o igual a 6.
    rango = (10, 18)  # Si la condición es verdadera, se asigna el rango de hemoglobina correspondiente.
elif edad_meses <= 12:  # Se verifica si la edad en meses es menor o igual a 12.
    rango = (11, 15)  # Si la condición es verdadera, se asigna el rango de hemoglobina correspondiente.
elif edad_meses <= 60:  # Se verifica si la edad en meses es menor o igual a 60.
    rango = (11.5, 15)  # Si la condición es verdadera, se asigna el rango de hemoglobina correspondiente.
elif edad_meses <= 120:  # Se verifica si la edad en meses es menor o igual a 120.
    rango = (12.6, 15.5)  # Si la condición es verdadera, se asigna el rango de hemoglobina correspondiente.
elif edad_meses <= 180:  # Se verifica si la edad en meses es menor o igual a 180.
    rango = (13, 15.5)  # Si la condición es verdadera, se asigna el rango de hemoglobina correspondiente.
elif sexo.lower() == 'femenino':  # Se verifica si el sexo ingresado es femenino.
    rango = (12, 16)  # Si la condición es verdadera, se asigna el rango de hemoglobina correspondiente.
elif sexo.lower() == 'masculino':  # Se verifica si el sexo ingresado es masculino.
    rango = (14, 18)  # Si la condición es verdadera, se asigna el rango de hemoglobina correspondiente.
else:  # Si ninguna de las condiciones anteriores se cumple.
    print("Por favor, introduce un sexo válido: 'femenino' o 'masculino'.")  # Se imprime un mensaje solicitando al usuario ingresar un sexo válido.

if nivel_hemoglobina < rango[0]:  # Se compara el nivel de hemoglobina ingresado con el límite inferior del rango correspondiente.
    print("Positivo para anemia")  # Si el nivel de hemoglobina es menor que el límite inferior del rango, se imprime que es positivo para anemia.
else:  # Si el nivel de hemoglobina es mayor o igual al límite inferior del rango.
    print("Negativo para anemia")  # Se imprime que es negativo para anemia.