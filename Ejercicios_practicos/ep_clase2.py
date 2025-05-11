# Ejercicio práctico Clase 2

'''
¡Hola!

En nuestro día a día, interactuamos con muchos clientes, y uno de los pasos iniciales es recopilar y organizar su información básica. 
Para eso, necesito que desarrolles un pequeño programa en Python que haga lo siguiente:

1. Solicite al cliente su nombre, apellido, edad y correo electrónico.

2. Almacene estos datos en variables.

3. Los muestre organizados en forma de una tarjeta de presentación en la pantalla.

¡Espero ver el resultado de tu trabajo pronto!

Saludos, Mariana”
'''

nombre = input("¿Cuál es tu nombre? ")
apellido = input("¿Cuál es su apellido? ")
edad =  int(input("¿Cuantos años tienes? [Ingresar un valor numérico] "))
email = input("¿Cual es tu correo electrónico? ")

print("\n==============================")
print("   Tarjeta de Presentación")
print("==============================")
print("Nombre:   \t", nombre)
print("Apellido: \t", apellido)
print("Edad:     \t", edad)
print("Email:    \t", email)
print("==============================\n")