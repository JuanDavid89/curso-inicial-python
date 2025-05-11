# Ejercicio práctico Clase 3

'''
¡Hola!

Necesito que desarrolles un pequeño programa en Python que haga exactamente lo siguiente:

Solicite al cliente o clienta su nombre, apellido, edad y correo electrónico.

Compruebe que el nombre, el apellido y el correo no estén en blanco, y que la edad sea mayor a 18 años.

Muestre los datos por la terminal, en el orden que se ingresaron. Si alguno de los datos ingresados no cumple los requisitos, sólo mostrar el texto “ERROR!”.

Saludos, Mariana”
'''

nombre = input("¿Cuál es tu nombre? ").strip()
apellido = input("¿Cuál es su apellido? ").strip()
edad =  int(input("¿Cuantos años tienes? [Ingresar un valor numérico] "))
email = input("¿Cual es tu correo electrónico? ")

if nombre != "" and apellido != "" and edad >= 18:
    print("\n==============================")
    print("   Tarjeta de Presentación")
    print("==============================")
    print("Nombre:   \t", nombre)
    print("Apellido: \t", apellido)
    print("Edad:     \t", edad)
    print("Email:    \t", email)
    print("==============================\n")
else:
    print("\n==============================")
    print("\t   Resultado")
    print("==============================")
    print("Error!")
    print("==============================\n")
        