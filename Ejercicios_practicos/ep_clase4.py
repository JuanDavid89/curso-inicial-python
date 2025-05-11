# Ejercicio práctico Clase 4

'''
¡Hola!

Estás haciendo un excelente trabajo. Luis me cuenta que estás explorando nuevas estructuras y comandos. 
Pero tengo trabajo para vos, ya que nuestro cliente nos pide que el programa que has desarrollado 
ahora haga lo siguiente:

Formatee correctamente los textos ingresados en “apellido” y “nombre”, 
convirtiendo la primera letra de cada palabra a mayúsculas y el resto en minúsculas.

Asegurarse que el correo electrónico no tenga espacios y contenga solo una “@”.

Que clasifique por rango etario basándose en su edad (“Niño/a” para los menores de 15 años, 
“Adolescente” de 15 a 18 y “Adulto/a” para los mayores de 18 años.)
'''
print("\nIngrese sus datos para crar su tarjeta de presentación")

# Solicitar datos del usuario
nombre = input("¿Cuál es tu nombre? ").strip()
apellido = input("¿Cuál es su apellido? ").strip()
edad =  int(input("¿Cuantos años tienes? [Ingresar un valor numérico] "))
email = input("¿Cual es tu correo electrónico? ").strip()

#Formatear nombre y apellido (Primera letra mayúscula, el resto minúscula)
nombre_formateado = nombre.capitalize()
apellido_formateado = apellido.capitalize()

# Validar email (sin espacios y solo un @)
email_valido = (email.count("@") == 1) and (" " not in email)

# Clasificación por edad
if edad > 0 and edad < 15:
    rango_etario = "Niño/a"
elif edad >=15 and edad < 18:
    rango_etario = "Adolescente"
elif edad > 18:
    rango_etario = "Adulto/a"


if nombre != "" and apellido != "" and email_valido:
    print("\n=================================")
    print("   Tarjeta de Presentación")
    print("=================================")
    print("Nombre:   \t", nombre_formateado)
    print("Apellido: \t", apellido_formateado)
    print("Edad:     \t", edad, f"({rango_etario})")
    print("Email:    \t", email)
    print("=================================\n")
else:
    print("\n==============================")
    print("\t   Resultado")
    print("==============================")
    print("ERROR!")
    print("==============================\n")