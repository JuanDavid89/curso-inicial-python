# Proyecto Final

import sqlite3
from colorama import Fore, Style, init
# Inicializar colorama
init(autoreset=True)

# Conexión a la base de datos
conexion = sqlite3.connect("inventario.db")
cursor = conexion.cursor()

# Crear la tabla de productos
cursor.execute('''
               CREATE TABLE IF NOT EXISTS productos (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nombre TEXT NOT NULL,
                   descripcion TEXT NOT NULL,
                   cantidad INTEGER NOT NULL,
                   precio REAL NOT NULL,
                   categoria TEXT NOT NULL
               )
               ''')

conexion.commit()
conexion.close()

print("Base de datos y tabla productos creadas con éxito.")

# Función para agregar producto
def agregar_producto(nombre, descripcion, cantidad, precio, categoria):
    cursor.execute("INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria) VALUES (?, ?, ?, ?, ?)", (nombre, descripcion, cantidad, precio, categoria))
    conexion.commit()
    print("El producto fue agregado exitosamente.")
 
# Función para mostrar todos los productos    
def mostrar_productos():
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    print("\nLista de Productos\n")
    
    for producto in productos:
        print(f"ID: {producto[0]}, Nombre: {producto[1]}, Descripción: {producto[2]}, Cantidad: {producto[3]}, Precio: {producto[4]}, Categoria: {producto[5]}")

# Función para actualizar todos los campos de un producto        
def actualizar_producto(id_producto, nuevo_producto):
    cursor.execute("UPDATE productos SET nombre = ? WHERE id = ?", (nuevo_producto, id_producto))
    conexion.commit()
    print(f"\nProducto: {nuevo_producto} actualizado exitosamente en el ID: {id_producto}.")

# Función para eliminar un producto    
def eliminar_producto(id_producto):
    cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))
    conexion.commit()
    print(f"\nProducto con ID {id_producto} eliminado exitosamente.")
    
# Función para buscar producto por ID
def buscar_producto_por_id(id_producto):
    cursor.execute("SELECT * FROM productos WHERE id = ?", (id_producto,))
    producto = cursor.fetchone()
    if producto:
        print(f"""
Producto encontrado:
ID: {producto[0]}, Nombre: {producto[1]}, Descripción: {producto[2]},
Cantidad: {producto[3]}, Precio: ${producto[4]}, Categoría: {producto[5]}
""")
    else:
        print("⚠ No se encontró ningún producto con ese ID.")

# Función para reporte de stock bajo
def reporte_stock_bajo(limite):
    cursor.execute("SELECT * FROM productos WHERE cantidad <= ?", (limite,))
    productos = cursor.fetchall()
    if productos:
        print(f"\nProductos con stock igual o menor a {limite}:\n")
        for producto in productos:
            print(f"ID: {producto[0]}, Nombre: {producto[1]}, Cantidad: {producto[3]}")
    else:
        print("Todos los productos tienen suficiente stock.")

# Menú de opciones a seleccionar
while True:
    print("\n================ Gestión de Productos ==========================")
    print("1. Agregar producto")
    print("2. Mostrar producto")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Actualizar producto")
    print("6. Eliminar producto")
    print("============================================================")
    print("7. Salir")
    print("============================================================")

    opcion = input("Seleccione una opción entre 1 y 7: ").strip()

    if not opcion.isdigit():
        print("Debe ingresar solo números.")
        continue

    opcion = int(opcion)

    if opcion == 1:
        nombre = input("Ingrese el nombre del producto: ").strip()
        descripcion = input("Ingrese una breve descripción del producto: ").strip()
        cantidad = input("Ingrese la cantidad del producto: ").strip()
        precio = input("Ingrese el precio del producto: ").strip()
        categoria = input("Ingrese la categoria del producto: ").strip()
        
        if cantidad.isdigit() and int(cantidad) > 0:
        # Se valida que la cantidad sea un número entero mayor a 0
            try:
                precio_float = float(precio)
                agregar_producto(
                    nombre=nombre,
                    descripcion=descripcion,
                    cantidad=int(cantidad),
                    precio=precio_float,
                    categoria=categoria
                )
                print("Producto agregado correctamente.")
            except ValueError:
                print("El precio debe ser un número válido (ej: 12.50).")
        else:
            print("La cantidad debe ser un número entero mayor a 0.")
            
    elif opcion == 2:
        mostrar_productos()
             
    elif opcion == 3:
        mostrar_productos()
        id_producto = input("\nIngrese el ID del producto a actualizar: ").strip()
        nuevo_producto = input("Ingrese el nuevo producto: ").strip()
        
        if id_producto.isdigit():
            actualizar_producto(int(id_producto), nuevo_producto)
        else:
            print("El ID debe ser un número válido.")
            

    elif opcion == 4:
        mostrar_productos()
        
        id_producto = input("\nIngrese el ID del producto a eliminar: ").strip()
        if id_producto.isdigit():
            eliminar_producto(int(id_producto))
        else:
            print("El ID debe ser un número válido.")
        
    elif opcion == 5:
        id_producto = input("\nIngrese el ID del producto a buscar: ").strip()
        if id_producto.isdigit():
            buscar_producto_por_id(int(id_producto))
        else:
            print("El ID debe ser un número válido.")

    elif opcion == 6:
        limite = input("\nMostrar productos con stock menor o igual a: ").strip()
        if limite.isdigit():
            reporte_stock_bajo(int(limite))
        else:
            print("El límite debe ser un número entero.")
    
    elif opcion == 7:        
        print("============================================================\n")
        print("                   Fin del programa...")
        print("\n============================================================\n")
        break
    
    else:
        print("Opción fuera de rango (1-5). Intente nuevamente.")
        
print("============================================================")
print("              Desarrollado por: Juan Saavedra            ")
print("============================================================\n")

conexion.close()