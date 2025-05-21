# Ejercicio práctico clase 8

'''
¡Hola!

En TalentoLab nos han pedido desarrollar una aplicación que registre productos y sus precios utilizando diccionarios. Necesitamos que tu programa cumpla con estas instrucciones:

Crear un diccionario llamado productos donde las claves sean los nombres de los productos y los valores sean sus precios. 

Permitir que se agreguen productos y sus precios hasta que se decida finalizar. 

Mostrar el contenido del diccionario después de cada operación.
'''

productos = []
# Bucle para ingresar los datos de varios Productos
while True:
   print("\nIngresá los datos del producto.[vacío para finalizar]:")
   codigo = input("Código del producto: ")
   
   # Condición para salir del bucle si el código está vacío
   if codigo == "":
      break
   
   nombre = input("Nombre del producto: ")
   precio = input("Precio del producto: ")
   
   # Creamos un diccionario con los datos ingresados
   producto = {
      "código": codigo,
      "nombre": nombre,
      "valor": precio
   }

   # Agregamos el diccionario a la lista de clientes
   productos.append(producto)

# Mostramos los datos de todos los clientes registrados
print("\n--- Clientes Registrados ---")
for i in productos:
   print(f"Código: {i['código']}, Nombre: {i['nombre']}, Precio: {i['valor']}")