# Gestión de Productos - Pre-Entrega

productos = []

print("\n============================================================")
print("               Gestión de Productos                         ")
print("============================================================")

while True:
    print("\n================ Menú de Opciones ==========================")
    print("1. Agregar producto")
    print("2. Ver productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")
    print("============================================================")

    opcion = input("Seleccione una opción entre 1 y 5: ").strip()

    # Validación: debe ser un número del 1 al 5
    if not opcion.isdigit():
        print("Debe ingresar solo números.")
        continue

    opcion = int(opcion)

    if opcion == 1:
        nombre = input("Ingrese el nombre del producto: ").strip()
        if nombre == "":
            print("El nombre no puede estar vacío.")
            continue

        categoria = input("Ingrese la categoría: ").strip()
        if categoria == "":
            print("La categoría no puede estar vacía.")
            continue

        precio = input("Ingrese el precio (solo números, sin centavos): ").strip()
        if not precio.isdigit():
            print("Debe ingresar un número entero válido.")
            continue

        producto = [nombre, categoria, int(precio)]
        productos.append(producto)
        print("Producto agregado con éxito.")

    elif opcion == 2:
        if len(productos) == 0:
            print("No hay productos registrados.")
        else:
            print("\n==================== Lista de productos ====================")
            contador = 1
            for producto in productos:
                print(f"{contador}. Nombre: {producto[0]} | Categoría: {producto[1]} | Precio: ${producto[2]}")
                contador += 1
            print("============================================================")

    elif opcion == 3:
        buscar = input("Ingrese el nombre del producto a buscar: ").strip().lower()
        encontrados = 0
        for producto in productos:
            if buscar == producto[0].lower():
                print("Producto encontrado:")
                print(f"- Nombre: {producto[0]}")
                print(f"- Categoría: {producto[1]}")
                print(f"- Precio: ${producto[2]}")
                encontrados += 1
        if encontrados == 0:
            print("Producto no encontrado.")

    elif opcion == 4:
        eliminar = input("Ingrese el nombre exacto del producto a eliminar: ").strip().lower()
        eliminado = False
        for producto in productos:
            if eliminar == producto[0].lower():
                productos.remove(producto)
                print("Producto eliminado con éxito.")
                eliminado = True
                break
        if not eliminado:
            print("Producto no encontrado.")

    elif opcion == 5:
        if len(productos) > 0:
            print("\n=================== Productos ingresados ===================")
            contador = 1
            for producto in productos:
                print(f"{contador}. Nombre: {producto[0]} | Categoría: {producto[1]} | Precio: ${producto[2]}")
                contador += 1
            print("============================================================\n")
        else:
            print("No se ingresaron productos.")
            print("============================================================\n")

        print("                   Fin del programa...")
        print("\n============================================================\n")
        break

    else:
        print("Opción fuera de rango (1-5). Intente nuevamente.")

print("============================================================")
print("              Desarrollado por: Juan Saavedra            ")
print("============================================================\n")

