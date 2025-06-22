import sqlite3

conexion = sqlite3.connect("productos_ejercicio.db")
cursor = conexion.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS productos (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nombre TEXT NOT NULL,
                   precio REAL NOT NULL
               )
               ''')

# Para insertar datos
#cursor.execute('''
#             INSERT INTO productos (nombre, precio) VALUES (?, ?)''', ("Pala Head", 200.15)
#              )

#print("El producto se agregó correctamente")

# Para realizar consultas
#cursor.execute('''SELECT * FROM productos''')
#productos = cursor.fetchall()

#print("La consulta es: ")
#for producto in productos:
#    print(f"id: {producto[0]} | Nombre: {producto[1]} | Precio: {producto[2]}")

# Consulta ordenando por precio ascendente - sería lo mismo para descendente pero hay que cambiar el ASC por DESC en la consulta
#cursor.execute('''SELECT * FROM productos ORDER BY precio ASC''')
#productosASC = cursor.fetchall()

#print("La consulta es: ")
#for producto in productosASC:
#    print(f"id: {producto[0]} | Nombre: {producto[1]} | Precio: {producto[2]}")

# Para eliminar un producto en específico
#nombre_producto = "Pala Head"
#cursor.execute("DELETE FROM productos WHERE nombre = ?",(nombre_producto,))

conexion.commit()
conexion.close()

def agregar_productos():
    nombre = input("Ingrese nombre: ")
    precio = input("Ingrese precio: ")
    
    cursor.execute('''
             INSERT INTO productos (nombre, precio) VALUES (?,?)''', (nombre, precio)
              )
    
#def mostrar_productos():

while True:    
    print("\n==== | Gestión de productos | ==== \n")
    print("1. Agregar")
    print("2. Mostrar")
    print("==============")
    print("3. Salir")
   
    opcion = input(f"\nIngresa el número de la opción deseada: ")
    
    if opcion == "1":
        agregar_productos()
 #   elif opcion == "2":
 #       mostrar_productos()