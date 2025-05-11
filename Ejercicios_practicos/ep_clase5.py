# Ejercicio práctico Clase 5

'''
Para este ejercicio necesitamos un software que ayude a registrar y calcular información financiera básica
 para nuestros y nuestras clientes.

Tu tarea para esta semana es la siguiente:

- Registrar los ingresos mensuales de un cliente durante 6 meses. 
- Usá un bucle while para solicitar el ingreso de cada mes. 
- Validar que los ingresos sean números positivos. 
- Si se ingresa un valor negativo, mostrá un mensaje indicando que el valor no es válido y volvé a pedir el dato.

- Calcular el total acumulado durante los 6 meses. Mostrá este resultado al final del programa.

- El programa debe mostrar el apellido, nombre y dirección de correo con el formato pedido, 
y el texto correspondiente a su rango etario.

¡Estoy segura de que harás un excelente trabajo!

Saludos, Mariana
'''
nombre = input("Ingresa tu nombre: ").strip().title()
apellido = input("Ingresa tu apellido: ").strip().title()
edad_input = input("Ingresa tu edad: ").strip()
email = input("Ingresa tu correo electrónico: ").strip().replace(" ", "")



# Validar campos vacíos
if not nombre or not apellido or not email or not edad_input:
    print("ERROR: Ningún campo puede estar vacío.")
# Validar edad
elif not edad_input.isdigit():
    print("ERROR: La edad debe ser un número entero válido.")
# Validar email
elif email.count("@") != 1:
    print("ERROR: El correo electrónico debe contener exactamente un '@' y no tener espacios.")

else:
    edad = int(edad_input)

    # Clasificación por rango etario 
    match edad:
        case edad if edad < 15:
            rango = "Niño/a"
        case edad if 15 <= edad <= 18:
            rango = "Adolescente"
        case _:
            rango = "Adulto/a"
    # Calcular la suma de los ingresos mensuales
    print("\nIngresá tus ingresos mensuales de los últimos 6 meses (sólo números positivos, pueden tener decimales con punto):")

    contador = 1
    suma_ingresos = 0

    while contador <= 6:
        ingreso = input("Ingreso del mes " + str(contador) + ": ").strip()

        # Validar ingreso como número positivo con decimales
        if ingreso.replace(".", "", 1).isdigit():  # permite un solo punto decimal si tiene dos puntos no pasa
            ingreso_num = float(ingreso)
            suma_ingresos = suma_ingresos + ingreso_num
            contador = contador + 1
        else:
            print("Ingresá un número positivo válido (por ejemplo: 4500 o 4500.75)")

    # Mostrar resultados
    print("\n\n================ Registro Financiero ================\n")
    print("Apellido/Nombre:\t\t", apellido + ",", nombre)
    print("Email:\t\t\t\t", email)
    print("Rango Etario:\t\t\t", rango)
    print("Ingresos Mensuales:\t\t\t $", round(suma_ingresos, 2))
    print("\n===================  Fin Registro  ===================\n")

'''ingresos_mensuales = input("Ingresa tu ingreso mensual")'''