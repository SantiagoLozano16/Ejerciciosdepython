# Declarar variables para la edad y el sexo
edad = int(input("Por favor, introduce tu edad: "))  # Solicita al usuario que ingrese su edad
sexo = input("Por favor, introduce tu sexo (femenino/masculino): ")  # Solicita al usuario que ingrese su sexo

# Evaluar el sexo y calcular las pulsaciones según la condición
if sexo.lower() == 'femenino':
    pulsaciones = (220 - edad) / 10  # Calcula las pulsaciones para mujeres
elif sexo.lower() == 'masculino':
    pulsaciones = (210 - edad) / 10  # Calcula las pulsaciones para hombres
else:
    print("Por favor, introduce un sexo válido: 'femenino' o 'masculino'.")  # Si el sexo no es válido, muestra un mensaje de error

# Imprimir el resultado
print("El número de pulsaciones que debes tener por cada 10 segundos de ejercicio aeróbico es:", pulsaciones)