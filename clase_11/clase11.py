# Scope o alcance

'''
mensaje = "Hola"
print(id(mensaje))

def saludar():
    global mensaje
    mensaje = "Hola Mundo" # Varibale global
    print(id(mensaje))

print(saludar())
print(mensaje)
'''

'''
numero = 5550
print(id(numero))

def operacion():
    global numero
    numero = 55 # Varibale global
    print(id(numero))

print(operacion())
print(numero)
'''

# En los otros archivos de la clase 11 se estara viendo Modulos