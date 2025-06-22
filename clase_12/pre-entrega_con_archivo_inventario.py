print("\n==== Gestión del Inventario ====")

productos = []

archivo = open("inventario.txt", "a+", encoding="utf-8") # Crea el archivo "inventario.txt" si no existe en el directorio. Permite escritura al final del último registro, si no existen registros escribe en la línea 1. Si lo abriesemos con "r" no crearía el archivo inventario en caso que no exista y arrojaría error crítico FileNotFoundError.
archivo.seek(0) # Posiciona el cursor en la posición 0 (cero) al inicio de la primera línea del archivo "inventario.txt", si no existe y lo crea, se ubica en ese lugar pero no carga nada en RAM porque no hay datos.
for linea in archivo: # Recorre cada línea del archivo, en cada vuelta, línea contiene una cadena de texto de una línea del archivo que incluye al salto de línea \n. Por ejemplo: Palta|Fruta|1200
    linea_valida = linea.strip() # Crea la variable linea_valida y almacena cada linea del for eliminando los espacios en blanco del principio y el final de la línea, las tabulaciones y los saltos de línea (\n).
    if linea_valida: # Verifica que la línea no esté vacía. Evitando procesar líneas en blanco.
        datos = linea_valida.split('|') # Divide la línea en partes separadas por '|'. Por ejemplo, si la línea es "Pan|Alimentos|2500", esto se convierte en datos en: ['Pan', 'Alimentos', '50'].
        if len(datos) == 3: # Asegura que se hayan obtenido exactamente 3 elementos (nombre, categoría y precio). Es una forma básica de validar que la línea está bien formada.
            productos.append(datos) # Agrega a la lista principal lista productos lo almacenados en datos [nombre, categoría, precio] con .append()
archivo.close() # Habiéndo cargado en la RAM lo que haya en "invnetario.txt" se cierra el archivo.

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
   
    opcion = input(f"\nIngresa el número de la opción deseada: ")
   
    if opcion == "1":
        print("\nAgregar Nuevo Producto:\n")
       
        nombre = input("\tNombre: ").strip().capitalize()
        categoria = input("\tCategoría: ").strip().capitalize()
        precio = input("\tPrecio: ")
       
        if not precio.isdigit() or int(precio) <= 0:
            print("El precio debe ser un entero positivo.")
            continue
       
        precio_ingresado = int(precio)
        productos.append([nombre, categoria, precio_ingresado])
       
       # Habiéndo cargado previamente el inventario.txt a la RAM, cualquier operación que se haga con el código se puede guardar.
        archivo = open("inventario.txt", "a", encoding="utf-8") # Abre con "a" el inventario que permite añadir elementos nuevos a la última línea del archivo intentario.
        archivo.write(f"{nombre}|{categoria}|{precio_ingresado}\n") # Escribe (o guarda en el archivo) los valores de las variables nombre, categoria y precio. Si el inventario tiene 15 líneas, por ejemplo, al estar abierto con "a" guarda esos valores en la línea 16.
        archivo.close() # Cierra el archivo. 
       
        print(f"\n'{nombre}' se agregó al inventario.\n")
        continue
    
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
            print("Número del producto inexistente. Intente de nuevo.")
            continue
       
        eliminado = productos.pop(producto_a_eliminar - 1)
        print(f"Producto '{eliminado[0]}' eliminado.")
       
        archivo = open("inventario.txt", "w", encoding="utf-8") # Abre el archivo con "w" para sobrescribir los registros si hay modificaciones en el órden del inventario.
        for producto in productos: # Recorre la lista principal, tal como esté en la RAM en ese momento de la ejecución y recorre cada elemento con "producto" de la lista "productos"
            archivo.write(f"{producto[0]}|{producto[1]}|{producto[2]}\n") # En cada vuelta del for pasa por cada registro y pisa (sobrescribe) los valores de la RAM en el archivo "inventario.txt".
        archivo.close() # Cierra el archivo.
       
    elif opcion == "3": # Buscar: no necesita código para operar en el archivo "inventario.txt" porque sólo opera con los datos de la RAM.
        print("Buscar Productos")
       
        buscar = input("Ingrese el nombre del producto a buscar: ").strip()
       
        busqueda = []
        for producto in productos:
            if buscar.lower() in producto[0].lower():
                busqueda.append(producto)
               
        print("\nResultados de la Búsqueda:\n")
       
        if busqueda:
            for i in range(len(busqueda)):
                print(f"\t{i + 1}. {busqueda[i][0]} | Categoría: {busqueda[i][1]} | Precio: {busqueda[i][2]}")
        else:
            print("No se encontraron productos.")
           
    elif opcion == "4": # Mostrar: No necesita código para trabajar con el archivo "inventario.txt" porque trabaja con los datos de la RAM.
        if len(productos) <= 0:
            print("No hay productos en el inventario.")
        else:
            for i in range(len(productos)):
                print(f"\t{i + 1}. Nombre: {productos[i][0]} | Categoría: {productos[i][1]} | Precio: {productos[i][2]}")
               
    elif opcion == "5":
        print("\nPrograma finalizado.\n")
        break
    else:
        print("Ingrese un número válido.")