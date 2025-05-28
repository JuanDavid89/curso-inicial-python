# Funciones - Nos permite modularizar el código

# Funciones nativas de Python
'''
Print()
input()
int()
'''

# Función definida por el usuario
'''
def saludar():
    print("Hola mundo!")

# Invocar la funciónr
saludar() 
'''

'''
def saludar(nombre):
    print(f"Hola {nombre}")

# Invocar la funciónr
saludar(input("Ingrese su nombre: ")) 
'''

'''
def sumar(num1, num2):
    resultado = num1 + num2
    print(f"El resultado de la suma es: {resultado}")

sumar(10, 5)
'''
# Misma función intereactiva (En este caso suma o resta)
# Función con parametros (Lo que se le pasa dentro de los parantesis)
'''
def sumar(num1, num2):
    resultado = num1 + num2
    print(f"El resultado de la suma es: {resultado}")

def restar(num1, num2):
    resultado = num1 - num2
    print(f"El resultado de la resta es: {resultado}")

# Llamando a la función con argumentos (Lo que se pasa para cada parametro)
sumar(int(input("ingrese un número: ")), int(input("Ingrese otro número: ")))
restar(int(input("ingrese un número: ")), int(input("Ingrese otro número: ")))
'''

# Se pasa por parametros el string del mensaje por defecto
'''
def saludar(nombre, mensaje="Hola"):
    print(f"{mensaje}, {nombre}!")

# Como no se pasa algo más por argumento imprime el argumento de mensaje pasado en el parametro
saludar("Ana")
# Sobre escribe el argumento de mensaje
saludar("Luis", "Buenos días")
'''

# Misma función pasando argumentos interactivos
'''
def saludar(nombre, mensaje):
    print(f"{mensaje}, {nombre}!")

# Como no se pasa algo más por argumento imprime el argumento de mensaje pasado en el parametro
saludar(input("Ingresa un nombre: "), input("Ingresa un saludo: "))
'''

# Ejemplo para diferenciar posiciones de parametros y argumentos
'''
def registrar_usuario(nombre, edad, ciudad):
    print(f"Nombre: {nombre}, Edad: {edad}, Ciudad: {ciudad}")

registrar_usuario(edad=30, nombre="Carlos", ciudad="Madrid")
'''

'''
def crear_direccion(calle, numero='S/N', ciudad='Sin especificar', 
codigo_postal='N/A'):
    return f"Dirección: {calle} {numero}, Ciudad: {ciudad}. C.P: {codigo_postal}"

# Llamada con todos los parámetros especificados
print(crear_direccion("Avenida Corrientes", 1234, "Buenos Aires", "1043"))

# Llamada sin especificar el número ni el código postal
print(crear_direccion("Calle florida"))
'''

# Variable fuera de la función   
'''
mensaje = "Hola Juan!"

def saludar():
    mensaje = "¡Hola, mundo!" # mensaje es una variable local
    print(mensaje)
    return mensaje

# Imprime lo que tiene el print de la función
mensaje_de_la_funcion = saludar()
# Imprime lo que tiene la variable fuera de la función
print(mensaje)
# Imprime lo que se guarda en la variable obtenido del return
print(mensaje_de_la_funcion)
'''

def saludar():
    # Declaramos que queremos usar la variable global 'nombre'
    global nombre
    nombre = "María"
    print(f"Hola, {nombre} --> local")

saludar()
print(f"Hola, {nombre} --> global")



