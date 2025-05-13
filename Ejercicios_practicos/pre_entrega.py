# Consigna ejercicio Pre-Entrega

productos = []

print("\n==================================================")
print(" Lista de Productos | Escriba 'fin' para terminar.")
print("==================================================")

while True:
    nombre_producto = input("Ingrese el nombre de un producto: ")

    if nombre_producto.lower() == 'fin':
        break

    productos.append(nombre_producto)
print("==================================================\n")

print("==================================================")
print(" Listado de productos:")
print("==================================================")
for producto in productos:
    print(f"- {producto}")

print("==================================================\n")