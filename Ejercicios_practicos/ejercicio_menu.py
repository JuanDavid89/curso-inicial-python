# Consigna ejercicio Pre-Entrega

productos = []

print("\n==================================================")
print("               Gestión de Productos               ")
print("==================================================")

while True:
    print("==================================================")
    print("Opciones:")
    print("==================================================")
    print("1. Presione '1' para agregar nombre")
    print("2. Presione '2' para eliminar nombre")
    print("==================================================")
    print("3. Presione '3' paras Salir")
    print("==================================================")

    opcion_str = input(f"\nIngresa el número de la opción deseada: ")

    if not opcion_str.isdigit():
        print("\nDebe ingresar solo caracteres numéricos.")
        continue

    try:
        opcion = int(opcion_str)

        if opcion <= 0 or opcion > 3:
            print("Número invalido, vuelva a intentarlo.")
            continue
       
        elif opcion == 1:
            nombre_producto = input("Ingrese el nombre de un producto: ")
            print(f"Producto ingresado: {nombre_producto}\n")
            productos.append(nombre_producto)
            continue

        elif opcion == 2:
            nombre_producto = input("Ingrese el nombre del producto a eliminar: ")
            if nombre_producto in productos:
                productos.remove(nombre_producto)
                print(f"'{nombre_producto}' eliminado correctamente.")
            else:
                print(f"'{nombre_producto}' no se encuentra en la lista.")
            continue

        elif opcion == 3:
            print("Ingreso Finalizado")
            break  

    except ValueError:
        print("\nOcurrió un error. Intente nuevamente.")
        continue

print("\n==================================================")

print("==================================================")
print(" Listado de productos:")
print("==================================================")
for producto in productos:
    print(f"- {producto}")

print("==================================================\n")