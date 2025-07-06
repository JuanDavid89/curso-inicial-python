# Proyecto Final Inventario

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
                   nombre TEXT UNIQUE NOT NULL,
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
def agregar_producto():
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    
    try:
        print(Fore.CYAN + "\n=== Registrar Nuevo Producto ===")

        # Solicitud de datos
        nombre = input("Ingrese el nombre del producto: ").strip().capitalize()
        descripcion = input("Ingrese una breve descripción del producto: ").strip().capitalize()
        cantidad = input("Ingrese la cantidad del producto: ").strip()
        precio = input("Ingrese el precio del producto: ").strip()
        categoria = input("Ingrese la categoria del producto: ").strip().capitalize()

        # Validación
        if not cantidad.isdigit() or int(cantidad) <= 0:
            print(Fore.RED + "[Error] La cantidad debe ser un número entero mayor a 0.")
            return

        try:
            precio_float = float(precio)
        except ValueError:
            print(Fore.RED + "[Error] El precio debe ser un número válido (ej: 12.50).")
            return

        # Inserción
        cursor.execute("""
            INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
            VALUES (?, ?, ?, ?, ?)
        """, (nombre, descripcion, int(cantidad), precio_float, categoria))

        conexion.commit()
        print(Fore.GREEN + f"[ÉXITO] Producto '{nombre}' agregado correctamente.")

    except sqlite3.IntegrityError:
        print(Fore.RED + "[Error] Ya existe un producto con ese nombre.")
    except sqlite3.Error as e:
        print(Fore.RED + f"[Error] Error de base de datos: {e}")
    finally:
        conexion.close()
         
# Función para mostrar todos los productos    
def mostrar_productos():
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()

    try:
        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()
        
        if productos:
            print(Fore.CYAN + "\n=== Lista de Productos ===\n")
            for producto in productos:
                print(f"ID: {producto[0]}, Nombre: {producto[1]}, Descripción: {producto[2]}, "
                      f"Cantidad: {producto[3]}, Precio: ${producto[4]}, Categoría: {producto[5]}")
        else:
            print(Fore.YELLOW + "\n[Info] No hay productos registrados.")

    except sqlite3.Error as e:
        print(Fore.RED + f"[Error] No se pudo obtener la lista de productos: {e}")

    finally:
        conexion.close()

# Función para actualizar todos los campos de un producto        
def actualizar_producto(id_producto):
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()

    try:
        cursor.execute("SELECT * FROM productos WHERE id = ?", (id_producto,))
        producto = cursor.fetchone()

        if producto:
            print(Fore.CYAN + "\nProducto encontrado:")
            print(f"ID: {producto[0]}, Nombre: {producto[1]}, Descripción: {producto[2]}, "
                  f"Cantidad: {producto[3]}, Precio: ${producto[4]}, Categoría: {producto[5]}")
            
            confirmar = input(Fore.YELLOW + "\n¿Desea actualizar este producto? (s/n): ").strip().lower()
            if confirmar != 's':
                print(Fore.BLUE + "Actualización cancelada.")
                return

            print(Fore.CYAN + "\nDeje en blanco los campos que no desea cambiar.\n")
            nuevo_nombre = input(f"Nuevo nombre [{producto[1]}]: ").strip() or producto[1]
            nueva_descripcion = input(f"Nueva descripción [{producto[2]}]: ").strip() or producto[2]
            nueva_cantidad = input(f"Nueva cantidad [{producto[3]}]: ").strip() or str(producto[3])
            nuevo_precio = input(f"Nuevo precio [{producto[4]}]: ").strip() or str(producto[4])
            nueva_categoria = input(f"Nueva categoría [{producto[5]}]: ").strip() or producto[5]

            if not nueva_cantidad.isdigit():
                print(Fore.RED + "La cantidad debe ser un número entero.")
                return
            try:
                nuevo_precio = float(nuevo_precio)
            except ValueError:
                print(Fore.RED + "El precio debe ser un número válido.")
                return

            cursor.execute("""
                UPDATE productos
                SET nombre = ?, descripcion = ?, cantidad = ?, precio = ?, categoria = ?
                WHERE id = ?
            """, (nuevo_nombre, nueva_descripcion, int(nueva_cantidad), nuevo_precio, nueva_categoria, id_producto))

            conexion.commit()
            print(Fore.GREEN + f"\n[ÉXITO] Producto ID {id_producto} actualizado correctamente.")
        else:
            print(Fore.YELLOW + "\n[INFO] No se encontró ningún producto con ese ID.")

    except sqlite3.Error as e:
        print(Fore.RED + f"[ERROR] No se pudo actualizar el producto: {e}")
    finally:
        conexion.close()

# Función para eliminar un producto    
def eliminar_producto(id_producto):
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()

    try:
        cursor.execute("SELECT * FROM productos WHERE id = ?", (id_producto,))
        producto = cursor.fetchone()

        if producto:
            print(Fore.CYAN + "\nProducto encontrado:")
            print(f"ID: {producto[0]}, Nombre: {producto[1]}, Descripción: {producto[2]}, "
                  f"Cantidad: {producto[3]}, Precio: ${producto[4]}, Categoría: {producto[5]}")
            
            confirmar = input(Fore.YELLOW + "\n¿Está seguro que desea eliminar este producto? (s/n): ").strip().lower()
            if confirmar != 's':
                print(Fore.BLUE + "Eliminación cancelada.")
                return

            cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))
            conexion.commit()
            print(Fore.GREEN + f"\n[ÉXITO] Producto con ID {id_producto} eliminado correctamente.")
        else:
            print(Fore.YELLOW + f"\n[INFO] No se encontró ningún producto con ID {id_producto}.")

    except sqlite3.Error as e:
        print(Fore.RED + f"[ERROR] No se pudo eliminar el producto: {e}")
    finally:
        conexion.close()
    
