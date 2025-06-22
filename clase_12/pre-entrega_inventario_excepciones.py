print("\n==== Gestión del Inventario ====")

productos = []

# Cargar inventario desde archivo
try:
    archivo = open("inventario.txt", "a+", encoding="utf-8")
    archivo.seek(0)
    for linea in archivo:
        linea_limpia = linea.strip()
        if linea_limpia:
            datos = linea_limpia.split('|')
            if len(datos) == 3:
                productos.append(datos)
    archivo.close()
except Exception as e:
    print(f"Error al cargar el archivo: {e}. Se iniciará con una lista vacía.")

while True:    
    print("\n==============")
    print("Menu:")
    print("==============")
    print("1. Agregar")
    print("2. Eliminar")
    print("3. Buscar")
    print("4. Mostrar")
    print("==============")
    print("5. Salir")
   
    opcion = input(f"\nIngresa el número de la opción deseada: \n").strip()

# ===================== | 1 | ==================================
       
    if opcion == "1":
        print("\nAgregar Nuevo Producto:\n")
       
        nombre = input("\tNombre: ").strip().capitalize()
        categoria = input("\tCategoría: ").strip().capitalize()
        precio = input("\tPrecio: ").strip()
       
        if not precio.isdigit() or int(precio) <= 0:
            print("El precio debe ser un entero positivo.")
            continue
       
        precio_ingresado = int(precio)
        productos.append([nombre, categoria, str(precio_ingresado)])
        
        # Guardar en archivo
        try:
            archivo = open("inventario.txt", "a", encoding="utf-8")
            archivo.write(f"{nombre}|{categoria}|{precio_ingresado}\n")        
            archivo.close()
            print(f"\n'{nombre}' se agregó al inventario.\n")
        except Exception as e:
            print(f"\nError al guardar el producto: {e}\n")
           
        continue

# ===================== | 2 | ==================================

    elif opcion == "2":
        print("Eliminar Producto")
       
        if len(productos) <= 0:
            print("\nNo hay productos cargados en el inventario.\n")
            continue
       
        for i in range(len(productos)):
            print(f"- {i + 1} {productos[i][0]}")

        producto_a_eliminar = input("Número del producto a eliminar: ").strip()
       
        if not producto_a_eliminar.isdigit():
            print("Ingrese un número válido")
            continue
       
        producto_a_eliminar = int(producto_a_eliminar)
       
        if producto_a_eliminar < 1 or producto_a_eliminar > len(productos):
            print("Número del producto inexistente. Rentente.")
            continue
       
        eliminado = productos.pop(producto_a_eliminar - 1)
        print(f"Producto '{eliminado[0]}' eliminado.")
        
        # Reescribir todo el archivo
        try:
            archivo = open("inventario.txt", "w", encoding="utf-8")
            for producto in productos:
                archivo.write(f"{producto[0]}|{producto[1]}|{producto[2]}\n")
            archivo.close()
        except Exception as e:
            print(f"Error al actualizar el archivo: {e}")

# ===================== | 3 | ==================================
               
    elif opcion == "3":
        print("Buscar Productos")
       
        buscar = input(f"Ingrese el nombre del producto a buscar: ").strip()
       
        busqueda = []
        for listado_productos in productos:
            if buscar.lower() in listado_productos[0].lower():
                busqueda.append(listado_productos)
       
        print("\nResultados de la Búsqueda:\n")
       
        if busqueda:
            for i in range(len(busqueda)):
                prod = busqueda[i]
                print(f"\t{i + 1}. {prod[0]} | Categoría: {prod[1]} | Precio: {prod[2]}")
        else:
            print("No se encontraron productos.")

# ===================== | 4 | ==================================
   
    elif opcion == "4":
        print("\nProductos en inventario:")
        if len(productos) <= 0:
            print("No hay productos en el inventario.")
        else:
            for i in range(len(productos)):
                producto = productos[i]
                print(f"\t{i + 1}. {producto[0]} | Categoría: {producto[1]} | Precio: {producto[2]}")

# ===================== | 5 | ==================================
               
    elif opcion == "5":
        print("\nPrograma finalizado.\n")
        break

    else:
        print("Ingrese un número válido." )