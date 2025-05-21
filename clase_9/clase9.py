# Diccionarios 
 
# Para acceder al contenido del diccionario se va a utilizar o pedir la clave para obtener el valor
'''diccionarios = {"clave" : "valor"}
diccionarios.get("Clave")'''

'''frutas = {
    "manzana": 150,
    "banana": 120,
    "naranja": 100,
    "uva": 500,
    "cereza": 800
}

# Para obtner las clave
print(frutas.keys())

#Para obtener un valor por clave
print(frutas.get("banana"))

# Para obtner todos los valores
print(frutas.values())

# Para el contenido por tuplas
print(frutas.items())

#Para modificar el valor por clave
frutas.update({"uva": 130, "cereza": 110})
print(frutas.items())'''

# Registro de clientes con diccionarios y listas

# Creamos una lista vacía para almacenar los diccionarios
clientes = []
# Bucle para ingresar los datos de varios clientes
while True:
   print("\nIngresá los datos del cliente.[vacío para finalizar]:")
   codigo = input("Código del cliente: ")
   
   # Condición para salir del bucle si el código está vacío
   if codigo == "":
      break
   
   nombre = input("Nombre del cliente: ")
   ciudad = input("Ciudad del cliente: ")
   
   # Creamos un diccionario con los datos ingresados
   cliente = {
      "código": codigo,
      "nombre": nombre,
      "ciudad": ciudad
   }

   # Agregamos el diccionario a la lista de clientes
   clientes.append(cliente)

# Mostramos los datos de todos los clientes registrados
print("\n--- Clientes Registrados ---")
for cliente in clientes:
   print(f"Código: {cliente['código']}, Nombre: {cliente['nombre']}, Ciudad: {cliente['ciudad']}")

   # Clase 9