# Función para buscar producto por ID, Nombre o Categoría
def buscar_producto():
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()

    print(Fore.CYAN + "\n=== Buscar Producto ===")
    print("Puede buscar por ID, Nombre o Categoría.")
    criterio = input("Ingrese el valor de búsqueda: ").strip()

    try:
        if criterio.isdigit():
            cursor.execute("SELECT * FROM productos WHERE id = ?", (int(criterio),))
        else:
            cursor.execute("""
                SELECT * FROM productos
                WHERE nombre LIKE ? OR categoria LIKE ?
            """, (f"%{criterio}%", f"%{criterio}%"))

        productos = cursor.fetchall()

        if productos:
            print(Fore.GREEN + "\nProductos encontrados:\n")
            for producto in productos:
                print(f"""
ID: {producto[0]}, Nombre: {producto[1]}, Descripción: {producto[2]},
Cantidad: {producto[3]}, Precio: ${producto[4]:.2f}, Categoría: {producto[5]}
                """)
        else:
            print(Fore.YELLOW + "No se encontraron productos con ese criterio.")

    except sqlite3.Error as e:
        print(Fore.RED + f"[ERROR] Error al buscar productos: {e}")

    finally:
        conexion.close()

# Función para reporte de stock bajo
def reporte_stock_bajo(limite):
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()

    try:
        cursor.execute("SELECT * FROM productos WHERE cantidad <= ?", (limite,))
        productos = cursor.fetchall()
        
        if productos:
            print(f"\nProductos con stock igual o menor a {limite}:\n")
            for producto in productos:
                print(f"ID: {producto[0]}, Nombre: {producto[1]}, Cantidad: {producto[3]}")
        else:
            print(Fore.YELLOW + "Todos los productos tienen suficiente stock.")

    except sqlite3.Error as e:
        print(Fore.RED + f"[Error] Error al consultar la base de datos: {e}")
    
    finally:
        conexion.close()

# Función para exportar datos       
def exportar_a_txt(nombre_archivo="productos_exportados.txt"):
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()

    try:
        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()

        if not productos:
            print(Fore.YELLOW + "[INFO] No hay productos para exportar.")
            return

        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            archivo.write("=== LISTADO DE PRODUCTOS ===\n\n")
            for producto in productos:
                archivo.write(f"ID: {producto[0]}\n")
                archivo.write(f"Nombre: {producto[1]}\n")
                archivo.write(f"Descripción: {producto[2]}\n")
                archivo.write(f"Cantidad: {producto[3]}\n")
                archivo.write(f"Precio: ${producto[4]:.2f}\n")
                archivo.write(f"Categoría: {producto[5]}\n")
                archivo.write("-" * 40 + "\n")

        print(Fore.GREEN + f"[ÉXITO] Productos exportados correctamente a '{nombre_archivo}'.")

    except sqlite3.Error as e:
        print(Fore.RED + f"[ERROR] No se pudieron exportar los datos: {e}")
    finally:
        conexion.close()
        
def salir_del_programa():
    print(Fore.BLUE + "\n" + "=" * 60)
    print(Fore.WHITE + "Gracias por utilizar el sistema de inventario.".center(60))
    print(Fore.WHITE + "Desarrollado por: Juan Saavedra".center(60))
    print(Fore.BLUE + "=" * 60 + "\n")

def menu():
    # Menú de opciones a seleccionar
    while True:
        print(Fore.BLUE + "\n================ Gestión de Productos =======================")
        print(Fore.WHITE + "1. Agregar producto")
        print(Fore.WHITE + "2. Mostrar producto/s")
        print(Fore.WHITE + "3. Actualizar producto")
        print(Fore.WHITE + "4. Eliminar producto")
        print(Fore.WHITE + "5. Buscar producto por ID / Nombre / Categoría")
        print(Fore.WHITE + "6. Reporte de producto por cantidad")
        print(Fore.WHITE + "7. Exportar productos a TXT")
        print(Fore.BLUE + "============================================================")
        print(Fore.WHITE + "8. Salir")
        print(Fore.BLUE + "============================================================")

        opcion = input(Fore.WHITE + "Seleccione una opción entre 1 y 8: ").strip()

        if not opcion.isdigit():
            print("Debe ingresar solo números.")
            continue
        
        opcion = int(opcion)

        if opcion == 1:
            agregar_producto()
                
        elif opcion == 2:
            mostrar_productos()
                
        elif opcion == 3:
            mostrar_productos()
            id_producto = input("\nIngrese el ID del producto a actualizar: ").strip()
            if id_producto.isdigit():
                actualizar_producto(int(id_producto))
            else:
                print(Fore.RED + "El ID debe ser un número válido.")

        elif opcion == 4:
            mostrar_productos()
            id_producto = input("\nIngrese el ID del producto a eliminar: ").strip()
            if id_producto.isdigit():
                eliminar_producto(int(id_producto))
            else:
                print(Fore.RED + "El ID debe ser un número válido.")
            
        elif opcion == 5:
            buscar_producto()

        elif opcion == 6:
            limite = input("\nMostrar productos con stock menor o igual a: ").strip()
            if limite.isdigit():
                reporte_stock_bajo(int(limite))
            else:
                print(Fore.RED + "El límite debe ser un número entero.")
        
        elif opcion == 7:
            exportar_a_txt()
            
        elif opcion == 8:
            salir_del_programa()
            break

        
menu()
